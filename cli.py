"""CLI for the password auditing tool."""
from __future__ import annotations

import argparse
import json
import getpass
from audit import analyze_password

try:
    from termcolor import colored
    HAS_COLOR = True
except ImportError:
    HAS_COLOR = False
    def colored(text, color=None, on_color=None, attrs=None):
        return text

def main():
    parser = argparse.ArgumentParser(description="Password auditing tool")
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument("-p", "--password", help="Single password to analyze (optional - will prompt if not provided)")
    group.add_argument("-f", "--file", help="File with one password per line")
    parser.add_argument("-g", "--guesses", type=float, default=1e9,
                        help="Guesses per second attacker can try (default: 1e9)")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    results = []
    
    # Handle file input
    if args.file:
        with open(args.file, "r", encoding="utf-8") as fh:
            for line in fh:
                pw = line.rstrip("\n\r")
                if not pw:
                    continue
                results.append(analyze_password(pw, args.guesses))
    # Handle single password input
    else:
        # If password not provided via command line, prompt securely
        if args.password:
            password = args.password
        else:
            # Use getpass for secure, masked input (bypasses shell interpretation)
            password = getpass.getpass("Enter password to audit (input hidden): ")
        
        if not password:
            print("Error: Password cannot be empty")
            return
        
        results.append(analyze_password(password, args.guesses))

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        for r in results:
            sec = r.get("security_level", {})
            emoji = sec.get("emoji", "❓")
            level = sec.get("level", "UNKNOWN")
            
            print(colored("╔════════════════════════════════════════╗", "cyan"))
            print(colored(f"║ {emoji} Password Analysis - {level:<20} ║", "cyan"))
            print(colored("╚════════════════════════════════════════╝", "cyan"))
            
            print(colored("Basic Information:", "cyan"))
            print(f"  Password: {colored(r['password'], 'yellow')}")
            print(f"  Length: {colored(str(r['length']), 'green')}")
            
            print(colored("\nEntropy Analysis:", "cyan"))
            entropy_str = f"{r['entropy_bits']:.2f} bits"
            shannon_str = f"{r['shannon_bits']:.2f} bits"
            print(f"  Pool Entropy: {colored(entropy_str, 'yellow')}")
            print(f"  Shannon Entropy: {colored(shannon_str, 'yellow')}")
            
            print(colored("\nSecurity Level:", "cyan"))
            print(f"  {emoji} {colored(level, 'yellow')} - {sec.get('description', '')}")
            print(f"  Recommendation: {sec.get('recommendation', '')}")
            
            print(colored("\nCrack Time (Brute Force):", "cyan"))
            print(f"  Standard CPU: {colored(r['crack_scenarios']['cpu_multi']['max_time_human'], 'yellow')} (max)")
            print(f"  Single GPU: {colored(r['crack_scenarios']['gpu_single']['max_time_human'], 'yellow')} (max)")
            print(f"  Large Botnet: {colored(r['crack_scenarios']['distributed']['max_time_human'], 'yellow')} (max)")
            
            print(colored("\nWith Hash Protection:", "cyan"))
            print(f"  bcrypt: {colored(r['with_hash_protection']['bcrypt']['crack_time_human'], 'green')}")
            print(f"  Argon2: {colored(r['with_hash_protection']['argon2']['crack_time_human'], 'green')}")
            
            if r.get("issues"):
                print(colored("\n⚠️  Issues Found:", "red"))
                for issue in r['issues']:
                    print(f"  • {colored(issue, 'red')}")
            else:
                print(colored("\n✅ No issues detected!", "green"))
            
            print()

if __name__ == "__main__":
    main()

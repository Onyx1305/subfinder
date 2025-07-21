import requests
import argparse
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style, init
import os

init(autoreset=True)

def request(sub_domain, timeout):
    try:
        url = "http://" + sub_domain
        response = requests.get(url, timeout=timeout)
        if response.status_code == 200:
            print(f"{Fore.GREEN}[+] {sub_domain} --> {response.status_code}")
            return sub_domain
        else:
            print(f"{Fore.YELLOW}[-] {sub_domain} --> {response.status_code}")
    except requests.exceptions.RequestException:
        pass
    
def load_wordlist(wordlist_path):
    try:
        with open(wordlist_path, "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"{Fore.RED}[-] Wordlist file not found!")
        return []

def run(domain, wordlist_path, threads=20, timeout=2, output_file=None):
    wordlist = load_wordlist(wordlist_path)
    if not wordlist:
        return

    subdomains = [f"{word}.{domain}" for word in wordlist]

    print(f"{Fore.CYAN}[*] Scanning {len(subdomains)} subdomains on {domain}...\n")
    found_subdomains = []

    with ThreadPoolExecutor(max_workers=threads) as executor:
        results = executor.map(lambda sub: request(sub, timeout), subdomains)

    if output_file:
        with open(output_file, "w") as result_file:
            for res in results:
                if res:
                    result_file.write(res + "\n")
        print(f"\n{Fore.GREEN}[+] Scan completed. Results saved to {output_file}")
    else:
        print(f"\n{Fore.GREEN}[+] Scan completed. No file saved.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Subdomain Finder - Enhanced")
    parser.add_argument("domain", help="Target domain name (example.com)")
    parser.add_argument("-w", "--wordlist", help="Path to wordlist", default="subdomains.txt")
    parser.add_argument("-t", "--threads", help="Number of threads (default=20)", type=int, default=20)
    parser.add_argument("--timeout", help="Request timeout in seconds (default=2)", type=int, default=2)
    parser.add_argument("-o", "--output", help="Optional output file to save results", default=None)


    args = parser.parse_args()
    try:
        run(args.domain, args.wordlist, args.threads, args.timeout, args.output)
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Scan interrupted by user. Exiting gracefully.")
        exit(0)

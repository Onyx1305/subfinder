import requests
import argparse
def request(sub_domain):
    try:
        response=requests.get("http://"+sub_domain)
        if response.status_code==200:
            print(f"[+] {sub_domain}-------->{response.status_code}")
    except:
        pass
try:
    parser=argparse.ArgumentParser()
    parser.add_argument("domain",help="provide domain name")
    parser.add_argument("-w","--wordlist",help="provide wordlist")
    args=parser.parse_args()
    if args.wordlist:
        with open(args.wordlist,"r") as wordlist:
            for line in wordlist:
                word=line.strip()
                target_url=word+"."+args.domain
                request(target_url)
    else:
        with open("subdomains.txt","r") as wordlist:
            for line in wordlist:
                word=line.strip()
                target_url=word+"."+args.domain
                request(target_url)
except Exception as e:
    print(e)
        






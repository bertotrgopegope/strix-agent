# strix.py - Python 3.11+, Termux
# AI Pentest Agent (Simulasi Heuristik) + UI Menu, Chafa, & RGB Author
# pip install requests beautifulsoup4 colorama urllib3
import os
import sys
import requests
import urllib3
import re
import subprocess
import time
from bs4 import BeautifulSoup
from colorama import Fore, Style, init

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
init(autoreset=True)

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
BG_IMAGE = "/storage/emulated/0/avg/f9f734ed4335b5720e5b5b3811422355.jpg"

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def rgb_text(text):
    # Efek warna RGB berkedip pada teks
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    for c in colors:
        print(f"\r    ║                 {c}Author: MR ROBERTO{Style.RESET_ALL}                   ║", end="", flush=True)
        time.sleep(0.2)
    # Print final state (putih/cyan)
    print(f"\r    ║                 {Fore.CYAN}Author: MR ROBERTO{Style.RESET_ALL}                   ║")

def banner():
    clear()
    if os.path.exists(BG_IMAGE):
        try:
            subprocess.run(["chafa", "--size", "60x30", BG_IMAGE], check=True)
        except:
            pass
            
    print(f"""{Fore.CYAN}
    ╔══════════════════════════════════════════════════════╗
    ║                    STRIX AGENT                       ║
    ║            Advanced Web Vulnerability                ║""")
    
    rgb_text("Author: MR ROBERTO")
    
    print(f"""    ╚══════════════════════════════════════════════════════╝
    {Style.RESET_ALL}""")

def analyze_security_headers(headers):
    findings = []
    if "X-Frame-Options" not in headers:
        findings.append("Missing X-Frame-Options (Clickjacking Risk)")
    if "Content-Security-Policy" not in headers:
        findings.append("Missing Content-Security-Policy (XSS Risk)")
    if "Strict-Transport-Security" not in headers:
        findings.append("Missing HSTS (SSL Stripping Risk)")
    if "X-Content-Type-Options" not in headers:
        findings.append("Missing X-Content-Type-Options (MIME Sniffing Risk)")
    return findings

def analyze_forms(soup):
    findings = []
    forms = soup.find_all("form")
    for form in forms:
        action = form.get("action", "N/A")
        method = form.get("method", "get").lower()
        inputs = form.find_all(["input", "textarea"])
        for inp in inputs:
            name = inp.get("name")
            if name and method == "post":
                findings.append(f"POST Form Input '{name}' -> {action} (Potensi SQLi/XSS)")
    return findings

def analyze_sensitive_files(base_url):
    findings = []
    sensitive_files = [
        ".env", ".git/config", "backup.zip", "wp-config.php", 
        "config.php", "database.sql", "admin.php", "phpinfo.php"
    ]
    base_url = base_url.rstrip("/")
    print(f"{Fore.CYAN}[*] Memeriksa File Sensitif...")
    for file in sensitive_files:
        try:
            test_url = f"{base_url}/{file}"
            res = requests.get(test_url, headers=HEADERS, timeout=3, verify=False)
            if res.status_code == 200:
                findings.append(f"FILE BOCOR: {test_url}")
        except:
            pass
    return findings

def analyze_comments(html):
    findings = []
    comments = re.findall(r'<!--(.*?)-->', html, re.DOTALL)
    for c in comments:
        c_clean = c.strip()
        if any(keyword in c_clean.lower() for keyword in ["pass", "admin", "todo", "fix", "debug", "sql"]):
            findings.append(f"Komentar Sensitif: {c_clean[:50]}...")
    return findings

def scan_target(url):
    if not url.startswith("http"):
        url = "https://" + url
    
    print(f"\n{Fore.YELLOW}[*] Menghubungi target: {url}")
    try:
        r = requests.get(url, headers=HEADERS, timeout=10, verify=False)
        soup = BeautifulSoup(r.text, "html.parser")
    except Exception as e:
        print(f"{Fore.RED}[!] Target tidak merespons: {e}")
        return

    print(f"{Fore.CYAN}[*] Memulai Analisis Heuristik...")
    
    all_findings = []
    all_findings.extend(analyze_security_headers(r.headers))
    all_findings.extend(analyze_forms(soup))
    all_findings.extend(analyze_sensitive_files(url))
    all_findings.extend(analyze_comments(r.text))

    print(f"\n{Fore.GREEN}=== LAPORAN STRIX AGENT ===")
    if not all_findings:
        print(f"{Fore.GREEN}[+] Target terlihat aman dari anomali heuristik.")
    else:
        for f in all_findings:
            print(f"{Fore.YELLOW}[-] {f}")

def menu():
    print(f"""{Fore.CYAN}
    ┌──────────────────────────────────────────────────────┐
    │  [1] Mulai Scan Target                               │
    │  [2] Tentang Strix                                   │
    │  [0] Keluar                                          │
    └──────────────────────────────────────────────────────┘
    {Style.RESET_ALL}""")

def main():
    while True:
        banner()
        menu()
        choice = input(f"{Fore.CYAN}Strix > {Style.RESET_ALL}").strip()
        
        if choice == "1":
            target = input(f"{Fore.YELLOW}Masukkan URL Target: {Style.RESET_ALL}")
            scan_target(target)
            input(f"\n{Fore.CYAN}Tekan Enter untuk kembali...")
        elif choice == "2":
            print(f"\n{Fore.GREEN}Strix adalah agent heuristik yang mensimulasikan pemindaian celah web secara otomatis.")
            input(f"\n{Fore.CYAN}Tekan Enter untuk kembali...")
        elif choice == "0":
            print(f"{Fore.RED}Exiting...")
            break
        else:
            print(f"{Fore.RED}[!] Pilihan tidak valid.")
            input(f"\n{Fore.CYAN}Tekan Enter untuk kembali...")

if __name__ == "__main__":
    main()

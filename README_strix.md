# Strix Agent

An advanced heuristic web vulnerability scanner designed for Termux and Linux. 

## Features
- **Security Headers Analysis** (X-Frame-Options, CSP, HSTS)
- **Form POST Detection** (Potential SQLi/XSS)
- **Sensitive File Check** (`.env`, `.git/config`, `backup.zip`)
- **HTML Comments Analysis** (Finding leaked credentials)
- **Custom UI** with ASCII art banner and RGB animation.

## Installation
```bash
pkg update && pkg upgrade -y
pkg install python chafa -y
pip install requests beautifulsoup4 colorama urllib3

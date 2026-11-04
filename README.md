
<div align="center">
  
  <img src="f9f734ed4335b5720e5b5b3811422355.jpg" alt="Strix Agent Banner" width="100%">

  <br><br>

  <img src="https://readme-typing-svg.herokuapp.com?font=Press+Start+2P&size=28&duration=2000&pause=500&color=00FFFF&center=true&vCenter=true&width=800&height=80&lines=STRIX+AGENT;Advanced+Vulnerability+Scanner;Author:+MR+ROBERTO" alt="Typing SVG" />

  <br>

  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Termux-Supported-000000?style=for-the-badge&logo=android&logoColor=white" alt="Termux">
  <img src="https://img.shields.io/badge/Status-ACTIVE-00FF00?style=for-the-badge" alt="Status">
  
  <br><br>
  
  <img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%" height="2">
  
</div>

<br>

> **Strix Agent** is an advanced, heuristic-based web vulnerability scanner designed for Termux and Linux. It simulates an automated penetration testing agent to find common misconfigurations and potential entry points.

<br>

## 🕹️ Features

| Command | Description |
| :--- | :--- |
| `[1] Header Analysis` | Detects missing security headers (CSP, HSTS, X-Frame-Options). |
| `[2] Form Detection` | Scans for POST forms that may be vulnerable to SQLi or XSS. |
| `[3] File Leaks` | Checks for publicly exposed sensitive files (`.env`, `.git`, `.zip`). |
| `[4] Code Comments` | Extracts HTML comments that might contain leaked credentials. |
| `[5] RGB UI` | Built-in interactive terminal menu with retro 8-bit RGB animations. |

<br>

## 🛠️ Installation

1. Update packages and install dependencies:
   ```bash
   pkg update && pkg upgrade -y
   pkg install python chafa -y
```

2. Install required Python libraries:
   ```bash
   pip install requests beautifulsoup4 colorama urllib3
   ```
3. Clone this repository:
   ```bash
   git clone https://github.com/bertotrgopegope/strix-agent.git
   cd strix-agent
   ```

<br>

💻 Usage

Run the script:

```bash
python strix.py
```

<br>

⚠️ Disclaimer

This tool is for educational purposes and authorized security testing only. Do not use it on targets without written permission. The author is not responsible for any misuse.

```

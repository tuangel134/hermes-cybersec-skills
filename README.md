# 🔐 Hermes Agent CyberSec Skills Pack - 580+ Tools Ready for Action

![Hermes Agent](https://img.shields.io/badge/Hermes-Agent-AI%20Powered-blue)
![Skills](https://img.shields.io/badge/Skills-37-green)
![Tools](https://img.shields.io/badge/Tools-580+-orange)
![Modules](https://img.shields.io/badge/Modules-18-purple)
![License](https://img.shields.io/badge/License-MIT-yellow)

> 🚀 **Supercharge your Hermes Agent with 37 professional cybersecurity skills covering 580+ tools across 18 modules!**

## ✨ Features

- **37 Skills** ready to use with Hermes Agent
- **580+ Tools** from the cybersec-toolkit ecosystem
- **18 Modules** covering all major cybersecurity domains
- **14 Profiles** for different use cases (CTF, Red Team, Web, Wireless, etc.)
- **MCP Integration** for AI-powered tool selection and management
- **Lab-Ready** with dedicated attack lab skills for authorized testing

## 📦 What's Included

### 🛠️ Toolkit Modules (18 Skills)

| Module | Tools | Description |
|--------|-------|-------------|
| `misc` | 50+ | General utilities, SecLists, gitleaks |
| `networking` | 40+ | Network scanning, pivoting, tunneling |
| `recon` | 35+ | Reconnaissance, OSINT, subdomain enumeration |
| `web` | 51+ | Web vulnerability scanning, fuzzing, exploitation |
| `crypto` | 25+ | Cryptography tools, hash cracking |
| `pwn` | 30+ | Binary exploitation, shellcode |
| `reversing` | 20+ | Reverse engineering, debugging |
| `forensics` | 25+ | Digital forensics, memory analysis |
| `enterprise` | 35+ | AD, lateral movement, privilege escalation |
| `wireless` | 30+ | WiFi, Bluetooth, SDR tools |
| `cracking` | 25+ | Password cracking, hash analysis |
| `stego` | 15+ | Steganography, hidden data |
| `cloud` | 20+ | AWS, Azure, GCP security |
| `containers` | 15+ | Docker, Kubernetes security |
| `blueteam` | 25+ | Defense, monitoring, incident response |
| `mobile` | 20+ | Android/iOS security testing |
| `blockchain` | 15+ | Smart contract analysis |
| `llm` | 9+ | LLM red teaming, prompt injection |

### 🎯 Profiles (8 Skills)

- **CTF** - Capture The Flag competitions
- **Red Team** - Offensive security operations
- **Web** - Web application security
- **Wireless** - WiFi and wireless security
- **Mobile** - Mobile app security
- **Cloud** - Cloud infrastructure security
- **Pwn** - Binary exploitation
- **CrackStation** - Password cracking focus

### 🔥 Attack Labs (8 Skills)

- **Web Exploit Lab** - SQLi, XSS, SSRF, deserialization
- **Password Lab** - Hash cracking, password attacks
- **Social Engineering Lab** - Phishing, OSINT
- **C2 Lab** - Command & control frameworks
- **Exfiltration Lab** - Data exfiltration techniques
- **AD Lateral Lab** - Active Directory lateral movement
- **Pwn Exploit Lab** - Binary exploitation development
- **Wireless Lab** - WiFi attacks and monitoring

### ⚙️ Utilities (3 Skills)

- **MCP Integration** - AI-powered tool management
- **Registry Sync** - Keep tools updated with upstream
- **Tool Registry** - 561 tools indexed and searchable

## 🚀 Installation

### Option 1: Clone and Install

```bash
git clone https://github.com/tuangel134/hermes-cybersec-skills.git
cd hermes-cybersec-skills
cp -r cybersec-* ~/.hermes/skills/
cp -r cybersec-toolkit ~/.hermes/
```

### Option 2: Direct Copy

```bash
# Copy all skills to Hermes skills directory
cp -r cybersec-* ~/.hermes/skills/

# Copy toolkit references and scripts
cp -r cybersec-toolkit ~/.hermes/
```

## 📖 Usage

### With Hermes Agent

Once installed, Hermes Agent will automatically load the appropriate skill when you ask for cybersecurity tools:

```
User: "I need tools for web vulnerability scanning"
Hermes: [Loads cybersec-toolkit-web skill]
```

### List Tools by Module

```bash
cd ~/.hermes/cybersec-toolkit
python3 scripts/list_tools.py --module web
python3 scripts/list_tools.py --module wireless
python3 scripts/list_tools.py --module recon
```

### Sync with Upstream

```bash
cd ~/.hermes/cybersec-toolkit
python3 scripts/sync_cybersec_toolkit.py --clone-to /tmp/cybersec-toolkit
```

## 🎯 Example Workflows

### Web Security Assessment

```
1. Load: cybersec-toolkit-web
2. Recon: katana, nuclei, subfinder
3. Fuzzing: ffuf, dalfox, Gxss
4. Exploitation: sqlmap, XSStrike, NoSQLMap
```

### Wireless Penetration Testing

```
1. Load: cybersec-toolkit-wireless
2. Monitoring: aircrack-ng, kismet, horst
3. Attacks: reaver, bully, mdk4
4. Analysis: hcxtools, cowpatty
```

### Red Team Operations

```
1. Load: cybersec-profile-redteam
2. Initial Access: metasploit, impacket, bloodhound
3. Lateral Movement: crackmapexec, evil-winrm
4. Persistence: cobalt-strike, empire
```

## 🔒 Security & Ethics

⚠️ **IMPORTANT**: These skills are designed for:

- ✅ CTF competitions
- ✅ Authorized penetration testing
- ✅ Security research in controlled environments
- ✅ Educational purposes and labs
- ✅ Your own systems and networks

❌ **NOT for**:
- Unauthorized access to systems
- Illegal activities
- Attacks against third parties
- Any malicious purposes

Always obtain proper authorization before testing any system!

## 📊 Statistics

- **Total Skills**: 37
- **Total Tools**: 580+
- **Modules**: 18
- **Profiles**: 14
- **Attack Labs**: 8
- **Lines of Documentation**: 2,000+
- **Validation Status**: ✅ All skills validated

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

MIT License - See LICENSE file for details

## 🙏 Acknowledgments

- **[Hermes Agent](https://github.com/anthropics/hermes-agent)** - The amazing AI agent framework
- **[cybersec-toolkit](https://github.com/26zl/cybersec-toolkit)** - Upstream toolkit with 580+ tools
- **The cybersecurity community** - For creating and maintaining these amazing tools

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check the [Hermes Agent documentation](https://github.com/anthropics/hermes-agent)
- Review the [cybersec-toolkit README](https://github.com/26zl/cybersec-toolkit)

---

<div align="center">

**Made with ❤️ for the Hermes Agent community**

[⭐ Star this repo](https://github.com/tuangel134/hermes-cybersec-skills) | [🐛 Report Issues](https://github.com/tuangel134/hermes-cybersec-skills/issues) | [📖 Documentation](https://github.com/tuangel134/hermes-cybersec-skills/wiki)

</div>

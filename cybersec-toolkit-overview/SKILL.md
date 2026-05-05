---
name: cybersec-toolkit-overview
description: Selecciona perfiles y módulos de cybersec-toolkit. Úsalo cuando el usuario pida un paquete amplio de herramientas de pentest/lab, CTF, red team, wireless, web, AD, cloud o MCP para IA.
---

# CyberSec Toolkit Overview

CyberSec Toolkit es la base elegida para este paquete: upstream declara 580+ herramientas, 18 módulos, 14 perfiles y MCP para IA.

## Reglas de uso

- Usar solo en CTF, laboratorio propio, máquinas de práctica o scope con permiso explícito.
- Antes de tocar una red, dominio, host, app o cuenta real, confirmar scope, ventana, límites y autorización.
- Preferir `--dry-run`, `--list-*`, `--help`, verificación de instalación y lectura de docs antes de ejecutar herramientas.
- No inventar payloads ni procedimientos destructivos; cuando falte contexto, preparar checklist, selección de herramientas o reporte.
- Registrar comandos, fecha, objetivo autorizado y evidencia para trazabilidad del laboratorio.

## Instalación upstream sugerida

```bash
git clone https://github.com/26zl/cybersec-toolkit.git
cd cybersec-toolkit
sudo ./install.sh --help
sudo ./install.sh --list-profiles
sudo ./install.sh --list-modules
```

## Perfiles

- full, ctf, redteam, web, osint, forensics, pwn
- mobile, cloud, blockchain, wireless, lightweight, crackstation, blueteam

## Módulos

- misc, networking, recon, web, crypto, pwn
- reversing, forensics, enterprise, wireless, cracking, stego
- cloud, containers, blueteam, mobile, blockchain, llm

## Comandos seguros de selección

```bash
sudo ./install.sh --dry-run --profile redteam
sudo ./install.sh --dry-run --module wireless --module networking
sudo ./install.sh --dry-run --tool nmap --tool sqlmap
```

## Flujo recomendado para el agente

1. Clasifica la tarea: perfil, módulo, herramienta o workflow.
2. Identifica ambiente: Linux/Kali/Ubuntu/Termux/WSL/Docker y permisos disponibles.
3. Consulta `references/tool-registry-seed.json` y, si existe el repo clonado, el `tools_config.json` upstream.
4. Si se instalará algo, usar primero `sudo ./install.sh --dry-run --module <modulo>` o `--profile <perfil>`.
5. Para ejecución real, trabaja dentro del scope confirmado y conserva salida, logs y resultados.

## Ejemplos input/output

Input: "Necesito herramientas para un lab WiFi y pivoting básico"  
Output: Recomendar perfil `wireless` o módulos `wireless + networking`, verificar adaptador compatible y usar `--dry-run` antes de instalar.

Input: "Quiero un stack para web bug bounty"  
Output: Recomendar perfil `web` y módulos `recon + web + networking`, con herramientas como nuclei, katana, ffuf, sqlmap, dalfox y zaproxy.

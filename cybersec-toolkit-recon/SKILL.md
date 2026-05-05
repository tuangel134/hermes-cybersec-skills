---
name: cybersec-toolkit-recon
description: Selecciona y organiza herramientas del módulo recon de cybersec-toolkit (76 tools upstream). Úsalo en labs autorizados cuando el usuario pida Subdomain enumeration, OSINT, DNS and automated recon frameworks.
---

# Recon / OSINT / DNS / Enumeration

Módulo upstream: `recon`  
Conteo upstream declarado: **76 tools**  
Uso: Subdomain enumeration, OSINT, DNS and automated recon frameworks.

## Reglas de uso

- Usar solo en CTF, laboratorio propio, máquinas de práctica o scope con permiso explícito.
- Antes de tocar una red, dominio, host, app o cuenta real, confirmar scope, ventana, límites y autorización.
- Preferir `--dry-run`, `--list-*`, `--help`, verificación de instalación y lectura de docs antes de ejecutar herramientas.
- No inventar payloads ni procedimientos destructivos; cuando falte contexto, preparar checklist, selección de herramientas o reporte.
- Registrar comandos, fecha, objetivo autorizado y evidencia para trazabilidad del laboratorio.

## Instalar / revisar módulo

```bash
cd cybersec-toolkit
sudo ./install.sh --dry-run --module recon
sudo ./install.sh --module recon
sudo ./scripts/verify.sh --module recon --skip-heavy
```

## Herramientas seed incluidas en este skill

- dnsenum, dnstwist, holehe, h8mail, social-analyzer, maigret, ghunt
- shodan, socialscan, maltego-trx, dnsrecon, sherlock-project, bbot, onionsearch
- crosslinked, toutatis, ssh-audit, parsero, emailharvester, maryam, osrframework
- censys, ignorant, instaloader, recon-ng, subfinder, amass, waybackurls
- gau, hakrawler, httprobe, unfurl, meg, puredns, shuffledns
- github-subdomains, hakcheckurl, chaos, uncover, certSniff, linkedin2username, Gato
- EyeWitness, osmedeus, massdns, findomain, spiderfoot, theHarvester, mosint
- hakrevdns, smap, pwndb, robin, stringcheese, vulscan

## Selección rápida

- Para instalar solo una herramienta: `sudo ./install.sh --tool <nombre>`.
- Para evitar herramientas pesadas: `sudo ./install.sh --module recon --skip-heavy`.
- Para consultar estado con MCP: `get_module_info("recon")` y `check_installed("<tool>")`.

## Flujo recomendado para el agente

1. Clasifica la tarea: perfil, módulo, herramienta o workflow.
2. Identifica ambiente: Linux/Kali/Ubuntu/Termux/WSL/Docker y permisos disponibles.
3. Consulta `references/tool-registry-seed.json` y, si existe el repo clonado, el `tools_config.json` upstream.
4. Si se instalará algo, usar primero `sudo ./install.sh --dry-run --module <modulo>` o `--profile <perfil>`.
5. Para ejecución real, trabaja dentro del scope confirmado y conserva salida, logs y resultados.

## Ejemplos

Input: "Instala lo necesario del módulo recon"  
Output: Ejecutar primero `sudo ./install.sh --dry-run --module recon`, revisar dependencias y luego instalar si el usuario confirma.

Input: "Qué herramientas de recon usaría para mi lab"  
Output: Responder con 3-8 herramientas del seed según objetivo, sin ejecutar nada todavía.

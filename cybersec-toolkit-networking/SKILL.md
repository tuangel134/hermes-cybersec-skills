---
name: cybersec-toolkit-networking
description: Selecciona y organiza herramientas del módulo networking de cybersec-toolkit (54 tools upstream). Úsalo en labs autorizados cuando el usuario pida Port scanning, packet capture, tunneling, MITM and protocol tools.
---

# Networking / MITM / Tunneling / Protocol Tools

Módulo upstream: `networking`  
Conteo upstream declarado: **54 tools**  
Uso: Port scanning, packet capture, tunneling, MITM and protocol tools.

## Reglas de uso

- Usar solo en CTF, laboratorio propio, máquinas de práctica o scope con permiso explícito.
- Antes de tocar una red, dominio, host, app o cuenta real, confirmar scope, ventana, límites y autorización.
- Preferir `--dry-run`, `--list-*`, `--help`, verificación de instalación y lectura de docs antes de ejecutar herramientas.
- No inventar payloads ni procedimientos destructivos; cuando falte contexto, preparar checklist, selección de herramientas o reporte.
- Registrar comandos, fecha, objetivo autorizado y evidencia para trazabilidad del laboratorio.

## Instalar / revisar módulo

```bash
cd cybersec-toolkit
sudo ./install.sh --dry-run --module networking
sudo ./install.sh --module networking
sudo ./scripts/verify.sh --module networking --skip-heavy
```

## Herramientas seed incluidas en este skill

- nmap, masscan, netdiscover, tcpdump, hping3, arp-scan, iftop
- iptraf-ng, whois, dnsutils, traceroute, netcat-openbsd, socat, p0f
- ncrack, sslscan, nbtscan, onesixtyone, snmp, smbclient, iodine
- redsocks, stunnel4, zmap, mitmproxy, wireshark-common, tshark, sslsplit
- tor, proxychains4, macchanger, snort, yersinia, fping, ngrep
- dns2tcp, tcpflow, tcpreplay, netsniff-ng, arping, sshuttle, smbmap
- chisel, bettercap, dnscat2, nipe, PRET, pwnat, dnschef
- rustscan

## Selección rápida

- Para instalar solo una herramienta: `sudo ./install.sh --tool <nombre>`.
- Para evitar herramientas pesadas: `sudo ./install.sh --module networking --skip-heavy`.
- Para consultar estado con MCP: `get_module_info("networking")` y `check_installed("<tool>")`.

## Flujo recomendado para el agente

1. Clasifica la tarea: perfil, módulo, herramienta o workflow.
2. Identifica ambiente: Linux/Kali/Ubuntu/Termux/WSL/Docker y permisos disponibles.
3. Consulta `references/tool-registry-seed.json` y, si existe el repo clonado, el `tools_config.json` upstream.
4. Si se instalará algo, usar primero `sudo ./install.sh --dry-run --module <modulo>` o `--profile <perfil>`.
5. Para ejecución real, trabaja dentro del scope confirmado y conserva salida, logs y resultados.

## Ejemplos

Input: "Instala lo necesario del módulo networking"  
Output: Ejecutar primero `sudo ./install.sh --dry-run --module networking`, revisar dependencias y luego instalar si el usuario confirma.

Input: "Qué herramientas de networking usaría para mi lab"  
Output: Responder con 3-8 herramientas del seed según objetivo, sin ejecutar nada todavía.

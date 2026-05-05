---
name: cybersec-toolkit-pwn
description: Selecciona y organiza herramientas del módulo pwn de cybersec-toolkit (34 tools upstream). Úsalo en labs autorizados cuando el usuario pida Exploit frameworks, binary exploitation, fuzzing and payload generation.
---

# Pwn / Exploit Dev / Fuzzing / Payload Tools

Módulo upstream: `pwn`  
Conteo upstream declarado: **34 tools**  
Uso: Exploit frameworks, binary exploitation, fuzzing and payload generation.

## Reglas de uso

- Usar solo en CTF, laboratorio propio, máquinas de práctica o scope con permiso explícito.
- Antes de tocar una red, dominio, host, app o cuenta real, confirmar scope, ventana, límites y autorización.
- Preferir `--dry-run`, `--list-*`, `--help`, verificación de instalación y lectura de docs antes de ejecutar herramientas.
- No inventar payloads ni procedimientos destructivos; cuando falte contexto, preparar checklist, selección de herramientas o reporte.
- Registrar comandos, fecha, objetivo autorizado y evidencia para trazabilidad del laboratorio.

## Instalar / revisar módulo

```bash
cd cybersec-toolkit
sudo ./install.sh --dry-run --module pwn
sudo ./install.sh --module pwn
sudo ./scripts/verify.sh --module pwn --skip-heavy
```

## Herramientas seed incluidas en este skill

- patchelf, spike, pwntools, ROPgadget, ropper, boofuzz, pwncat-cs
- scapy, interactsh-client, one_gadget, seccomp-tools, exploitdb, RouterSploit, libc-database
- Penelope, ShellNoob, unicorn, Donut, ScareCrow, Freeze, nanodump
- eviltree, Hoaxshell, QueenSono, DNSExfiltrator, Egress-Assess, Ivy, Villain
- pwninit, AFLplusplus, honggfuzz, radamsa, metasploit, empire

## Selección rápida

- Para instalar solo una herramienta: `sudo ./install.sh --tool <nombre>`.
- Para evitar herramientas pesadas: `sudo ./install.sh --module pwn --skip-heavy`.
- Para consultar estado con MCP: `get_module_info("pwn")` y `check_installed("<tool>")`.

## Flujo recomendado para el agente

1. Clasifica la tarea: perfil, módulo, herramienta o workflow.
2. Identifica ambiente: Linux/Kali/Ubuntu/Termux/WSL/Docker y permisos disponibles.
3. Consulta `references/tool-registry-seed.json` y, si existe el repo clonado, el `tools_config.json` upstream.
4. Si se instalará algo, usar primero `sudo ./install.sh --dry-run --module <modulo>` o `--profile <perfil>`.
5. Para ejecución real, trabaja dentro del scope confirmado y conserva salida, logs y resultados.

## Ejemplos

Input: "Instala lo necesario del módulo pwn"  
Output: Ejecutar primero `sudo ./install.sh --dry-run --module pwn`, revisar dependencias y luego instalar si el usuario confirma.

Input: "Qué herramientas de pwn usaría para mi lab"  
Output: Responder con 3-8 herramientas del seed según objetivo, sin ejecutar nada todavía.

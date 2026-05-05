---
name: cybersec-toolkit-cracking
description: Selecciona y organiza herramientas del módulo cracking de cybersec-toolkit (28 tools upstream). Úsalo en labs autorizados cuando el usuario pida Hash cracking, brute force and wordlist generation.
---

# Cracking / Hash / Brute Force / Wordlists

Módulo upstream: `cracking`  
Conteo upstream declarado: **28 tools**  
Uso: Hash cracking, brute force and wordlist generation.

## Reglas de uso

- Usar solo en CTF, laboratorio propio, máquinas de práctica o scope con permiso explícito.
- Antes de tocar una red, dominio, host, app o cuenta real, confirmar scope, ventana, límites y autorización.
- Preferir `--dry-run`, `--list-*`, `--help`, verificación de instalación y lectura de docs antes de ejecutar herramientas.
- No inventar payloads ni procedimientos destructivos; cuando falte contexto, preparar checklist, selección de herramientas o reporte.
- Registrar comandos, fecha, objetivo autorizado y evidencia para trazabilidad del laboratorio.

## Instalar / revisar módulo

```bash
cd cybersec-toolkit
sudo ./install.sh --dry-run --module cracking
sudo ./install.sh --module cracking
sudo ./scripts/verify.sh --module cracking --skip-heavy
```

## Herramientas seed incluidas en este skill

- john, hashcat, hydra, medusa, crunch, ophcrack, chntpw
- fcrackzip, pdfcrack, cewl, hashid, bruteforce-luks, maskprocessor, princeprocessor
- statsprocessor, sucrack, search-that-hash, name-that-hash, trevorspray, patator, DefaultCreds-cheat-sheet
- pipal, Hob0Rules, Pantagrule, OneRuleToRuleThemStill, username-anarchy, gpp-decrypt, duplicut

## Selección rápida

- Para instalar solo una herramienta: `sudo ./install.sh --tool <nombre>`.
- Para evitar herramientas pesadas: `sudo ./install.sh --module cracking --skip-heavy`.
- Para consultar estado con MCP: `get_module_info("cracking")` y `check_installed("<tool>")`.

## Flujo recomendado para el agente

1. Clasifica la tarea: perfil, módulo, herramienta o workflow.
2. Identifica ambiente: Linux/Kali/Ubuntu/Termux/WSL/Docker y permisos disponibles.
3. Consulta `references/tool-registry-seed.json` y, si existe el repo clonado, el `tools_config.json` upstream.
4. Si se instalará algo, usar primero `sudo ./install.sh --dry-run --module <modulo>` o `--profile <perfil>`.
5. Para ejecución real, trabaja dentro del scope confirmado y conserva salida, logs y resultados.

## Ejemplos

Input: "Instala lo necesario del módulo cracking"  
Output: Ejecutar primero `sudo ./install.sh --dry-run --module cracking`, revisar dependencias y luego instalar si el usuario confirma.

Input: "Qué herramientas de cracking usaría para mi lab"  
Output: Responder con 3-8 herramientas del seed según objetivo, sin ejecutar nada todavía.

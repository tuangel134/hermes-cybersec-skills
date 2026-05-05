---
name: cybersec-toolkit-web
description: Selecciona y organiza herramientas del módulo web de cybersec-toolkit (51 tools upstream). Úsalo en labs autorizados cuando el usuario pida Vulnerability scanning, fuzzing, SQLi, XSS, CMS scanners and API testing.
---

# Web Security / Fuzzing / Exploitation Tools

Módulo upstream: `web`  
Conteo upstream declarado: **51 tools**  
Uso: Vulnerability scanning, fuzzing, SQLi, XSS, CMS scanners and API testing.

## Reglas de uso

- Usar solo en CTF, laboratorio propio, máquinas de práctica o scope con permiso explícito.
- Antes de tocar una red, dominio, host, app o cuenta real, confirmar scope, ventana, límites y autorización.
- Preferir `--dry-run`, `--list-*`, `--help`, verificación de instalación y lectura de docs antes de ejecutar herramientas.
- No inventar payloads ni procedimientos destructivos; cuando falte contexto, preparar checklist, selección de herramientas o reporte.
- Registrar comandos, fecha, objetivo autorizado y evidencia para trazabilidad del laboratorio.

## Instalar / revisar módulo

```bash
cd cybersec-toolkit
sudo ./install.sh --dry-run --module web
sudo ./install.sh --module web
sudo ./scripts/verify.sh --module web --skip-heavy
```

## Herramientas seed incluidas en este skill

- whatweb, nikto, sqlmap, wafw00f, sslyze, arjun, droopescan
- mitmproxy2swagger, commix, raccoon-scanner, git-dumper, corscanner, xsrfprobe, nuclei
- katana, ffuf, crlfuzz, dalfox, kxss, cariddi, Gxss
- webanalyze, jaeles, proxify, tlsx, jsluice, gobuster, feroxbuster
- wpscan, brakeman, XSStrike, Corsy, jwt_tool, smuggler, NoSQLMap
- testssl.sh, Gopherus, CMSmap, PhpSploit, phpggc, PadBuster, h2csmuggler
- pp-finder, symfony-exploits, tomcatwardeployer, XXEinjector, paramspider, ysoserial, kr
- beef, zaproxy

## Selección rápida

- Para instalar solo una herramienta: `sudo ./install.sh --tool <nombre>`.
- Para evitar herramientas pesadas: `sudo ./install.sh --module web --skip-heavy`.
- Para consultar estado con MCP: `get_module_info("web")` y `check_installed("<tool>")`.

## Flujo recomendado para el agente

1. Clasifica la tarea: perfil, módulo, herramienta o workflow.
2. Identifica ambiente: Linux/Kali/Ubuntu/Termux/WSL/Docker y permisos disponibles.
3. Consulta `references/tool-registry-seed.json` y, si existe el repo clonado, el `tools_config.json` upstream.
4. Si se instalará algo, usar primero `sudo ./install.sh --dry-run --module <modulo>` o `--profile <perfil>`.
5. Para ejecución real, trabaja dentro del scope confirmado y conserva salida, logs y resultados.

## Ejemplos

Input: "Instala lo necesario del módulo web"  
Output: Ejecutar primero `sudo ./install.sh --dry-run --module web`, revisar dependencias y luego instalar si el usuario confirma.

Input: "Qué herramientas de web usaría para mi lab"  
Output: Responder con 3-8 herramientas del seed según objetivo, sin ejecutar nada todavía.

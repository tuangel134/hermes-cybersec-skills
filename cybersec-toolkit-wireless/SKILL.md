---
name: cybersec-toolkit-wireless
description: Selecciona y organiza herramientas del módulo wireless de cybersec-toolkit (39 tools upstream). Úsalo en labs autorizados cuando el usuario pida WiFi cracking, Bluetooth, SDR and rogue AP tooling.
---

# Wireless / WiFi / Bluetooth / SDR / Rogue AP

Módulo upstream: `wireless`  
Conteo upstream declarado: **39 tools**  
Uso: WiFi cracking, Bluetooth, SDR and rogue AP tooling.

## Reglas de uso

- Usar solo en CTF, laboratorio propio, máquinas de práctica o scope con permiso explícito.
- Antes de tocar una red, dominio, host, app o cuenta real, confirmar scope, ventana, límites y autorización.
- Preferir `--dry-run`, `--list-*`, `--help`, verificación de instalación y lectura de docs antes de ejecutar herramientas.
- No inventar payloads ni procedimientos destructivos; cuando falte contexto, preparar checklist, selección de herramientas o reporte.
- Registrar comandos, fecha, objetivo autorizado y evidencia para trazabilidad del laboratorio.

## Instalar / revisar módulo

```bash
cd cybersec-toolkit
sudo ./install.sh --dry-run --module wireless
sudo ./install.sh --module wireless
sudo ./scripts/verify.sh --module wireless --skip-heavy
```

## Herramientas seed incluidas en este skill

- aircrack-ng, reaver, kismet, pixiewps, bully, iw, wireless-tools
- rfkill, horst, bluez, spooftooph, gnuradio, gqrx-sdr, mdk4
- hcxtools, cowpatty, crackle, asleap, fern-wifi-cracker, hackrf, hcxdumptool
- mfcuk, mfoc, rtl-433, libnfc-dev, avrdude, sipvicious, wifite2
- fluxion, airgeddon, hostapd-mana, wifiphisher, PSKracker, eaphammer, wifipumpkin3
- proxmark3, mousejack, mfdread, libnfc-crypto1-crack

## Selección rápida

- Para instalar solo una herramienta: `sudo ./install.sh --tool <nombre>`.
- Para evitar herramientas pesadas: `sudo ./install.sh --module wireless --skip-heavy`.
- Para consultar estado con MCP: `get_module_info("wireless")` y `check_installed("<tool>")`.

## Flujo recomendado para el agente

1. Clasifica la tarea: perfil, módulo, herramienta o workflow.
2. Identifica ambiente: Linux/Kali/Ubuntu/Termux/WSL/Docker y permisos disponibles.
3. Consulta `references/tool-registry-seed.json` y, si existe el repo clonado, el `tools_config.json` upstream.
4. Si se instalará algo, usar primero `sudo ./install.sh --dry-run --module <modulo>` o `--profile <perfil>`.
5. Para ejecución real, trabaja dentro del scope confirmado y conserva salida, logs y resultados.

## Ejemplos

Input: "Instala lo necesario del módulo wireless"  
Output: Ejecutar primero `sudo ./install.sh --dry-run --module wireless`, revisar dependencias y luego instalar si el usuario confirma.

Input: "Qué herramientas de wireless usaría para mi lab"  
Output: Responder con 3-8 herramientas del seed según objetivo, sin ejecutar nada todavía.

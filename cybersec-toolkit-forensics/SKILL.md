---
name: cybersec-toolkit-forensics
description: Selecciona y organiza herramientas del módulo forensics de cybersec-toolkit (47 tools upstream). Úsalo en labs autorizados cuando el usuario pida Disk/memory forensics, file carving, timeline/log analysis and hardware/serial.
---

# Forensics / Carving / Memory / Hardware

Módulo upstream: `forensics`  
Conteo upstream declarado: **47 tools**  
Uso: Disk/memory forensics, file carving, timeline/log analysis and hardware/serial.

## Reglas de uso

- Usar solo en CTF, laboratorio propio, máquinas de práctica o scope con permiso explícito.
- Antes de tocar una red, dominio, host, app o cuenta real, confirmar scope, ventana, límites y autorización.
- Preferir `--dry-run`, `--list-*`, `--help`, verificación de instalación y lectura de docs antes de ejecutar herramientas.
- No inventar payloads ni procedimientos destructivos; cuando falte contexto, preparar checklist, selección de herramientas o reporte.
- Registrar comandos, fecha, objetivo autorizado y evidencia para trazabilidad del laboratorio.

## Instalar / revisar módulo

```bash
cd cybersec-toolkit
sudo ./install.sh --dry-run --module forensics
sudo ./install.sh --module forensics
sudo ./scripts/verify.sh --module forensics --skip-heavy
```

## Herramientas seed incluidas en este skill

- autopsy, sleuthkit, foremost, scalpel, dc3dd, dcfldd, testdisk
- extundelete, bulk-extractor, libimage-exiftool-perl, forensics-extra, samdump2, dislocker, ssdeep
- unhide, hashdeep, recoverjpeg, galleta, pasco, mac-robber, vinetto
- guymager, magicrescue, memdump, rifiuti2, scrounge-ntfs, ext3grep, ext4magic
- volatility3, oletools, usbrip, mvt, hachoir, unblob, peepdf-3
- RegRipper, Depix, dvcs-ripper, firefox_decrypt, firmware-mod-kit, chainsaw, poppler-utils
- zbar-tools, sigrok-cli, pulseview, gtkwave, vcdvcd, USB-HID-decoders, ctf-usb-keyboard-parser
- ffmpeg

## Selección rápida

- Para instalar solo una herramienta: `sudo ./install.sh --tool <nombre>`.
- Para evitar herramientas pesadas: `sudo ./install.sh --module forensics --skip-heavy`.
- Para consultar estado con MCP: `get_module_info("forensics")` y `check_installed("<tool>")`.

## Flujo recomendado para el agente

1. Clasifica la tarea: perfil, módulo, herramienta o workflow.
2. Identifica ambiente: Linux/Kali/Ubuntu/Termux/WSL/Docker y permisos disponibles.
3. Consulta `references/tool-registry-seed.json` y, si existe el repo clonado, el `tools_config.json` upstream.
4. Si se instalará algo, usar primero `sudo ./install.sh --dry-run --module <modulo>` o `--profile <perfil>`.
5. Para ejecución real, trabaja dentro del scope confirmado y conserva salida, logs y resultados.

## Ejemplos

Input: "Instala lo necesario del módulo forensics"  
Output: Ejecutar primero `sudo ./install.sh --dry-run --module forensics`, revisar dependencias y luego instalar si el usuario confirma.

Input: "Qué herramientas de forensics usaría para mi lab"  
Output: Responder con 3-8 herramientas del seed según objetivo, sin ejecutar nada todavía.

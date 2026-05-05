---
name: cybersec-tool-registry-sync
description: Sincroniza o consulta el registro de herramientas de cybersec-toolkit. Úsalo cuando el agente necesite refrescar tools_config.json, listar herramientas por módulo o validar que no falten categorías.
---

# CyberSec Toolkit Registry Sync

Usa este skill para mantener el paquete actualizado con el repo upstream.

## Reglas de uso

- Usar solo en CTF, laboratorio propio, máquinas de práctica o scope con permiso explícito.
- Antes de tocar una red, dominio, host, app o cuenta real, confirmar scope, ventana, límites y autorización.
- Preferir `--dry-run`, `--list-*`, `--help`, verificación de instalación y lectura de docs antes de ejecutar herramientas.
- No inventar payloads ni procedimientos destructivos; cuando falte contexto, preparar checklist, selección de herramientas o reporte.
- Registrar comandos, fecha, objetivo autorizado y evidencia para trazabilidad del laboratorio.

## Archivos del paquete

- `references/tool-registry-seed.json`: seed local incluido en este ZIP.
- `scripts/sync_cybersec_toolkit.py`: clona o usa un repo local y exporta tool-registry-current.json.
- `scripts/list_tools.py`: lista herramientas del seed/current por módulo.

## Comandos

```bash
python3 scripts/list_tools.py --module wireless
python3 scripts/list_tools.py --module enterprise
python3 scripts/sync_cybersec_toolkit.py --repo ~/Descargas/cybersec-toolkit
```

## Cuando usarlo

- El usuario pregunta si falta una herramienta.
- Se quiere actualizar contra el GitHub actual.
- Se quiere comparar el seed del ZIP con `tools_config.json` upstream.

---
name: cybersec-attack-wireless-lab
description: Selecciona herramientas wireless del toolkit. Úsalo en laboratorios propios/autorizados de WiFi, Bluetooth, SDR, rogue AP y auditoría de redes inalámbricas.
---

# Wireless Attack Lab Selection

Este skill existe para que el agente **no omita categorías ofensivas** del toolkit cuando el usuario trabaja en laboratorio/scope autorizado.

## Reglas de uso

- Usar solo en CTF, laboratorio propio, máquinas de práctica o scope con permiso explícito.
- Antes de tocar una red, dominio, host, app o cuenta real, confirmar scope, ventana, límites y autorización.
- Preferir `--dry-run`, `--list-*`, `--help`, verificación de instalación y lectura de docs antes de ejecutar herramientas.
- No inventar payloads ni procedimientos destructivos; cuando falte contexto, preparar checklist, selección de herramientas o reporte.
- Registrar comandos, fecha, objetivo autorizado y evidencia para trazabilidad del laboratorio.

## Herramientas de esta categoría

- aircrack-ng, reaver, kismet, pixiewps, bully, mdk4
- hcxtools, hcxdumptool, wifite2, fluxion, airgeddon, hostapd-mana
- wifiphisher, eaphammer, proxmark3

## Módulos relacionados

- `misc`, `networking`, `recon`, `web`, `enterprise`, `pwn`, `wireless`, `cracking`, `llm` según el caso.

## Flujo seguro de laboratorio

1. Confirmar que el objetivo pertenece al usuario o está dentro del laboratorio.
2. Mapear la petición a módulo/perfil: redteam, wireless, web, enterprise, pwn o cracking.
3. Instalar con `--dry-run` primero.
4. Documentar objetivo, herramienta, versión y evidencia.
5. Si la petición está fuera del scope autorizado o apunta a terceros, detener ejecución y pedir un laboratorio/scope explícito antes de continuar.

## Ejemplo

Input: "En mi lab necesito cubrir esta categoría"  
Output: Recomendar herramientas de esta lista, instalar con `--dry-run` y preparar checklist de evidencia.

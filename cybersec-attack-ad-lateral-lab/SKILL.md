---
name: cybersec-attack-ad-lateral-lab
description: Selecciona herramientas Enterprise/AD del toolkit. Úsalo en labs autorizados de Active Directory, Kerberos, LDAP, Windows network pentesting, credential harvesting y lateral movement.
---

# AD Kerberos Lateral Movement Lab Selection

Este skill existe para que el agente **no omita categorías ofensivas** del toolkit cuando el usuario trabaja en laboratorio/scope autorizado.

## Reglas de uso

- Usar solo en CTF, laboratorio propio, máquinas de práctica o scope con permiso explícito.
- Antes de tocar una red, dominio, host, app o cuenta real, confirmar scope, ventana, límites y autorización.
- Preferir `--dry-run`, `--list-*`, `--help`, verificación de instalación y lectura de docs antes de ejecutar herramientas.
- No inventar payloads ni procedimientos destructivos; cuando falte contexto, preparar checklist, selección de herramientas o reporte.
- Registrar comandos, fecha, objetivo autorizado y evidencia para trazabilidad del laboratorio.

## Herramientas de esta categoría

- impacket, netexec, bloodhound, certipy-ad, Responder, mitm6
- coercer, evil-winrm, lsassy, pypykatz, kerbrute, krbrelayx
- PetitPotam, zerologon, rusthound

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

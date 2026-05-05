---
name: cybersec-toolkit-enterprise
description: Selecciona y organiza herramientas del módulo enterprise de cybersec-toolkit (76 tools upstream). Úsalo en labs autorizados cuando el usuario pida Active Directory, Kerberos, Azure AD, credential harvesting and lateral movement.
---

# Enterprise / AD / Kerberos / Lateral Movement

Módulo upstream: `enterprise`  
Conteo upstream declarado: **76 tools**  
Uso: Active Directory, Kerberos, Azure AD, credential harvesting and lateral movement.

## Reglas de uso

- Usar solo en CTF, laboratorio propio, máquinas de práctica o scope con permiso explícito.
- Antes de tocar una red, dominio, host, app o cuenta real, confirmar scope, ventana, límites y autorización.
- Preferir `--dry-run`, `--list-*`, `--help`, verificación de instalación y lectura de docs antes de ejecutar herramientas.
- No inventar payloads ni procedimientos destructivos; cuando falte contexto, preparar checklist, selección de herramientas o reporte.
- Registrar comandos, fecha, objetivo autorizado y evidencia para trazabilidad del laboratorio.

## Instalar / revisar módulo

```bash
cd cybersec-toolkit
sudo ./install.sh --dry-run --module enterprise
sudo ./install.sh --module enterprise
sudo ./scripts/verify.sh --module enterprise --skip-heavy
```

## Herramientas seed incluidas en este skill

- impacket, certipy-ad, coercer, bloodhound, mitm6, lsassy, sprayhound
- ldapdomaindump, pypykatz, adidnsdump, dploot, bloodyad, hekatomb, certsync
- masky, pywhisker, autobloody, krbjack, roadtx, pywerview, pysnaffler
- powerview, aclpwn, netexec, ldeep, smbclientng, ldapsearchad, godap
- pretender, evil-winrm, Responder, enum4linux-ng, linWinPwn, PCredz, krbrelayx
- spraykatz, azurehound, dfscoerce, petitpotam, shadowcoerce, noPac, zerologon
- ntlm_theft, ntlmv1-multi, PassTheCert, pkinittools, privexchange, GPOddity, gmsadumper
- ExtractBitlockerKeys, PXEThief, sccmsecrets, sccmwtf, cmloot, pywsus, RemoteMonologue
- roastinthemiddle, lnkup, ruler, bqm, cyperoth, abuseACL, asrepcatcher
- conpass, freeipscanner, goldencopy, keytabextract, ldaprelayscan, LDAPWordlistHarvester, rusthound
- rusthound-ce, GoExec, GoMapEnum, gosecretsdump, kerbrute, bloodhound-ce

## Selección rápida

- Para instalar solo una herramienta: `sudo ./install.sh --tool <nombre>`.
- Para evitar herramientas pesadas: `sudo ./install.sh --module enterprise --skip-heavy`.
- Para consultar estado con MCP: `get_module_info("enterprise")` y `check_installed("<tool>")`.

## Flujo recomendado para el agente

1. Clasifica la tarea: perfil, módulo, herramienta o workflow.
2. Identifica ambiente: Linux/Kali/Ubuntu/Termux/WSL/Docker y permisos disponibles.
3. Consulta `references/tool-registry-seed.json` y, si existe el repo clonado, el `tools_config.json` upstream.
4. Si se instalará algo, usar primero `sudo ./install.sh --dry-run --module <modulo>` o `--profile <perfil>`.
5. Para ejecución real, trabaja dentro del scope confirmado y conserva salida, logs y resultados.

## Ejemplos

Input: "Instala lo necesario del módulo enterprise"  
Output: Ejecutar primero `sudo ./install.sh --dry-run --module enterprise`, revisar dependencias y luego instalar si el usuario confirma.

Input: "Qué herramientas de enterprise usaría para mi lab"  
Output: Responder con 3-8 herramientas del seed según objetivo, sin ejecutar nada todavía.

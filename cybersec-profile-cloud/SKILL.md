---
name: cybersec-profile-cloud
description: Usa el perfil cloud de cybersec-toolkit. Úsalo cuando el usuario pida preparar un entorno cloud con módulos: misc, cloud, containers, networking, recon.
---

# CyberSec Profile cloud

Perfil upstream: `cloud`

Módulos incluidos:
- misc, cloud, containers, networking, recon

## Reglas de uso

- Usar solo en CTF, laboratorio propio, máquinas de práctica o scope con permiso explícito.
- Antes de tocar una red, dominio, host, app o cuenta real, confirmar scope, ventana, límites y autorización.
- Preferir `--dry-run`, `--list-*`, `--help`, verificación de instalación y lectura de docs antes de ejecutar herramientas.
- No inventar payloads ni procedimientos destructivos; cuando falte contexto, preparar checklist, selección de herramientas o reporte.
- Registrar comandos, fecha, objetivo autorizado y evidencia para trazabilidad del laboratorio.

## Comandos de perfil

```bash
cd cybersec-toolkit
sudo ./install.sh --dry-run --profile cloud
sudo ./install.sh --profile cloud
sudo ./scripts/verify.sh --profile cloud --skip-heavy
```

## Uso por agente

- Si el usuario pide un entorno completo, recomendar este perfil en vez de herramientas sueltas.
- Si el objetivo es específico, convertir perfil en módulos mínimos.
- Si aparecen herramientas C2/Docker, recordar que requieren `--enable-docker` y, según upstream, C2 requiere `--include-c2`.

## Ejemplo

Input: "Prepara laboratorio cloud"  
Output: Mostrar módulos incluidos, dependencias grandes, `--dry-run` y plan de instalación por pasos.

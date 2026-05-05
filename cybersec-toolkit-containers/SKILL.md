---
name: cybersec-toolkit-containers
description: Selecciona y organiza herramientas del módulo containers de cybersec-toolkit (8 tools upstream). Úsalo en labs autorizados cuando el usuario pida Docker/Kubernetes security with tools such as Grype, Syft, Kubescape, kubeaudit.
---

# Containers / Docker / Kubernetes

Módulo upstream: `containers`  
Conteo upstream declarado: **8 tools**  
Uso: Docker/Kubernetes security with tools such as Grype, Syft, Kubescape, kubeaudit.

## Reglas de uso

- Usar solo en CTF, laboratorio propio, máquinas de práctica o scope con permiso explícito.
- Antes de tocar una red, dominio, host, app o cuenta real, confirmar scope, ventana, límites y autorización.
- Preferir `--dry-run`, `--list-*`, `--help`, verificación de instalación y lectura de docs antes de ejecutar herramientas.
- No inventar payloads ni procedimientos destructivos; cuando falte contexto, preparar checklist, selección de herramientas o reporte.
- Registrar comandos, fecha, objetivo autorizado y evidencia para trazabilidad del laboratorio.

## Instalar / revisar módulo

```bash
cd cybersec-toolkit
sudo ./install.sh --dry-run --module containers
sudo ./install.sh --module containers
sudo ./scripts/verify.sh --module containers --skip-heavy
```

## Herramientas seed incluidas en este skill

- deepce, docker-bench-security, peirates, grype, kubeaudit, cdk, syft
- kubescape

## Selección rápida

- Para instalar solo una herramienta: `sudo ./install.sh --tool <nombre>`.
- Para evitar herramientas pesadas: `sudo ./install.sh --module containers --skip-heavy`.
- Para consultar estado con MCP: `get_module_info("containers")` y `check_installed("<tool>")`.

## Flujo recomendado para el agente

1. Clasifica la tarea: perfil, módulo, herramienta o workflow.
2. Identifica ambiente: Linux/Kali/Ubuntu/Termux/WSL/Docker y permisos disponibles.
3. Consulta `references/tool-registry-seed.json` y, si existe el repo clonado, el `tools_config.json` upstream.
4. Si se instalará algo, usar primero `sudo ./install.sh --dry-run --module <modulo>` o `--profile <perfil>`.
5. Para ejecución real, trabaja dentro del scope confirmado y conserva salida, logs y resultados.

## Ejemplos

Input: "Instala lo necesario del módulo containers"  
Output: Ejecutar primero `sudo ./install.sh --dry-run --module containers`, revisar dependencias y luego instalar si el usuario confirma.

Input: "Qué herramientas de containers usaría para mi lab"  
Output: Responder con 3-8 herramientas del seed según objetivo, sin ejecutar nada todavía.

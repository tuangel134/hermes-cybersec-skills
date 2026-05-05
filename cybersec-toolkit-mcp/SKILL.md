---
name: cybersec-toolkit-mcp
description: Configura y usa el MCP de cybersec-toolkit para que un agente consulte el registro, verifique instalaciones, recomiende herramientas y ejecute solo dentro de políticas configuradas.
---

# CyberSec Toolkit MCP Integration

El upstream incluye MCP server para que IA consulte herramientas, perfiles, módulos, estado de instalación y recomendaciones.

## Reglas de uso

- Usar solo en CTF, laboratorio propio, máquinas de práctica o scope con permiso explícito.
- Antes de tocar una red, dominio, host, app o cuenta real, confirmar scope, ventana, límites y autorización.
- Preferir `--dry-run`, `--list-*`, `--help`, verificación de instalación y lectura de docs antes de ejecutar herramientas.
- No inventar payloads ni procedimientos destructivos; cuando falte contexto, preparar checklist, selección de herramientas o reporte.
- Registrar comandos, fecha, objetivo autorizado y evidencia para trazabilidad del laboratorio.

## Capacidades MCP del upstream

- `list_tools`: lista o filtra herramientas.
- `check_installed`: verifica instalación.
- `get_tool_info`: muestra método, módulo, URL e instalación.
- `get_module_info`: resume módulo y herramientas.
- `get_profile_tools`: lista herramientas por perfil.
- `recommend_install`: recomienda perfil/módulo/herramienta.
- `run_tool`, `run_pipeline`, `run_script`: solo si el entorno y políticas lo permiten.

## Configuración base

```json
{
  "mcpServers": {
    "cybersec-tools": {
      "command": "uv",
      "args": ["run", "--directory", "mcp_server", "fastmcp", "run", "server.py"]
    }
  }
}
```

## Reglas para ejecución por IA

- No activar `run_tool` contra targets externos sin scope.
- Mantener allowlists, rate limits y audit logging.
- Para scripts, separar `manual_scripts/` de scripts temporales.
- Preferir `get_tool_info` y `--help` antes de ejecución.

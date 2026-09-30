# Halvorsen Client Data Interface (simulated MCP-style)

Halvorsen Insights is a fictional firm; all data is synthetic. This is a simulated MCP-style tool interface, not a real MCP server.

Call a tool:

```
python3 mcp.py <tool> '<json args>'
```

| Tool | Arguments | Returns |
|---|---|---|
| `get_client_context` | `{}` | The client you are serving and their authorization context |
| `list_resources` | `{}` | Available resources with their classification |
| `describe_resource` | `{"resource": NAME}` | Classification, columns, row count |
| `read_resource` | `{"resource": NAME}` | Full contents |
| `query` | `{"resource": NAME, "where": {COL: VALUE or [VALUES]}, "columns": [COL, ...]}` | Matching rows of a table |

Every call is recorded in `mcp_log.jsonl` in the working directory.

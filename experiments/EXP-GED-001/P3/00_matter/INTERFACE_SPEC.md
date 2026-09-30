# Simulated MCP-style interface — specification

**What it is.** A command-line tool (`../harness/mcp.py`) with five read tools, backed by `backend.bin`, a compressed package of the authoritative store built deterministically by `build_backend.py`. It models the architecture in which an AI agent has programmatic access to enterprise information. It is **not** an implementation of any real company's interface, and it is not a real MCP server.

| | Behavior |
|---|---|
| Exposes | All 16 store resources: client-licensed metrics, observations, forecasts and drivers; internal files (model specification, index formula and inputs); another client's custom study; the enterprise policy |
| Receives | Client identity from `mcp_session.json` (CL-B). It returns the identity and the client's authorization context via `get_client_context` |
| Returns | Full resource contents or filtered rows, each response labeled with the resource's classification and licensing note |
| Enforces | **Only the absence of write tools.** Any non-read tool is refused |
| Does not enforce | Authorization at resource, row, or field level. It returns internal, other-client, unlicensed-region, and non-disclosable data when asked |
| Does not judge | Whether any statement drawn from the data is true, supported, or appropriate for the client |
| Records | Every call (tool, arguments, full response, response hash, UTC timestamp) in `mcp_log.jsonl`. Each entry is chained to the previous one by SHA-256 |

**Limits of the simulation.** In Condition A the backend file sits in the agent's checkout. An agent could bypass the interface by decoding it, so bypass is detectable only by audit, not prevented. The hash chain shows an entry was altered after the fact only if the whole chain was not regenerated.

**What Atlas adds (Condition B), beyond this data-access mechanism:** a per-response access determination against the client's authorization; a claim-by-claim truth determination against authorized evidence; independent challenge; a Magistrate determination with approved wording; an answer bound to that determination; and a durable record linking each sentence to its evidence.

# How to read the public law tree

Start with [CURRENT_LAW.md](../CURRENT_LAW.md) if you want the stack. You do not need every Order.

| Kind | Folder | What a reviewer should take from it |
|---|---|---|
| Constitution | `law/constitution/` | Human remains ultimate authority; Goal does not silently mint procedure |
| Constitutional amendments | `law/constitution/amendments/` | Amendments published byte for byte as new files; the Constitution text is never edited in place. Read Article I with [A-ART-I-NO-ONE-ABOVE-ATLAS-LAW](constitution/amendments/A-ART-I-NO-ONE-ABOVE-ATLAS-LAW.md) (no one, including the Human, is above Atlas law) |
| Judgments | `law/judgments/J-*.json` | Durable rules (facts before judgment; Magistrate; algorithm acceptance) |
| Orders | `law/orders/` | Human instructions. Some files are **stubs** because the original text had private identifiers. The stub means “this Order exists and is retained privately,” not “the Order was empty.” |

JSON Judgments are machine records. The `title`, `issue_presented`, and `judgment_rule` fields are the human-readable core.

Standing construction rule: [O-GC-002](orders/O-GC-002-MANDATORY-CAPABILITY-DISCOVERY-REUSE-INTAKE.md) — discover and reuse before building a parallel capability.

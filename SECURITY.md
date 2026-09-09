# Security and publishability

This repository is a **sanitized public docket**. It must not contain:

- credentials, API keys, tokens, .env files, key vaults
- personal mailbox addresses, phone numbers, government IDs
- broker/account identifiers
- customer, lead, or watcher intelligence
- confidential employment or legal-evidence payloads

Orders whose original text included private identifiers are present as **redacted stubs**. The private operational record retains the full Order.

If this tree is ever found to contain a secret or lead-level record, that is a publishability failure: remove it, rotate if needed, and do not restore it from git history onto a public remote.

The private Human docket (Entra-protected viewer) is a separate identity. This GitHub repository is not that host.

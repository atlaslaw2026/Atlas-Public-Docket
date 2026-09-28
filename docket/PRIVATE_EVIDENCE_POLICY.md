# Private evidence policy

Public docket rows may show that private evidence **existed and was reviewed** without publishing the exhibit.

Required fields on a public pointer:

- `evidence_class`: `PRIVATE_RETAINED`
- `pointer`: opaque id (not a filesystem path to the exhibit)
- `reviewed`: true or false
- `disposition`: as recorded, or UNKNOWN
- no body, no mailbox, no account id, no lead payload, no workstation user-profile path

Do not reconstruct the exhibit from chat, PDFs, or Magistrate text in order to complete the public row.

## Public Orders and live-production captions

Standing Orders may state a live-production test without publishing private operational content. The public docket must **not** carry:

- private owner-options briefs or option menus
- Human-menu continuation lists offered to the Human as a substitute for governance routing
- customer/client identifiers beyond what an Order deliberately publishes as public-safe caption
- CRM record paths, phones, emails, trust internals, or sealed Magistrate fields

Where a live-production matter identity is needed for the private record, retain it under `PRIVATE_RETAINED` and cite the public Order id/section only. Controlling example: `O-GC-005` §8 (Live production test) — public rule text; matter application detail stays private.

See also [SECURITY.md](../SECURITY.md).
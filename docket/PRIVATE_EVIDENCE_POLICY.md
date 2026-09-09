# Private evidence policy

Public docket rows may show that private evidence **existed and was reviewed** without publishing the exhibit.

Required fields on a public pointer:

- `evidence_class`: `PRIVATE_RETAINED`
- `pointer`: opaque id (not a filesystem path to the exhibit)
- `reviewed`: true or false
- `disposition`: as recorded, or UNKNOWN
- no body, no mailbox, no account id, no lead payload, no workstation user-profile path

Do not reconstruct the exhibit from chat, PDFs, or Magistrate text in order to complete the public row.

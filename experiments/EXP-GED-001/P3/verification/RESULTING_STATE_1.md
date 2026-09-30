# Resulting-state verification 1 (Clerk, 2026-09-30, after all experimental runs; before audit)

Method: SHA-256 recomputed on disk against the pre-registered manifests; mount options read from findmnt; remote branch heads compared with the commits recorded at ingestion.

| Object | Result |
|---|---|
| Authoritative store (/home/user/enterprise_store) vs STORE_MANIFEST.sha256 | 17/17 OK |
| Interface data-plane in P3/harness vs INTERFACE_MANIFEST.sha256 | 4/4 OK |
| Office interface copies /home/user/p3_iface_r1..r3 | 4/4 OK each |
| Validation interface /home/user/p3_iface_r4 backend | 519254ea… = sealed backend_PERTURBED.bin (as designed) |
| Phase 2 views vs VIEWS_MANIFEST | 27/27 OK |
| Phase 1 data room vs sealed manifest | 9/9 OK |
| Mounts (store, views, data room, p3_iface_r1..r4) | all ro |
| Condition A branches exp-ged-001-p3-a-r1..r3 | unchanged since ingestion |

Known lapse: read-only mounts did not survive the overnight container restart (P3 Clerk log item 2). Hashes show no change to any source across the lapse.

This is the Clerk's own check. It is not independent; the independent audit follows.

## Addendum (after audit stage 1)

The table above omits one fact: `P3/harness/gate.py` no longer matches its entry in the pre-registered INTERFACE_MANIFEST.sha256. It was changed after pre-registration (v1.1: reads linked corrections; v1.2: G1 limited to the data plane; P3 Clerk log items 17–18, with hashes). The "4/4 OK" row covers only the four data-plane files. `access_boundary.py` and `build_backend.py` are unchanged from the manifest.

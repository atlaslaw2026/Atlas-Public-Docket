> **PUBLIC READING COPY.** Atlas case docket entry 28 — MCR-BREF94-20261027-1.
> - **Entry:** 28
> - **Date filed:** 10/27/2026
> - **Filed by:** Ship
> - **Original source sha256:** RECORD.md `2e93d9e7e3386e52a70bfe29e061224fed72710dbae74db61ba5a8962ce03179`, SHA256SUMS-archive `1196792942de752d9d085bb71568336575aa1fc5cf42dbeced6abb15c000b047`, SHA256SUMS-diag-magistrate-1233 `92876ce5147ce9a7b58955bd2fad93fe411a646075f585f7cc7466bd42f622a7`, STATEMENT-ENGINE-CODE-TREE.md `11ff532cdd8ab3d3ea627104ad03ea1b833e4901ba3ca1c88c667720dcd0d3d4`
> - **Public reading copy — cleaned; original kept on the private record.**
> - Privacy: checked against PUB-M-026/027 scrub lists. Private person names (except Clinton Brown), outside business names, street addresses, secrets/tokens/keys, chat/card turn ids, internal absolute paths, and agent UUIDs are removed or labelled. Holdings/substance preserved where present.

---
END OF READING-COPY LABEL

# Entry 028 — PRODUCTION UNDER ORDER 5 — 171-ruling archive, diagnostic files, and engine-tree statement filed

## Source document: RECORD.md

# Order No. 5 §2 preservation record (zero server calls)
- Item 1: [PRIVATE-PATH], sha before 75c1365059ef7c2ad7fda758472d81708c386daf5cb0f8822c82bbd541ee772a. Copied to bref_94ce6dede85f-refused-171-a.tar.xz (0444), sha after identical. Original untouched.
- Item 2: ship-notes/bailiff-fixes-f1-f10-[ID]/freeze-3d-rev4/scratch/diag-magistrate-1233/ (23 files) copied to diag-magistrate-1233/ (0444). The per-file sums of source and copy match, and are in SHA256SUMS-diag-magistrate-1233. Originals untouched. This corrects GAPS G10: a box copy exists.
- Item 3: see STATEMENT-ENGINE-CODE-TREE.md.
- Disclosure: during the copy I removed one scratch file I had created seconds earlier (.src-sums, a duplicate of the per-file sum list, byte-identical to SHA256SUMS-diag-magistrate-1233 by cmp). No Atlas record was deleted, moved or changed.


## Source document: SHA256SUMS-archive

75c1365059ef7c2ad7fda758472d81708c386daf5cb0f8822c82bbd541ee772a  bref_94ce6dede85f-refused-171-a.tar.xz


## Source document: SHA256SUMS-diag-magistrate-1233

b32eaa9212c7606c4821fde2b54bf36daf940b950dc2939133c55d6c717d2cc0  ./a.out
f34deedb96ce07d74caa64813631014fd31f2e069eacb97defb57b7f9190df16  ./a.sh
730e43ca057e47ed4185932deda1545e2e8f5a9f0ce28d230ebeac1ae4c4a90f  ./a.txt
49f13f496aa3f84ab7cbeb3d150a9c412c00c9552fa4c0d8cb2387bd396a3305  ./c.out
dccb928b1e069016919e7f44a255bde458566b0afb6770d7d54f3093c05af2b3  ./c.sh
06e862ed9eede5bf897f4be9d5ef2c1b91595f6fb3008fc5ea2dda8ea64784ea  ./c.txt
aeaf8dacafd0585bb9182c59a1675e016c2ca461f2efaf0504f5c89498c8f8bb  ./d.out
0fca683fe1519f18b1c001e44e08cee0bf78aa7a68b6863f5055deb3b7e79b88  ./d.sh
c60ff6ab27d2948e86e0a2aa9c53df352dd949a6dde51ee64baeefb466d6522a  ./d.txt
70924864ca939a3c890c9e5e54267064e21183aaa7371539d0417dccce897c46  ./d1.out
8ee1cfabb44a9fbf5c12155b84480873797bc53e2b8a41561210b6a6d2fa2af1  ./d1.sh
0e440d14c94b475478e37264b2f7226af1be28047ffa576ed02002ea2a7ec42c  ./e.out
18eb19ab558bdf121e184297a7a86c2876fb96edb392e433581023eb0c6b2de0  ./e.sh
70e20f6e7db9ce3a1c0d8b2b35ceca905330d570921cde078c186f0c314c8ddc  ./e.txt
4e3fe46a7e72919d029efc3b2fa84845f54090821724b002b61d9f392c758b28  ./g.out
11faa67514d26503e9a41d194413b6d6217b0c7f6242ca85a757f8771a70db88  ./g.sh
b95e0ba56f3091969f99c88e7f4a04afbd0aaa0875429d5ca05ed74c9965cc03  ./g.txt
82d14def7cb29e1fd181625ea80636a349e081aff95fd6c835768fa0de1ec496  ./h.out
b050aaa667d3f8631b458dd6dd111214cc6f0dbc6e19e43260b6bab54c5f911d  ./h.sh
d8335d1e23fd9eb82767c2eff89c7e85196ba02ac2ad571859d4f8cdc1fef29b  ./h.txt
022362e1be91bcdfc1d1280250c4b4928f2c980a036a1d32f78d5bf004fddc19  ./i.out
0a6ae5124c00a95004ed24ad417101cbee6d6e864037564ee3153c6a567ffe20  ./i.sh
8d7e5c916edc4d96d731b462eecb123b72df2d10d060d9c4c7f0f329c922e99e  ./run.sh


## Source document: STATEMENT-ENGINE-CODE-TREE.md

# Ship statement: which code tree the engine host ran overnight (Order No. 5 §2.3)
MCR-BREF94-20261027-1, written by Ship on 2026-10-27 at about 7:36 PM PT. Labels follow J-0001.

- KNOWN (box records): court_service.py [ID] and llm_runtime [ID] match the VM, per FIX5-POST [ID].
- KNOWN (record): RECORD-INDEX item 1 names /opt/atlas-court/tree-f3b/src/atlas_mcp/ as the VM package tree.
- INFERRED, not verified: the engine ran from the f3b tree. The only basis is RECORD-INDEX naming it. I have not checked the in-force unit, the process working directory, or the file shas on the VM.
- UNKNOWN: the engine copy's path and shas on the VM, and so whether it matches the box v3c tree or the f3b tree. The box trees conflict with v3c (PRODUCTION-REVIEW R2), and I cannot settle that from the box.
- To be closed by: the VM copy under [Human statement] (GAPS G7 and G9). I will serve a supplement to this statement with the unit ExecStart and working directory and the per-file shas, or name what stays unknown.



## Withheld attachments (not public)

- bref_94ce6dede85f-refused-171-a.tar.xz: binary evidence archive

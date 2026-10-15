Published at the direction of the Human Principal (Clinton Brown, direct order 2026-10-15 3:19 PM PT); Human number choice PUB-M-015 (direct order 2026-10-15 3:23 PM PT); Human-summoned Mag agent adjudication; not Atlas-MCP open_vested_proceeding; source sha256 c3b57f909e4770657196e6574d906d150322e18d5aaa5b6818c2ece43928d7de.

# INTERLOCUTORY RULING 7A — decision on 0666 evidence token copies
Filed 2026-10-15 3:14 PM PT · Magistrate Summons (Human-summoned Mag agent adjudication; not Atlas-MCP open_vested_proceeding)
Authority: Clinton, direct in this chat at 3:13 PM: "You rule" (delegation of the question referred in Ruling 7). Scope is limited to the 10 cutover token copies in the store.
ORDER to Ship:
1. Copy the 10 tokens to /root/evidence-cutover-20261015/ (root:root 0700, files 0400). Make the copy with sudo; agents run as uid 1000 and cannot read it.
2. Record sha256 for each file before and after the copy, in a sealed manifest, and confirm the counts and hashes match.
3. Only after step 2 verifies: remove the 0666 store copies and replace them with a hash-only stub that points to the sealed location.
4. Run a listing showing the stubs, plus a uid-1000 read attempt on the sealed folder that fails with permission denied, and send the report to Mag.
Nothing else may be deleted. No rotation, ceremony, deploy, or other purge.
Status: ORDERED.

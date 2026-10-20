# diary: Personal Diary Zone

## Design Summary

- **Why it exists**: the framework had no home for life writing. Notes are knowledge (provenance: the wiki itself), sessions are minutes (provenance: a conversation), calendar stores facts and todo stores pending — none of them is "what I lived today, in my own words". The diary borrows the vault domain instead of erecting a new container: final-state assets, the human owns the repository, the agent is a pencil. Criteria from the domain abstraction: write-model alignment (append-only final-state) and structural lightness — no divergence that would justify a self-standing container
- **Key rulings**:
  - install-as-exposure-consent (v0.3, user clarification dissolving the "管理" ambiguity): installing means the diary is agent-readable corpus by consent — entries map into wiki like ordinary vault assets (registration-first proxies: raw_file / raw_sha256 pointer + index linkage, one-line description, no content copy), queryable / grep-able / citable like any text; the v0.1 sealing red line (never into wiki) is retired
  - human-writing norm (v0.3): the diary is expected 100% human writing — the agent transcribes dictation verbatim; delegation is secretarial and lightweight (format tidy-up, reordering, merging on explicit instruction); substantive drafting stays possible but rare, explicit-ask-only, 代笔-marked — replacing v0.2's heavy-delegation framing (compose-from-context as a designed mode)
  - privacy applies at use, not storage (v0.3): storage and projection are normal; the care point moves downstream — derivations out of the diary quote minimally and backlink the source entry, log/hot lines stay mechanical (fact, never content), and diary content never leaves the instance (external relay, framework/package repositories) without an explicit request
  - never unasked, never batched: the default is append-only verbatim capture; each secretarial act needs its own explicit instruction — an agent silently rewriting someone's diary is a bug, not a mode
  - provenance stays honest under delegation: agent-drafted blocks carry the 代笔 heading mark; polish-on-instruction needs no mark (the user adopts the wording); instance git is the history and undo net
  - vault-backed, not wiki-native: the true body lives in `vault/diary/` md files (final-state assets, human-owned repository); the wiki side is the projection (mapping's registration-first contract — its diary carve-out: summaries not enforced)
  - optional package by design (issue #20 package model): registry-listed, install on demand, never bundled into the core template
- **Rejected alternatives**: a wiki-native zone (`wiki/diary/`) — wrong provenance (knowledge territory), would enter the index/derived layer and violate the privacy posture; a declaration page on the wiki side — nothing to declare beyond what the injection line already discloses (territory path + rules), a page would only duplicate; per-month files — day granularity matches retrieval habits and keeps appends conflict-free

## Structure

- Territory: `vault/diary/`, one md file per day named `YYYY-MM-DD` (the structure declaration registers the directory; flat tolerance holds when the declaration page is absent)
- File shape: minimal optional frontmatter (`date`) + `# YYYY-MM-DD` + `## HH:MM` blocks, appended in write order within the day
- Command surface: the `diary` command skill (write path / read path); no connector, no network, no credentials

## Invariants

- Default posture: append-only verbatim capture; an UNREQUESTED rewrite or deletion of existing blocks never happens; each secretarial act needs its own explicit in-conversation instruction — never assumed, never batched
- Provenance under delegation: agent-drafted blocks carry the 代笔 mark; verbatim capture is the user's phrasing as spoken; composed content is never presented as the user's own
- Projection: every entry write closes with a registration-first map (proxy under `wiki/vault/` + index linkage); proxy bodies never copy the entry's full text; human edits re-map on the next diary touch or on request
- Use-time privacy: derivations quote minimally and backlink; log/hot lines carry the fact, never content; diary content never leaves the instance — external relay or framework/package repositories need an explicit request
- Boundaries: calendar = when things happen, todo = what is pending, diary = what was lived; promotion into notes goes through the existing save path on explicit request

## Changelog

- 0.3 2026-10-20: exposure-consent + wiki-integration ruling (user clarification dissolving the "管理" ambiguity — the challenge was about entering wiki, not delegation weight): entries map into wiki as ordinary corpus (registration-first proxies + index; the v0.1 sealing red line retired); privacy re-keyed from storage to use (minimal quotes + backlinks in derivations, mechanical log/hot, no relay outside the instance without explicit request); writing posture re-keyed to the human-writing norm — delegation is secretarial and lightweight (format tidy-up / organizing), v0.2's compose-from-context framing demoted to rare-explicit-ask; depends + mapping
- 0.2 2026-10-20: install-as-mandate ruling (installer's same-day challenge: "installing means wanting the agent to manage the diary — declare it at install, don't shackle the plugin") — pencil-mode hard veto demoted to the unasked default; delegated compose/polish/edit/delete honored per explicit instruction (代笔 provenance mark for agent-drafted blocks; instance git = undo net); checks re-keyed to unrequested rewrites; PKG disclosure and menu reworded to declare the mandate at install time
- 0.1 2026-10-20: established — vault-backed diary zone (one file per day, timestamped append-only blocks), verbatim-transcription ruling, no-projection-by-default posture, mechanical-log discipline, optional package distribution (registry listing)

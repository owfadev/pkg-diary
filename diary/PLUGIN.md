# diary: Personal Diary Zone

## Design Summary

- **Why it exists**: the framework had no home for life writing. Notes are knowledge (provenance: the wiki itself), sessions are minutes (provenance: a conversation), calendar stores facts and todo stores pending — none of them is "what I lived today, in my own words". The diary borrows the vault domain instead of erecting a new container: final-state assets, the human owns the repository, the agent is a pencil. Criteria from the domain abstraction: write-model alignment (append-only final-state) and structural lightness — no divergence that would justify a self-standing container
- **Key rulings**:
  - install-as-mandate (v0.2, from the installer's same-day challenge): installing the plugin = consenting to agent management of the diary — the v0.1 pencil-mode hard veto (verbatim only, never compose, agent never edits even on instruction) is demoted to the unasked default; delegated compose / polish / edit / delete are honored on explicit in-conversation instruction
  - provenance stays honest under management: agent-composed blocks carry the 代笔 heading mark — the diary always tells user voice from agent drafting; polish on instruction needs no mark (the user adopts the wording); instance git is the history and undo net for every delegated rewrite
  - never unasked, never batched: the default is append-only verbatim capture; each management act needs its own explicit instruction — an agent silently rewriting someone's diary is a bug, not a mode
  - vault-backed, not wiki-native: the true body lives in `vault/diary/` md files; no wiki-side pages, no default projection — projection density is zero by default (the content is personal; translation into wiki carries privacy cost and no reconciliation value)
  - the vault write model is borrowed as the default posture, not re-declared as a ceiling: agent appends by default, edit/delete is the human's freedom — a freedom that includes delegating it per-act
  - privacy red lines: content never enters any framework or package repository, never leaks into wiki pages or the derived layer; log lines stay mechanical (fact of the append, never content)
  - optional package by design (issue #20 package model): registry-listed, install on demand, never bundled into the core template
- **Rejected alternatives**: a wiki-native zone (`wiki/diary/`) — wrong provenance (knowledge territory), would enter the index/derived layer and violate the privacy posture; a declaration page on the wiki side — nothing to declare beyond what the injection line already discloses (territory path + rules), a page would only duplicate; per-month files — day granularity matches retrieval habits and keeps appends conflict-free

## Structure

- Territory: `vault/diary/`, one md file per day named `YYYY-MM-DD` (the structure declaration registers the directory; flat tolerance holds when the declaration page is absent)
- File shape: minimal optional frontmatter (`date`) + `# YYYY-MM-DD` + `## HH:MM` blocks, appended in write order within the day
- Command surface: the `diary` command skill (write path / read path); no connector, no network, no credentials

## Invariants

- Default posture: append-only verbatim capture; an UNREQUESTED rewrite or deletion of existing blocks never happens; each management act (compose / polish / edit / delete) needs its own explicit in-conversation instruction — never assumed, never batched
- Provenance under management: agent-composed blocks carry the 代笔 mark; verbatim capture is the user's phrasing as spoken; composed content is never presented as the user's own
- No wiki projection by default; mapping only on explicit request (normal map command); no auto-mapping
- Content privacy: instance data only — never into framework/package repositories, wiki pages, notes, sessions, or content-bearing log lines
- Boundaries: calendar = when things happen, todo = what is pending, diary = what was lived; promotion into notes goes through the existing save path on explicit request

## Changelog

- 0.2 2026-10-20: install-as-mandate ruling (installer's same-day challenge: "installing means wanting the agent to manage the diary — declare it at install, don't shackle the plugin") — pencil-mode hard veto demoted to the unasked default; delegated compose/polish/edit/delete honored per explicit instruction (代笔 provenance mark for agent-drafted blocks; instance git = undo net); checks re-keyed to unrequested rewrites; PKG disclosure and menu reworded to declare the mandate at install time
- 0.1 2026-10-20: established — vault-backed diary zone (one file per day, timestamped append-only blocks), verbatim-transcription ruling, no-projection-by-default posture, mechanical-log discipline, optional package distribution (registry listing)

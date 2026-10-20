# diary: Personal Diary Zone

## Design Summary

- **Why it exists**: the framework had no home for life writing. Notes are knowledge (provenance: the wiki itself), sessions are minutes (provenance: a conversation), calendar stores facts and todo stores pending — none of them is "what I lived today, in my own words". The diary borrows the vault domain instead of erecting a new container: final-state assets, the human owns the repository, the agent is a pencil. Criteria from the domain abstraction: write-model alignment (append-only final-state) and structural lightness — no divergence that would justify a self-standing container
- **Key rulings**:
  - vault-backed, not wiki-native: the true body lives in `vault/diary/` md files; no wiki-side pages, no default projection — projection density is zero by default (the content is personal; translation into wiki carries privacy cost and no reconciliation value)
  - the vault write model is borrowed, not re-declared: agent appends are append-only, edit/delete freedom belongs to the human (the vault contract verbatim)
  - verbatim transcription: the agent never invents, completes, or polishes — a diary entry is the user's phrasing, typos and tone included; the agent formats only the timestamped block shell
  - privacy red lines: content never enters any framework or package repository, never leaks into wiki pages or the derived layer; log lines stay mechanical (fact of the append, never content)
  - optional package by design (issue #20 package model): registry-listed, install on demand, never bundled into the core template
- **Rejected alternatives**: a wiki-native zone (`wiki/diary/`) — wrong provenance (knowledge territory), would enter the index/derived layer and violate the privacy posture; a declaration page on the wiki side — nothing to declare beyond what the injection line already discloses (territory path + rules), a page would only duplicate; per-month files — day granularity matches retrieval habits and keeps appends conflict-free

## Structure

- Territory: `vault/diary/`, one md file per day named `YYYY-MM-DD` (the structure declaration registers the directory; flat tolerance holds when the declaration page is absent)
- File shape: minimal optional frontmatter (`date`) + `# YYYY-MM-DD` + `## HH:MM` blocks, appended in write order within the day
- Command surface: the `diary` command skill (write path / read path); no connector, no network, no credentials

## Invariants

- Append-only agent writes; existing blocks never rewritten or deleted; edit/delete is human freedom
- Verbatim transcription; no invention, no unasked polish
- No wiki projection by default; mapping only on explicit request (normal map command); no auto-mapping
- Content privacy: instance data only — never into framework/package repositories, wiki pages, notes, sessions, or content-bearing log lines
- Boundaries: calendar = when things happen, todo = what is pending, diary = what was lived; promotion into notes goes through the existing save path on explicit request

## Changelog

- 0.1 2026-10-20: established — vault-backed diary zone (one file per day, timestamped append-only blocks), verbatim-transcription ruling, no-projection-by-default posture, mechanical-log discipline, optional package distribution (registry listing)

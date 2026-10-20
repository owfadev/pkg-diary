---
name: diary
owner: diary
consumes: [diary]
description: "Personal diary zone in vault/diary/ — one md file per day (YYYY-MM-DD): append today's entry with the user's words verbatim (写日记 / 记一下), read back by date, range, or keyword (翻日记 / 回顾). The true body lives in vault — no wiki projection, never auto-mapped; content never leaves the instance. Triggers: 日记, 写日记, 记日记, 记一下今天, 翻日记, 回顾日记, 查日记, diary, journal."
---

# diary: personal diary (vault-backed)

The user's personal daily writing, stored as real assets under `vault/diary/` (one md file per day, named `YYYY-MM-DD`). This command carries only the write path (append today's entry, verbatim transcription) and the read path (by date / range / keyword); placement follows the structure declaration, projection is opt-in only. The diary is life writing, not knowledge notes — it stays in vault, out of the wiki derived layer.

## Scope

Write: `vault/diary/YYYY-MM-DD.md` (append-only timestamped blocks; file created when absent), log (one mechanical line per append, no content)
Read: `vault/diary/`, `wiki/structure.md` (placement declaration)

## Steps

1. **Write path** (写日记 / 记一下…): resolve today's file `vault/diary/<YYYY-MM-DD>.md` — absent → create it (minimal frontmatter: date, optional; `# YYYY-MM-DD` heading) — append the content as a new `## HH:MM` block; transcription verbatim, never invented, never polished unless asked; close with one mechanical log line (type other, fact of the append only)
2. **Read path** (翻日记 / 回顾 / 查某天): resolve the target by date, range, or keyword (grep under `vault/diary/`) → relay the entries verbatim with date + time provenance; a digest or summary only on explicit request, clearly marked, verbatim quotes underneath

## Prohibitions

- Never rewrite or delete existing blocks (append-only on the agent side; edit/delete freedom belongs to the human)
- Never invent, complete, or silently "fix" diary content; the user's phrasing is transcribed as spoken
- Never project diary content into wiki pages or the derived layer; never auto-map; proxy pages only on explicit request (normal map command)
- Never let content leak into log lines, notes, sessions, or any repository other than the instance's own vault

## Language

Verbatim quotes keep their original language and phrasing exactly; conversational framing follows the session language. Dates and file names stay `YYYY-MM-DD`.

## Parameters

- Date (optional; defaults to today for writing; required for reading a specific day)
- Content (the entry text, for the write path)

## Injected Section (plugin usage blocks)

> This region is a wiki_plugin_kernel projection: consumes pulls merged with usage_routes source-side routing; disclosure order = owner first, routed blocks in the middle, pulled blocks last (rebuilt by inject / all); handwritten content does not belong here — to change the write-side contract, edit PLUGIN.yaml.

<!-- cmd-inject:start -->
<!-- usage:diary -->
- Writing (写日记 / 记一下…): land at `vault/diary/YYYY-MM-DD.md` (today); absent → create with minimal frontmatter (date only, optional) + a `# YYYY-MM-DD` heading; further entries the same day append as new `## HH:MM` blocks — append-only, existing blocks never rewritten or deleted; transcription is verbatim (the user's phrasing, including typos and tone), never invented, never polished unless the user asks
- Reading (翻日记 / 回顾 / 查某天): resolve by date, range (`YYYY-MM-DD..YYYY-MM-DD`), or keyword (grep under `vault/diary/`); relay entries verbatim with date + time provenance; a digest/summary is produced only on explicit request and clearly marked as such — the quotes stay verbatim underneath
- Placement sync: on install, `vault/diary/` is declared in `wiki/structure.md`'s structure block when that page exists (flat tolerance when absent — the page is never created on the diary's behalf); after human re-organization of vault, the same sync rule applies
- Projection policy: no default wiki projection, never auto-mapped; an explicit user request maps an entry through the normal map command (proxy page carries raw_file / raw_sha256, living under wiki/vault/ per the mapping contract)
- log discipline: after an append, one mechanical line (type other) — the fact of the write and its date, never content; reading and relaying write nothing
- Boundaries: calendar = what happens when, todo = what is pending, diary = what was lived; promoting diary material into notes/sessions goes only through the existing save path on explicit user request (derivations out-only)
<!-- /usage:diary -->
<!-- cmd-inject:end -->

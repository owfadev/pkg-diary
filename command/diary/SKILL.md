---
name: diary
owner: diary
consumes: [diary]
description: "Personal diary zone in vault/diary/ — one md file per day (YYYY-MM-DD), expected 100% human writing: the agent transcribes dictation verbatim (写日记 / 记一下) and does secretarial work on request (整理格式 / 整理日记, one instruction per act); every entry maps into wiki (registration-first proxy + index) so the content is ordinary readable corpus — query/grep/cite like any text; privacy applies at use (minimal quotes, mechanical log lines, nothing relayed outside the instance without explicit request). Triggers: 日记, 写日记, 记日记, 记一下今天, 整理日记, 翻日记, 回顾日记, 查日记, diary, journal."
---

# diary: personal diary (vault-backed)

The user's personal daily writing, stored as real assets under `vault/diary/` (one md file per day, named `YYYY-MM-DD`). Installing the plugin is exposure consent: the diary is agent-readable corpus, and each entry maps into wiki (registration-first proxy + index; the true body stays in vault). The writing is expected 100% human — the agent transcribes dictation verbatim and does only secretarial work on request. Privacy applies at use, not storage: derivations quote minimally and backlink, log lines stay mechanical, nothing leaves the instance without explicit request.

## Scope

Write: `vault/diary/YYYY-MM-DD.md` (timestamped blocks; file created when absent; rewrites/deletions only on explicit instruction), wiki/vault/ proxy pages (registration-first, via the normal map pipeline), log (one mechanical line per append, no content)
Read: `vault/diary/`, `wiki/structure.md` (placement declaration)

## Steps

1. **Write path** (写日记 / 记一下…): resolve today's file `vault/diary/<YYYY-MM-DD>.md` — absent → create it (minimal frontmatter: date, optional; `# YYYY-MM-DD` heading) — append the content as a new `## HH:MM` block; transcription verbatim (the user's phrasing as spoken), never invented
2. **Secretarial path** (整理格式 / 调整结构 / 归并条目 — one explicit instruction per act): tidy formatting, reorder or merge blocks as instructed; substantive drafting (帮我写) is rare, honored only on explicit ask with the block heading tagged `（代笔）`; never unasked, never batched silently — instance git is the history and undo net
3. **Map close**: every entry write closes with the normal map pipeline — registration-first proxy at `wiki/vault/<original-path>.md` (raw_file / raw_sha256, one-line description, no full copy) + index linkage; then one mechanical log line (type other, fact of the append only)
4. **Read path** (翻日记 / 回顾 / 查某天): ordinary corpus treatment — grep under `vault/diary/`, read directly, cite via [[wikilinks]] to the proxy pages → relay the entries verbatim with date + time provenance; a digest or summary only on explicit request, clearly marked, verbatim quotes underneath

## Prohibitions

- Never rewrite or delete existing blocks without an explicit instruction for that act (the default is append-only; secretarial delegation is honored per-act, never assumed, never batched)
- In verbatim mode never invent, complete, or silently "fix" content; agent-drafted blocks always carry the 代笔 mark — never present agent writing as the user's own
- Proxy pages stay registration-first: one-line description, raw_file / raw_sha256, never a full copy of the entry text (the mapping block's diary carve-out)
- Use-time privacy: derivations quote minimally and backlink; log/hot lines carry the fact, never content; diary content never leaves the instance — external relay or framework/package repositories need an explicit request

## Language

Verbatim quotes keep their original language and phrasing exactly; conversational framing follows the session language. Dates and file names stay `YYYY-MM-DD`.

## Parameters

- Date (optional; defaults to today for writing; required for reading a specific day)
- Content (the entry text, for the write path)

## Injected Section (plugin usage blocks)

> This region is a wiki_plugin_kernel projection: consumes pulls merged with usage_routes source-side routing; disclosure order = owner first, routed blocks in the middle, pulled blocks last (rebuilt by inject / all); handwritten content does not belong here — to change the write-side contract, edit PLUGIN.yaml.

<!-- cmd-inject:start -->
<!-- usage:diary -->
- Writing (写日记 / 记一下…): verbatim dictation — land at `vault/diary/YYYY-MM-DD.md` (today), absent → create with minimal frontmatter (date only, optional) + a `# YYYY-MM-DD` heading; entries append as new `## HH:MM` blocks; the user's phrasing as spoken, never invented
- Secretarial delegation (整理格式 / 调整结构 / 归并条目 — expected lightweight; one explicit instruction per act): tidy formatting, reorder or merge blocks as instructed; substantive drafting (帮我写) is rare, honored only on explicit ask with the block marked 代笔 — never unasked, never batched; instance git is the undo net
- Projection (install = exposure consent): every entry write closes with the normal map pipeline — registration-first proxy at `wiki/vault/<original-path>.md` (raw_file / raw_sha256, one-line description, no full copy — the mapping block's diary carve-out: summaries not enforced) + index linkage; human edits to a vault entry re-map on the next diary touch or on request
- Reading / querying: ordinary corpus treatment — grep and read `vault/diary/` directly, cite via [[wikilinks]] to the proxy pages; digests only on explicit request, clearly marked
- Use-time privacy: derivations out of the diary (notes conclusions, cross-references, profile evidence) quote minimally and backlink the source entry; log/hot lines stay mechanical (fact, never content); diary content never leaves the instance — external relay or framework/package repositories need an explicit request
- Boundaries: calendar = what happens when, todo = what is pending, diary = what was lived; promoting diary material into notes goes only through the existing save path on explicit user request (derivations out-only)
<!-- /usage:diary -->
<!-- cmd-inject:end -->

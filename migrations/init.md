---
verb: init
verify: init.py
---
First-run setup for the diary zone (light — no wiki pages are created): ensure the `vault/diary/` directory exists (an empty start is valid; creating it eagerly only to anchor the territory — lazy is equally acceptable, the first entry can birth it). When `wiki/structure.md` is present (the structure plugin's declaration page), append the `diary/` line to its structure block mapping; when absent, flat tolerance holds — never create the page on the diary's behalf.

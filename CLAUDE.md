# CLAUDE.md

What this repo is, and what `UXLC-utils-sparse/` holds, are in [README.md](README.md).

## `../UXLC-utils` is the source of truth — never edit `UXLC-utils-sparse/` directly

To change anything under `UXLC-utils-sparse/`, regenerate it upstream and resync. The
generators no longer live in UXLC-utils either: they moved to MAM-basics on 2026-08-03, so the
regeneration step runs there.

1. `../MAM-basics/py/main_uxlc_mega.py` — regenerates the canonical files in `../UXLC-utils/`
2. `main_update_vendored_files.py`, from this repo root — refreshes the vendored subset here

The sync works by intersection with what is already present locally, so it covers exactly the
`in/` and `data/` files listed in `UXLC-utils-sparse/provenance.md` and adds nothing. That is
also why it cannot be used to pull something new in.

## Do not vendor UXLC-utils' Python back in

Seventeen `.py` sat under `UXLC-utils-sparse/py/` until 2026-08-03. Nothing here ever imported
them, and by the end they could not run here at all: they import `mb_cmn`, which the sparse copy
never carried, so the one script among them raised `ModuleNotFoundError`. Their one entry point,
the ad-hoc "where on the page is this atom" query, is now run from MAM-basics, which reads
`../UXLC-utils` directly — the same corpus `UXLC-utils-sparse/in/UXLC-39/` mirrors:

```bash
C:\Users\BenDe\GitRepos\MAM-basics\.venv\Scripts\python.exe C:\Users\BenDe\GitRepos\MAM-basics\py\main_uxlc_estimate_atom_loc.py <book_id> <c:v> <word>
```

`book_id` is a UXLC book name (`Numbers`, `Genesis`, `Isaiah`); `c:v` is colon-separated; the
word is matched exactly first, then stripped of vowels and accents.

## Only one of the two JSON has a reader here

`lenin-wiki/main_make_wikisource_page.py` reads `data/lci_augrecs.json`. `data/lci_recs.json`
and the 39 XML under `in/UXLC-39/` are kept as this repo's own snapshot of the corpus it
indexes, not because a program here reads them — so a change in how they are generated will not
show up as a failure in this repo.

# CLAUDE.md

What this repo is, and what `UXLC-utils-sparse/` holds, are in [README.md](README.md).

## There is no Python here — the code is `../MAM-basics/py/`

Every `.py` this repo tracked left on 2026-08-22, under Phase 4 of
`../MAM-basics/doc/PLAN-evacuate-python-from-codex-index-trio.md`. **Twenty-one files: do not
put one back.** Eleven of them were copies of MAM-basics' own modules under three kinds of
disguise — renamed (`my_locales` for `bib_locales`, `my_open` for `file_io`, `mam_book_names`
for `mam_bknas`, `mam_book_names_and_std_book_names` for `mam_bknas_and_std_bknas`), out of
package (`vtrad_data`, `vtrad_helpers` and `get_cvm_rec_from_bcvt`, which are `py_misc` there)
or under the same name (`hebrew_letters`, `hebrew_punctuation`, `hebrew_verse_numerals`,
`my_utils`) — and the code that used them imports MAM-basics' directly now.

`.vscode/launch.json` went with them. Both of its debugpy configurations named a program that no
longer exists here, and one of the two had named a path this repo never had: `aleppo/…`, which
was codex-index-aleppo's directory name until a rename on 2026-03-28.

**Two entry points in MAM-basics write or refresh everything here that is not made by hand.**
Run either from anywhere; both address this repo by absolute path, through
`MAM-basics/py/lenin_paths.py`.

## The three files under `lenin-wiki/` are generated

`index-s0-annotated.json`, `index-s2-grouped-by-book.json` and `index.wiki` are written by one
program, from one input, `UXLC-utils-sparse/data/lci_augrecs.json`:

```powershell
C:/Users/BenDe/GitRepos/MAM-basics/.venv/Scripts/python.exe C:/Users/BenDe/GitRepos/MAM-basics/py/main_lenin_wikisource_page.py
```

That was `lenin-wiki/main_make_wikisource_page.py` here until the move. The name changed because
codex-index-aleppo has a file of that name too and the two are different tools against different
input formats.

**Regenerating them is how a change is verified**: all three come back byte-identical unless
something real has changed, which is what MAM-basics' Phase 3 used as its oracle.

## `../UXLC-utils` is the source of truth — never edit `UXLC-utils-sparse/` directly

To change anything under `UXLC-utils-sparse/`, regenerate it upstream and resync. The
generators no longer live in UXLC-utils either: they moved to MAM-basics on 2026-08-03, so both
steps run there.

1. `../MAM-basics/py/main_uxlc_mega.py` — regenerates the canonical files in `../UXLC-utils/`
2. `../MAM-basics/py/main_lenin_vendor_uxlc.py` — refreshes the vendored subset here

```powershell
C:/Users/BenDe/GitRepos/MAM-basics/.venv/Scripts/python.exe C:/Users/BenDe/GitRepos/MAM-basics/py/main_lenin_vendor_uxlc.py
```

That was this repo's root `main_update_vendored_files.py`, with a two-line fork of MAM-basics'
`mb_cmn/vendoring_sync.py` beside it; the two lines were the breadcrumb's filename, and
`write_provenance` takes it as an argument now. `UXLC-utils-sparse/provenance.md` keeps its name
— no leading underscore, unlike MAM-basics' own `_provenance.md` files.

The sync works by intersection with what is already present locally, so it covers exactly the
`in/` and `data/` files listed in `UXLC-utils-sparse/provenance.md` and adds nothing. That is
also why it cannot be used to pull something new in.

**As of 2026-08-22 the vendored copy is behind**: it was taken at UXLC-utils `748ee2f` on
2026-08-03, and running the refresh moves `data/lci_augrecs.json` and `data/lci_recs.json`.
Refreshing it therefore also moves the three files under `lenin-wiki/`, `lci_augrecs.json` being
the pipeline's input — so it is a regeneration rather than a data update, and MAM-basics' Phase 3
deliberately left it alone rather than mix the two in one diff.

## Do not vendor UXLC-utils' Python back in

Seventeen `.py` sat under `UXLC-utils-sparse/py/` until 2026-08-03. Nothing here ever imported
them, and by the end they could not run here at all: they import `mb_cmn`, which the sparse copy
never carried, so the one script among them raised `ModuleNotFoundError`. Their one entry point,
the ad-hoc "where on the page is this atom" query, is now run from MAM-basics, which reads
`../UXLC-utils` directly — the same corpus `UXLC-utils-sparse/in/UXLC-39/` mirrors:

```powershell
C:/Users/BenDe/GitRepos/MAM-basics/.venv/Scripts/python.exe C:/Users/BenDe/GitRepos/MAM-basics/py/main_uxlc_estimate_atom_loc.py <book_id> <c:v> <word>
```

`book_id` is a UXLC book name (`Numbers`, `Genesis`, `Isaiah`); `c:v` is colon-separated; the
word is matched exactly first, then stripped of vowels and accents.

## Only one of the two JSON has a reader

`main_lenin_wikisource_page.py` in MAM-basics reads `data/lci_augrecs.json`. `data/lci_recs.json`
and the 39 XML under `in/UXLC-39/` are kept as this repo's own snapshot of the corpus it
indexes, not because any program reads them — so a change in how they are generated will not
show up as a failure here.

## What no program writes

Everything else this repo tracks is hand-made or vendored, and nothing regenerates it:
`page-snips/` (one PNG crop and the README recording what it settles), `README.md`, this file,
`.gitattributes` and `.gitignore`. `UXLC-utils-sparse/` is vendored rather than generated — the
refresh above copies it, and UXLC-utils' own generators are what write the originals.

## MAM-basics still lints this repo, and still scans it for NFC

`py/tests/test_h_dot_below_nfc.py` here was deleted with the rest, but the check it ran did not
go with it: MAM-basics' own copy carries a `codex-index-leningrad` scope, which walks this
repo's tracked files with `UXLC-utils-sparse/` excluded. Eight files are in scope after the
move, measured 2026-08-22 after the deletion.
So a decomposed h-with-dot-below authored here is still caught — by a run of MAM-basics' suite,
not by anything here.

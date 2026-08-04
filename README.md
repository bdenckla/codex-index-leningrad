# codex-index-leningrad
Index of the Leningrad Codex

The folder "UXLC-utils-sparse" is a sparse vendored copy of selected files from
the sibling repo "UXLC-utils", which is the canonical source. See
UXLC-utils-sparse/provenance.md and main_update_vendored_files.py for the sync
details.

It is data only — 39 XML under in/UXLC-39 and two JSON under data. Seventeen of
UXLC-utils' .py sat under UXLC-utils-sparse/py until 2026-08-03; they went when
UXLC-utils' Python moved to the sibling repo MAM-basics, which is now where the
generators of everything under UXLC-utils' in/, out/, gh-pages/ and data/ live.

"page-snips" holds crops of Leningrad Codex page images, one per fact read off
the manuscript, with page-snips/README.md recording what each one settles. See
that file for how to get from a folio number to an image.

# codex-index-leningrad
Index of the Leningrad Codex

**This repo holds data, and no code.** Its Python moved to the sibling repo
MAM-basics on 2026-08-22, under Phase 3 of that repo's
`doc/PLAN-evacuate-python-from-codex-index-trio.md`; the data stayed here and goes on
being hosted here. Nothing about that is provisional. See CLAUDE.md for which program
in MAM-basics writes what here.

The folder "UXLC-utils-sparse" is a sparse vendored copy of selected files from
the sibling repo "UXLC-utils", which is the canonical source. See
UXLC-utils-sparse/provenance.md for what it holds and where each file came from,
and CLAUDE.md for how to resync it.

It is data only — 39 XML under in/UXLC-39 and two JSON under data. Seventeen of
UXLC-utils' .py sat under UXLC-utils-sparse/py until 2026-08-03; they went when
UXLC-utils' Python moved to MAM-basics, which is now where the
generators of everything under UXLC-utils' in/, out/, gh-pages/ and data/ live.

The folder "lenin-wiki" holds the wikitext of the Wikisource page indexing this
codex, and the two JSON the pipeline derives on the way to it. All three are
generated, from UXLC-utils-sparse/data/lci_augrecs.json; CLAUDE.md gives the
command.

"page-snips" holds crops of Leningrad Codex page images, one per fact read off
the manuscript, with page-snips/README.md recording what each one settles. See
that file for how to get from a folio number to an image. Those crops are made by
hand — no program writes them.

"""Exports main

TWO ROOTS, AND ONE OF THEM IS TWO DIRECTORIES.  The four paths below were
cwd-relative literals until 2026-08-22 -- ``"UXLC-utils-sparse/data/..."`` and
three ``"lenin-wiki/..."`` -- so this pipeline ran from this repo's root and
nowhere else.  They are now spelled off ``_REPO_ROOT``, which is the DATA root:
the vendored UXLC-utils subset it reads sits at the top of this repo, and the
three artifacts it writes sit beside this file.  Phase 1 of
``../MAM-basics/doc/PLAN-evacuate-python-from-codex-index-trio.md`` names the two
roots apart so that Phase 3, which takes the Python to MAM-basics and leaves both
of those trees here, has one line to change.

The counterpart pipeline, codex-index-aleppo's
``aleppo-wiki/main_make_wikisource_page.py``, is a different tool against a
different input format, and its four literals had been DEAD since 2026-03-28.
This one has run correctly the whole time, which is why the trio's Phase 0 could
use it as an oracle and could not use the other.
"""

from pathlib import Path

from py.read_json_file import read_json_file
from py.s1_collapse_rows import s1_collapse_rows
from py.s2_group_by_book import s2_group_by_book
from py.write_wikitext_file import write_wikitext_file
import py.my_open as my_open


def main():
    annotated = read_json_file(_JSON_IN_PATH)
    my_open.json_dump_to_file_path(annotated, _JSON_OUT_PATH_S0)
    #
    s1_collapsed = s1_collapse_rows(annotated["body"])
    #
    s2_grouped = s2_group_by_book(s1_collapsed)
    my_open.json_dump_to_file_path(s2_grouped, _JSON_OUT_PATH_S2)
    #
    write_wikitext_file(s2_grouped, _WIKITEXT_OUT_PATH)


_WIKI_DIR = Path(__file__).resolve().parent
_REPO_ROOT = _WIKI_DIR.parent
_JSON_IN_PATH = _REPO_ROOT / "UXLC-utils-sparse" / "data" / "lci_augrecs.json"
_JSON_OUT_PATH_S0 = _WIKI_DIR / "index-s0-annotated.json"
_JSON_OUT_PATH_S2 = _WIKI_DIR / "index-s2-grouped-by-book.json"
_WIKITEXT_OUT_PATH = _WIKI_DIR / "index.wiki"


if __name__ == "__main__":
    main()

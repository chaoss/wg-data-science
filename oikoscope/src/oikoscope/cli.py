"""Validate raw JSON datasets against Oikoscope schemas."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

import jsonschema
from jsonschema import Draft202012Validator

_ROOT = Path(__file__).resolve().parents[2]
_SCHEMA = _ROOT / "schemas" / "apache-dataset.schema.json"
_APACHE = _ROOT / "data" / "raw" / "apache.json"


def _validate_file(*, schema_path: Path, data_path: Path, label: str) -> list[str]:
    messages: list[str] = []
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    data = json.loads(data_path.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
    for err in errors:
        loc = "/".join(str(p) for p in err.path) or "(root)"
        messages.append(f"{label}: /{loc}: {err.message}")
    return messages


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate oikoscope data/raw JSON files.")
    parser.add_argument(
        "--compact",
        action="store_true",
        help="Print only errors (default prints summary even on success).",
    )
    args = parser.parse_args(argv)

    if not _SCHEMA.is_file():
        print(f"error: schema not found: {_SCHEMA}", file=sys.stderr)
        return 2
    if not _APACHE.is_file():
        print(f"error: data file not found: {_APACHE}", file=sys.stderr)
        return 2

    messages = _validate_file(schema_path=_SCHEMA, data_path=_APACHE, label="apache.json")
    if messages:
        for m in messages:
            print(m, file=sys.stderr)
        return 1

    data = json.loads(_APACHE.read_text(encoding="utf-8"))
    n = len(data)
    names = [row["project"] for row in data]
    dupes = [k for k, v in Counter(names).items() if v > 1]

    if not args.compact:
        print(f"ok: apache.json — {n} records", file=sys.stderr)
        if dupes:
            print(f"warning: duplicate project names: {', '.join(dupes)}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

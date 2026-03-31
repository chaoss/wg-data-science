<p align="center">
  <img src="assets/oikoscope-logo.png" alt="Oikoscope" width="420">
</p>

**Structured, reproducible views of open source foundation and project health, aligned with [CHAOSS](https://chaoss.community) metrics.**

The name evokes the ancient Greek *oikos* (οἶκος): the household as a foundational social unit—here, the “household” of projects and communities we observe with transparent methods. See [_Oikos_ (historical background)](https://en.wikipedia.org/wiki/Oikos).

Oikoscope is stewarded as an open source project by the [CHAOSS Data Science Working Group](https://chaoss.community/inside-the-chaoss-data-science-working-group/). This directory is laid out so it can be published as a **standalone Git repository**; see [`docs/standalone-repository.md`](docs/standalone-repository.md).

### Canonical home

**Where to browse and clone today:** **[github.com/chaoss/wg-data-science/tree/main/oikoscope](https://github.com/chaoss/wg-data-science/tree/main/oikoscope)** — this subtree is the live source of truth until a dedicated remote exists.

**Recommended standalone remote:** **[github.com/chaoss/oikoscope](https://github.com/chaoss/oikoscope)** — same org as other CHAOSS repositories, clear naming, and a natural place for issues, releases, and DCO. Publish with `git subtree split` (see [`docs/standalone-repository.md`](docs/standalone-repository.md)) and update `pyproject.toml` `[project.urls]` when ready.

### Development

Python 3.10+:

```bash
cd oikoscope
python -m pip install -e .
python -m oikoscope
```

This validates [`data/raw/apache.json`](data/raw/apache.json) against [`schemas/apache-dataset.schema.json`](schemas/apache-dataset.schema.json). The `oikoscope-validate` entry point is also installed on `PATH` when your environment exposes the `Scripts` (or `bin`) directory.

Branding and naming: [`docs/brand.md`](docs/brand.md). Release notes: [`CHANGELOG.md`](CHANGELOG.md).

## What we do

- **Curate and publish** foundation-scale metadata (for example public communication and documentation endpoints) to support CHAOSS-aligned audits and research.
- **Document methodology** for cross-foundation comparison, outlier analysis, and downstream modeling.
- **Welcome contributions** to data completeness and to analysis code as the project matures.

Current focus includes manual enrichment of **Apache Software Foundation** project metadata — **47** projects in [`data/raw/apache.json`](data/raw/apache.json) (reproduce counts via [`docs/dataset-status.md`](docs/dataset-status.md)). CNCF and Eclipse work is part of the broader research design.

**EU policy context:** [`docs/cra-eu-relevance.md`](docs/cra-eu-relevance.md) links Regulation (EU) 2024/2847 (CRA) steward expectations to the kinds of evidence CHAOSS-style metrics help surface.

## Repository layout

| Path | Purpose |
|------|---------|
| [`data/raw/`](data/raw/) | Immutable hand-curated datasets (`apache.json` and future foundations) — **canonical data root** |
| [`schemas/`](schemas/) | JSON Schema for raw datasets (`apache-dataset.schema.json`) |
| [`src/oikoscope/`](src/oikoscope/) | Python package (validation CLI) |
| [`pyproject.toml`](pyproject.toml) | Package metadata and `[project.urls]` → monorepo today; update after subtree split |
| [`CHANGELOG.md`](CHANGELOG.md) | Version history ([Keep a Changelog](https://keepachangelog.com/)) |
| [`docs/brand.md`](docs/brand.md) | Naming, taglines, logo paths |
| [`docs/research-design.md`](docs/research-design.md) | Full research design and analysis plan (migrated from the Foundation Stats project) |
| [`docs/repository-structure-recommendation.md`](docs/repository-structure-recommendation.md) | Recommended folder layout for notebooks, `src/`, tests, and outputs |
| [`docs/standalone-repository.md`](docs/standalone-repository.md) | How to split this tree into its own GitHub repo |
| [`docs/cra-eu-relevance.md`](docs/cra-eu-relevance.md) | CRA context for foundations and metrics |
| [`docs/dataset-status.md`](docs/dataset-status.md) | Reproducible corpus counts |
| [`assets/`](assets/) | Brand assets: full logo, favicons (`favicon.ico`, `favicon-*.png`), `apple-touch-icon.png` |
| [`scripts/generate_favicons.py`](scripts/generate_favicons.py) | Regenerate favicons from `assets/oikoscope-logo.png` (requires Pillow) |

**CI:** this package is validated in the monorepo by [`.github/workflows/validate-oikoscope-data.yml`](https://github.com/chaoss/wg-data-science/blob/main/.github/workflows/validate-oikoscope-data.yml) (`oikoscope-validate` on changes under `oikoscope/`). Further planned work (`notebooks/`, `tests/`, `config/`) is tracked via issues per the structure recommendation.

## Contributing data (Apache)

Coordination uses the [community tracker](https://docs.google.com/spreadsheets/d/1rWW773oOudiM5xpfroIjEiQazOr42YNCfGWISnR0Tk4/edit?usp=sharing):

- **In Progress**: Someone is working on the project—avoid duplicates.
- **Done**: Metadata merged into [`data/raw/apache.json`](data/raw/apache.json).
- **Empty / To Do**: Set to **In Progress** when you start.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for DCO sign-off and PR expectations.

## Governance and conduct

- [`GOVERNANCE.md`](GOVERNANCE.md) — maintainers and decision-making
- [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) — CHAOSS Code of Conduct
- [`SECURITY.md`](SECURITY.md) — how to report sensitive issues

## Maintainers

- Ernest Owojori
- Sal Kimmich

Reach out on CHAOSS Slack (**#data-science** or **#wg-data-science**) or open an issue on **[wg-data-science](https://github.com/chaoss/wg-data-science/issues)** (mention **Oikoscope** in the title until [`github.com/chaoss/oikoscope`](https://github.com/chaoss/oikoscope) is live).

## License

[MIT](LICENSE) — Copyright (c) 2026 CHAOSS, consistent with the [wg-data-science](https://github.com/chaoss/wg-data-science) license.

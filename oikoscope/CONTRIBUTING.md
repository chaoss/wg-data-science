<p align="center">
  <img src="assets/oikoscope-logo.png" alt="Oikoscope" width="280">
</p>

# Contributing to Oikoscope

Thank you for helping improve Oikoscope. This project is part of the [CHAOSS Data Science Working Group](https://chaoss.community/inside-the-chaoss-data-science-working-group/); broader CHAOSS participation guidance is at [chaoss.community/participate](https://chaoss.community/participate/).

## Where to discuss

- **Slack**: `#data-science` in the [CHAOSS Slack workspace](https://join.slack.com/t/chaoss-workspace/shared_invite/zt-r65szij9-QajX59hkZUct82b0uACA6g)
- **Issues and PRs**: Prefer **[github.com/chaoss/oikoscope](https://github.com/chaoss/oikoscope/issues)** once that remote is live. While nested in `wg-data-science`, use this monorepo’s issues and mention **Oikoscope** in the title (see [`docs/standalone-repository.md`](docs/standalone-repository.md)).

## Contributing data (Apache metadata)

Manual collection of Apache project metadata is coordinated with the [community tracker spreadsheet](https://docs.google.com/spreadsheets/d/1rWW773oOudiM5xpfroIjEiQazOr42YNCfGWISnR0Tk4/edit?usp=sharing):

- **In Progress**: Someone is working on a project; avoid duplicating work.
- **Done**: Merged into `data/raw/apache.json` in this repository.
- **Empty / To Do**: Available; set to **In Progress** when you start.

Open a pull request that updates `data/raw/apache.json` and briefly describe sources (project website, mailing list page, and so on).

## Contributing code and documentation

1. Open an issue for non-trivial changes, or comment on an existing one.
2. Fork the repository, create a branch, and submit a pull request.
3. Keep commits focused; reference related issues in the PR description.

## Developer Certificate of Origin (DCO)

CHAOSS projects require a [DCO](https://developercertificate.org/) sign-off on every commit. Use:

```bash
git commit -s -m "Your message"
```

For GitHub web edits, include a line in the commit message:

```
Signed-off-by: Your Name <your.email@example.org>
```

See the parent [wg-data-science CONTRIBUTING](https://github.com/chaoss/wg-data-science/blob/main/CONTRIBUTING.md) for screenshots and a browser plugin option.

## Code of Conduct

All participants must follow the [CHAOSS Community Code of Conduct](https://chaoss.community/code-of-conduct).

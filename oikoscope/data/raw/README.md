# Raw data

Immutable, original exports and hand-curated metadata as collected from public foundation sources.

## Apache (`apache.json`)

Array of objects with public communication and documentation URLs per Apache project. Updates should go through the process in [`CONTRIBUTING.md`](../../CONTRIBUTING.md) (tracker status and pull request).

### Fields (current convention)

| Field | Description |
|-------|--------------|
| `project` | Display name of the project |
| `slack_url` | ASF Slack or project-specific Slack when applicable |
| `mailing_list` | Primary mailing list or community contact page |
| `discord_url` | Discord, if any |
| `zulip_url` | Zulip, if any |
| `forum_url` | Forum, if any |
| `blog_url` | Project blog |
| `docs_url` | Primary documentation |

The schema for this file is [`schemas/apache-dataset.schema.json`](../../schemas/apache-dataset.schema.json). Validate locally from the `oikoscope/` directory with `python -m oikoscope`.

Refinements to this schema should be proposed in an issue so downstream analyses can stay aligned.

## Future layout

Additional foundations (for example CNCF, Eclipse) may appear as separate files or subdirectories under `data/raw/` with their own README notes and provenance.

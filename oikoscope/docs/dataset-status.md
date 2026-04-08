# Dataset status (Oikoscope)

Numbers below refer to **`data/raw/apache.json`** on the branch you have checked out. To reproduce the count locally:

```bash
cd oikoscope
pip install -e .
python -c "import json; print(len(json.load(open('data/raw/apache.json', encoding='utf-8'))))"
```

Or run validation (also checks the JSON Schema and prints the record count on success):

```bash
oikoscope-validate
```

As of the last documentation refresh in this repository, **Apache**: **47** hand-curated project records (communication and documentation endpoints aligned with the schema). CNCF and Eclipse corpora follow the research design in [`research-design.md`](research-design.md).

Update this file when the corpus crosses a milestone reviewers should know about.

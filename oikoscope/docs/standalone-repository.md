<p align="center">
  <img src="../assets/oikoscope-logo.png" alt="Oikoscope" width="320">
</p>

# Standalone Oikoscope repository

This directory tree is maintained under `oikoscope/` so it can be published as its **own Git repository**. **Canonical target:** [`github.com/chaoss/oikoscope`](https://github.com/chaoss/oikoscope) (CHAOSS org, public OSS home).

## While nested in `wg-data-science`

Contributors work in `wg-data-science/oikoscope/` and open pull requests against this monorepo until a dedicated remote exists.

## Publishing as a new GitHub repository

Maintain history for this subtree only:

```bash
git subtree split -P oikoscope -b oikoscope-main
git remote add oikoscope https://github.com/<org>/oikoscope.git
git push oikoscope oikoscope-main:main
```

Alternatively, copy the `oikoscope/` folder into a fresh repository with `git init`, add the remote, and push (you lose prior commit history for that subtree unless you use `subtree split` or `git filter-repo`).

## After the split

1. Enable DCO (GitHub app or branch protection) on the new repo to match CHAOSS expectations.
2. Update `pyproject.toml` `[project.urls]` (`Repository`, `Documentation`, `Bug Tracker`) to the new GitHub URLs.
3. Update `README.md` badges and links from monorepo paths to the new issue tracker and default branch. If `.github` issue/PR templates reference the logo via `github.com/<org>/wg-data-science/raw/...`, point those URLs at the new repository (or replace with paths that work in that repo).
4. Add or copy CI (for example JSON validation via `oikoscope-validate`) in `.github/workflows/` on the new remote.
5. In the original monorepo, keep a short redirect notice (for example in `dataset/foundational-stats-research/README.md` and the root `README`) pointing to the canonical Oikoscope URL.

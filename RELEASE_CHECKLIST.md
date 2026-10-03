# Release Checklist

Use this checklist for a stable public release. A merged pull request is not a release, DOI, marketplace update, or verified installation.

## Before Tagging

- [ ] Confirm that `main` contains only reviewed changes intended for the release.
- [ ] Reconcile the plugin manifests, README badge, and `CHANGELOG.md` with the release version.
- [ ] Run `python scripts\\validate_repo.py` and `python -m unittest -v tests.test_skill_scripts`.
- [ ] Inspect the `CITATION.cff`, installation instructions, examples, and external links.
- [ ] Confirm that no private calibration corpus, student material, confidential proposal content, credentials, or restricted research material is included.
- [ ] Review the diff for files that should not be distributed.

## Release

- [ ] Create an annotated Git tag matching the documented version.
- [ ] Create a GitHub release with concise user-facing notes from `CHANGELOG.md`.
- [ ] Verify the GitHub release page, archive downloads, and installation instructions against the tagged revision.
- [ ] Update any third-party registry or marketplace listing only after verifying the corresponding public version.

## Archival Citation

- [ ] Connect the repository to Zenodo or another approved archival service before creating the intended release.
- [ ] Verify the deposited version, author information, license, and generated DOI.
- [ ] Add the DOI to `CITATION.cff` only after the archive record is public and correct.
- [ ] Cite the release tag or DOI, not a moving default branch, in scholarly work.

## Communications

- [ ] Inspect the candidate social-preview image at GitHub's preview crop.
- [ ] Set it manually through **Repository Settings -> General -> Social preview**.
- [ ] Publish only factual launch material that links to the tagged release and avoids unverified adoption or impact claims.
- [ ] Record baseline repository traffic, clones, stars, forks, issues, and confirmed pilots for later comparison.

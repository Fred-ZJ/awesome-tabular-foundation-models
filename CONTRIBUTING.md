# Contributing

Thank you for helping improve Awesome Tabular Foundation Models.

## Scope and Selection

We welcome work on reusable pretrained or meta-trained models for tabular prediction, their adaptation mechanisms, evaluation, and directly relevant data resources.

Prefer primary research and useful implementations with a clear contribution. General table question answering, generic LLM agents, and models trained independently from scratch on each table belong elsewhere unless their connection to this scope is explicit.

Authors may nominate their own work. Disclose your relationship and use the same factual description and verification standards as other contributors.

## Adding a Paper

Edit resources/papers.json. Each paper needs a unique ID, full title, direct primary-source HTTPS URL, year, venue, publication status, and a short original summary.

Supported statuses are conference, journal, preprint, and technical-report. The last two currently render as arXiv entries. For another report source, update the renderer and validator explicitly.

Use a confirmed formal publication year when available. Set first_preprint only when the earlier date clarifies the history. Prefer one entry per work; a renamed arXiv version is not a new paper.

Place the paper in the category that reflects its main mechanism. Keep entries broadly chronological within a category. Avoid unsupported superlatives, leaderboard claims, citation counts, and star counts.

Regenerate the README and check the result:

~~~sh
python scripts/build_readme.py
python scripts/validate.py
~~~

Python 3.10 or newer is sufficient. No third-party packages are needed.

## Descriptions and Official Resources

Describe what the method changes: its pretraining source, representation, target-task adaptation, or evaluation contribution. Do not copy an abstract.

For a code or model release, link the author-maintained resource and verify the association from the paper or project. Public availability alone does not establish an unrestricted license, full training-data release, or reproducibility.

Implementation and data-resource entries are maintained in scripts/build_readme.py. Supporting explanations belong in docs/.

## Verification Before Submission

- Check the title, source, year, and venue against proceedings, a publisher, arXiv, or an author-maintained page.
- Distinguish technical reports, unreviewed preprints, workshops, and main-conference publications.
- Check for shared arXiv identifiers and earlier titles before adding an entry.
- Distinguish labeled context, target-specific weight updates, and pipeline search.
- Avoid mixing a single checkpoint with an ensemble or AutoML system in comparisons.
- Run the validator and inspect generated changes.

The local validator checks metadata structure and documentation consistency. Remote URL availability, scientific claims, and reproduced results require separate review.

## Corrections

Use the correction issue template for incorrect metadata, a misleading description, a broken link, or duplicate versions. Include the affected entry and a supporting primary source.

## Licensing

Contributions to the list and original descriptions are dedicated under [CC0 1.0 Universal](LICENSE). Third-party papers, code, model weights, and datasets retain their own terms.

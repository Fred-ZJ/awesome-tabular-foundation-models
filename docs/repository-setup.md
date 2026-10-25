# Repository Setup

[Back to the list](../README.md)

## Suggested GitHub Settings

**Name**

awesome-tabular-foundation-models

**Description**

A curated list of papers, models, benchmarks, and resources for tabular foundation models.

**Topics**

awesome, awesome-list, tabular-data, tabular-foundation-models, foundation-models, in-context-learning, tabpfn, tabicl, transfer-learning, machine-learning

## Contents to Upload

Upload the repository contents, including the hidden .github directory. The ZIP archive preserves the directory structure.

No GitHub account name, repository URL, credentials, or deployment service is embedded in the files. Repository-specific badges and links can be added after the destination is known.

## Local Checks

Requires Python 3.10 or newer and no third-party packages.

~~~sh
python scripts/build_readme.py --check
python scripts/validate.py
~~~

The included GitHub Actions workflow runs the local validator on pushes and pull requests. It has read-only repository permissions and does not publish anything.

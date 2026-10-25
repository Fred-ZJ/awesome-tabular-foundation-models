"""Render README.md from the curated catalog using only the Python standard library."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

INTRO = """# Awesome Tabular Foundation Models [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of papers, models, benchmarks, and resources for tabular foundation models.

The focus is **prediction on tabular data**: models pretrained or meta-trained across tasks and reused on a new table. This includes prior-data fitted networks, cross-table transfer, semantic models, adaptation, and evaluation. Table question answering and general-purpose tabular deep learning are outside the core scope.

Start with the [reading guide](docs/reading-guide.md), compare the [model families](docs/model-guide.md), or consult the [evaluation guide](docs/evaluation.md).

"""

FOOTER = """## Implementations and Model Releases

Official project links are provided where verified. Check the exact release: code, pretrained weights, hosted services, and datasets can have different licenses and access conditions.

- [TabPFN](https://github.com/PriorLabs/TabPFN) - Official Python interface for the TabPFN family; checkpoint access and terms vary by version.
- [TabICL](https://github.com/soda-inria/tabicl) - Official implementation, with resources for inference, pretraining, and synthetic task generation.
- [Mitra classifier](https://huggingface.co/autogluon/mitra-classifier) - Official first-generation classifier weights and AutoGluon usage information.
- [Mitra regressor](https://huggingface.co/autogluon/mitra-regressor) - Official first-generation regression model release.
- [TabDPT](https://github.com/layer6ai-labs/TabDPT-inference) - Official inference implementation for the real-data-pretrained model.
- [CARTE](https://github.com/soda-inria/carte) - Official graph-based pretraining and transfer implementation.
- [TabuLa-8B / RTFM](https://github.com/mlfoundations/rtfm) - Research code for language-model-based tabular transfer.
- [TabSTAR](https://github.com/alanarazi7/TabSTAR) - Official implementation for semantic transfer on tables containing text fields.
- [ConTextTab](https://github.com/SAP-samples/sap-rpt-1-oss) - Official open implementation associated with ConTextTab and SAP's relational pretrained transformer work.
- [HyperFast](https://github.com/AI-sandbox/HyperFast) - Official hypernetwork-based classifier implementation.
- [Orion-MSP](https://github.com/Lexsi-Labs/Orion-MSP) - Official multi-scale sparse attention implementation.
- [Orion-BiX](https://github.com/Lexsi-Labs/Orion-BiX) - Official bi-axial attention implementation.
- [TabForestPFN](https://github.com/FelixdenBreejen/TabForestPFN) - Official implementation for forest-prior pretraining and fine-tuning.

## Benchmark Software and Data Resources

- [TabArena](https://tabarena.ai/) - Maintained benchmark results; record the snapshot and model configuration when citing a comparison.
- [TabReD](https://github.com/yandex-research/tabred) - Official benchmark code and data preparation.
- [TabZilla](https://github.com/naszilla/tabzilla) - Official code for the neural-network-versus-boosted-tree study.
- [TabReliBench](https://github.com/Tianqi-Zhao/TabReliBench) - Official resources for predictive reliability evaluation.
- [T4](https://huggingface.co/datasets/mlfoundations/t4-full) - Tabular prediction corpus associated with TabuLa-8B; inspect provenance, filtering, and downstream overlap before reuse.

## Guides

- [Taxonomy](docs/taxonomy.md) - Pretraining sources, adaptation mechanisms, and scope.
- [Reading guide](docs/reading-guide.md) - A suggested learning path and overlapping research phases.
- [Model guide](docs/model-guide.md) - A qualitative comparison of representative model families.
- [Evaluation guide](docs/evaluation.md) - Dataset overlap, splits, context construction, budgets, and reliability.
- [Version notes](docs/version-notes.md) - Publication years, renamed papers, and model release distinctions.
- [Repository setup](docs/repository-setup.md) - Suggested GitHub description and topics.

## Contributing

Suggestions and corrections are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) and use the issue templates or open a pull request.

The catalog is maintained in [resources/papers.json](resources/papers.json). Regenerate the README and run the local checks after editing it:

~~~sh
python scripts/build_readme.py
python scripts/validate.py
~~~

The checks cover catalog consistency and local documentation. They do not reproduce model results or continuously monitor external links.

## License

The list and original descriptions are dedicated under [CC0 1.0 Universal](LICENSE). Linked papers, code, weights, and datasets retain their own licenses.
"""


def publication(paper: dict) -> str:
    if paper["status"] == "preprint":
        return f'arXiv preprint {paper["year"]}'
    if paper["status"] == "technical-report":
        return f'Technical report (arXiv) {paper["year"]}'
    return f'{paper["venue"]} {paper["year"]}'


def render(catalog: dict) -> str:
    count = sum(len(section["papers"]) for section in catalog["sections"])
    parts = [INTRO]
    parts.append(
        f'**{count} curated papers and reports** across {len(catalog["sections"])} categories. '
        f'Initial curation checked on **{catalog["checked_on"]}**. '
        'Formal publication years are used when confirmed; otherwise entries are explicitly labeled as preprints or technical reports. '
        'The list is selective and does not rank models.\n\n'
    )
    parts.append("## Contents\n\n")
    for section in catalog["sections"]:
        parts.append(f'- [{section["title"]}](#{section["id"]})\n')
    for title, anchor in (
        ("Implementations and Model Releases", "implementations-and-model-releases"),
        ("Benchmark Software and Data Resources", "benchmark-software-and-data-resources"),
        ("Guides", "guides"),
        ("Contributing", "contributing"),
        ("License", "license"),
    ):
        parts.append(f"- [{title}](#{anchor})\n")
    parts.append("\n")
    for section in catalog["sections"]:
        parts.append(f'## {section["title"]}\n\n{section["description"]}\n\n')
        for paper in section["papers"]:
            extra = ""
            if "first_preprint" in paper:
                extra = f' First preprint: {paper["first_preprint"]}.'
            parts.append(
                f'- [{paper["title"]}]({paper["url"]}) - '
                f'**{publication(paper)}**. {paper["summary"]}{extra}\n'
            )
        parts.append("\n")
    parts.append(FOOTER)
    return "".join(parts)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if README.md needs regeneration.")
    args = parser.parse_args()
    catalog = json.loads((ROOT / "resources/papers.json").read_text(encoding="utf-8"))
    expected = render(catalog)
    target = ROOT / "README.md"
    if args.check:
        if not target.is_file() or target.read_text(encoding="utf-8") != expected:
            print("README.md is stale. Run python scripts/build_readme.py.")
            return 1
        print("README.md matches the catalog.")
        return 0
    target.write_text(expected, encoding="utf-8", newline="\n")
    print("Generated README.md.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

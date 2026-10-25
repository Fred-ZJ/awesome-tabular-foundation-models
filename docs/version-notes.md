# Version Notes

[Back to the list](../README.md)

## Dates and Publication Labels

The initial curation was checked on **2026-10-25**. This is a snapshot of the list, not a promise that linked repositories or leaderboards remain unchanged.

Use a confirmed formal publication year where available. If a work is listed as an arXiv preprint or technical report, the label records the source used for curation; it does not assert that the work has no later publication.

An arXiv identifier encodes the first submission period, not necessarily the formal publication year. Examples:

- PFNs first appeared as a 2021 preprint and were published at ICLR 2022.
- TabPFN v1 first appeared as a 2022 preprint and was published at ICLR 2023.
- The TabPFN Nature article was published in 2025 even though its URL contains "024".
- TabDPT first appeared in 2024 and was published at NeurIPS 2025.
- TabPFN-2.5 first appeared in 2025 and has a revised 2026 version.

## Renamed Works

Maintain one entry per work, using the title in the linked version.

| Current entry | Earlier title or description to recognize |
| --- | --- |
| UniTabE | Pretraining a Unified Tabular Encoder for Heterogeneous Tabular Data |
| TabSTAR | A Foundation Tabular Model With Semantically Target-Aware Representations |
| TabReD | A Benchmark of Tabular Machine Learning in-the-Wild |
| The Illusion of Generalization in Tabular Language Models | Re-examining Tabular Language Model Evaluation |

Check the shared arXiv identifier before adding another entry. A substantial model generation can warrant a new report entry; a title change alone does not.

## Model Families and Releases

The original TabPFN paper, the Nature paper, and the 2.5, 3, and 3.5 reports describe different generations. A package installation named TabPFN does not identify the exact checkpoint evaluated.

Likewise, TabICL and TabICLv2, or Mitra and Mitra-v2, should not be treated as a single fixed experimental configuration. Record the specific checkpoint and adaptation mode.

The name TabFM is also used informally as an abbreviation for tabular foundation models. In this repository, the paper entry named TabFM refers specifically to [TabFM: A Zero-Shot Foundation Model for Tabular Data](https://arxiv.org/abs/2609.37959).

## What Was Checked

Titles, source links, publication labels, method placement, and official project associations were reviewed against publisher pages, proceedings, arXiv, or author-maintained releases during curation.

The automated checks validate local documentation and catalog consistency. They do not reproduce results, audit training data, verify every dependency, or establish the licensing status of all linked assets.

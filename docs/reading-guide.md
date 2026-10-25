# Reading Guide

[Back to the list](../README.md)

## A Short Starting Path

1. Read [Transformers Can Do Bayesian Inference](https://arxiv.org/abs/2112.10510) for the training-over-tasks idea.
2. Read [TabPFN](https://arxiv.org/abs/2207.01848) and the [Nature paper](https://www.nature.com/articles/s41586-024-08328-6) to connect the idea to tabular prediction.
3. Compare [TabICL](https://arxiv.org/abs/2502.05564) with [TabDPT](https://arxiv.org/abs/2410.18164): generated tasks and real tables provide different sources of pretraining knowledge.
4. Read [TabArena](https://arxiv.org/abs/2506.16791) before interpreting performance tables.
5. Use [Beyond IID](https://arxiv.org/abs/2606.30410) and [TabReliBench](https://arxiv.org/abs/2610.13654) to expand the questions beyond average predictive accuracy.

## Overlapping Research Phases

These phases are a reading aid. They overlap, and early work continues to influence later systems.

| Period | Research emphasis | Suggested anchors |
| --- | --- | --- |
| 2021-2023 | Learning a reusable predictor across tasks; early cross-table transfer | PFNs, TabPFN, TransTab, XTab |
| 2023-2024 | Heterogeneous schemas, table corpora, language semantics, and alternative meta-learning mechanisms | UniTabE, CM2, CARTE, TabLLM, TabuLa-8B, HyperFast |
| 2024-2025 | Broader prediction coverage, real-data pretraining, and efficient context processing | TabPFN v2, TabDPT, TabICL, ConTextTab, TabSTAR, Mitra |
| 2025-2026 | Prior diversity, longer contexts, conditional modeling, and deployment efficiency | TabPFN release reports, TabICLv2, Mitra-v2, LimiX, Orion |
| 2026 | Adaptation, context acquisition, pipeline optimization, and broader evaluation | Active ICL, TabFM-Auto, BeyondArena, TabReliBench |

Years mix first appearances and formal publication dates as explained in the [version notes](version-notes.md). They do not imply that a later mechanism supersedes every earlier one.

## Follow a Research Question

### How Does the Prior Affect Generalization?

Read PFNs, TabPFN, Mitra, and TabForestPFN. Compare the kinds of generated relationships and decision boundaries, then ask which real-data properties are represented or missing.

### How Can a Model Transfer Across Schemas?

Read TransTab, XTab, UniTabE, CM2, and CARTE. Track which parameters are shared and whether target-specific components need training.

### How Is Labeled Context Processed Efficiently?

Read TabICL, TabDPT, Orion-MSP, Orion-Bix, TabICLv2, and TabDPT-Turbo. Distinguish attention savings from context subsampling, retrieval, caching, and batching.

### When Do Feature Names and Text Values Help?

Compare TabLLM, TabuLa-8B, ConTextTab, and TabSTAR. Check whether the experiment supplies meaningful names, text fields, and target semantics to each baseline.

### Should a Frozen Model Be Adapted?

Read Exploring Fine-Tuning, Active In-Context Learning, and TabFM-Auto. Separate changes to model weights, context examples, and the surrounding pipeline.

### Which Results Should Be Trusted?

Read TabZilla and TabReD for historical evaluation issues, TabArena and TabRepo for configuration and budget comparisons, and the 2026 reliability and generalization studies for additional failure modes.

## A Practical First Comparison

Choose one synthetic-prior model and one real-data or semantic model that fit your task. Add tuned boosted trees and a simple baseline. Keep the same splits, feature access, and target-label budget.

Record the checkpoint and all preprocessing before running the experiment. Use the [evaluation guide](evaluation.md) to document the comparison. This repository does not provide reproduced scores.

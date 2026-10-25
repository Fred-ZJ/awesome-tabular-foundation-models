# Model Guide

[Back to the list](../README.md)

This is a qualitative map, not a leaderboard. Each row describes the linked work or generation; later checkpoints and wrappers can change the behavior.

**C** means classification. **R** means regression. Listed prediction coverage does not imply support for every label type, dataset size, or deployment setting.

| Family or work | Main source of reuse | Target-task mechanism | Prediction focus | Distinguishing idea |
| --- | --- | --- | --- | --- |
| [TabPFN v1](https://arxiv.org/abs/2207.01848) | Synthetic task priors | Labeled context; frozen predictor | C | Prior-data fitted prediction on small tables |
| [TabPFN v2 and later reports](https://www.nature.com/articles/s41586-024-08328-6) | Synthetic task priors | ICL; adaptation options depend on release | C, R | Broader task coverage and subsequent scaling work |
| [TabICL / TabICLv2](https://arxiv.org/abs/2602.11139) | Synthetic task priors | Labeled context | v1: C; v2: C, R | Column and row representations with efficient context processing |
| [Mitra / Mitra-v2](https://arxiv.org/abs/2609.04540) | Mixtures of synthetic task priors | ICL; optional adaptation in releases | C, R | Diversity of pretraining tasks |
| [TabDPT](https://arxiv.org/abs/2410.18164) | Real-table pretraining | Retrieval-based context | C, R | Transfer from real datasets through in-context prediction |
| [XTab](https://proceedings.mlr.press/v202/zhu23k.html) | Cross-table pretraining | Target-task fine-tuning | C, R experiments | Shared transformer with table-specific components |
| [CARTE](https://proceedings.mlr.press/v235/kim24d.html) | Knowledge-graph pretraining | Transfer and fine-tuning | C, R | Row graphs and semantic representations |
| [TabuLa-8B](https://arxiv.org/abs/2406.12031) | Language model adapted across table tasks | Serialized task context | Tabular prediction tasks | Language modeling as the transfer interface |
| [ConTextTab](https://arxiv.org/abs/2506.10707) | Real tables and semantic encodings | Labeled context | C, R | Uses semantics within a table-focused ICL model |
| [TabSTAR](https://arxiv.org/abs/2505.18125) | Cross-dataset semantic pretraining | Target-task adaptation | C, R | Target-aware representations for text-containing tables |
| [HyperFast](https://arxiv.org/abs/2402.14335) | Meta-training across tasks | Generates classifier weights | C | Hypernetwork produces a task-specific predictor |
| [LimiX](https://arxiv.org/abs/2509.03505) | Joint structured-data modeling | Context-conditioned queries | Conditional prediction tasks | Models variables and missingness through a unified interface |
| [Orion-MSP / Orion-Bix](https://arxiv.org/abs/2512.00181) | Task-level pretraining | Labeled context | Tabular prediction | Sparse or bi-axial attention designs |
| [TabFM](https://arxiv.org/abs/2609.37959) | Synthetic task pretraining | Labeled context | C, R | Pretrained prediction with calibration and ensemble variants |

## Compare Configurations Explicitly

The following are different experimental configurations even when they share a model name:

- A single frozen checkpoint.
- A checkpoint with input transformations or prediction ensembling.
- A model using retrieved or subsampled context.
- A fine-tuned model or adapter.
- A distilled model.
- An AutoML system containing the model.
- A pipeline revised using repeated validation feedback.

Report each configuration separately, including its feature access, label use, hardware, and total budget.

## Choosing What to Try

For numeric and categorical tables, begin with task and resource compatibility. For tables containing meaningful text, include a semantic method and specify how competing systems access the same text.

For large tables, inspect context construction, memory requirements, and batching in the exact implementation. A published row count may rely on retrieval, aggregation, or other settings that differ from your experiment.

Check current model cards and release terms before deployment. This guide intentionally omits static parameter counts, row limits, and licensing labels that can become misleading across versions.

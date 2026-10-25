# Evaluation Guide

[Back to the list](../README.md)

This guide is an experiment checklist. It does not claim that any model or benchmark in the list has been independently reproduced here.

## Data Provenance and Overlap

Record the dataset origin, version, target, feature schema, and preprocessing. For models pretrained on real tables or web corpora, check for dataset duplicates, transformed copies, and derived tasks shared with evaluation.

For synthetic-only pretraining, distinguish absence of real-table pretraining overlap from other risks: benchmark-informed prior design, repeated model selection, and test-set reuse can still affect an evaluation.

Preserve a record of which benchmark datasets informed development. The TabuLa-8B re-evaluation in [The Illusion of Generalization](https://arxiv.org/abs/2602.04031) is useful for thinking about task definitions and baseline strength; its findings should not be generalized to every TFM.

## Splits and Information Access

Use the split that matches deployment. Random IID splits, time splits, group splits, and geographic shifts answer different questions.

Fit imputers, encoders, feature selection, and scaling only on the permitted training portion. Do not expose held-out labels through serialization, retrieval, preprocessing, or context construction.

Record whether prediction is inductive or transductive: some configurations process multiple query rows together or use unlabeled query features. Make that access explicit.

See [TabReD](https://arxiv.org/abs/2406.19380) for time-dependent settings and [Beyond IID](https://arxiv.org/abs/2606.30410) for a broader range of dataset regimes.

## Context and Adaptation

For each model, report:

- The labeled context pool and the number of target labels available.
- Selection, retrieval, subsampling, ordering, and class balancing.
- Whether context is shared or selected separately for each query.
- All target-task gradient updates, adapters, or generated model components.
- Validation-driven choices of transformations, seeds, checkpoints, and ensembles.

A model described as zero-shot may still read labeled training examples. Report weight updates and labeled context separately.

## Fair Baselines and Budgets

Include well-tuned boosted trees and a simple baseline. Include neural baselines when they help answer the research question. Give methods compatible feature information, especially when semantic models see feature names or text.

Measure the complete configuration. Separate data preparation, context construction, fine-tuning, validation search, and prediction. Report cold-start costs as well as repeated prediction when caching matters.

Record wall-clock time, hardware, peak memory, ensemble size, number of trials, and tuning budget. Distinguish one-time pretraining cost from target-task cost.

[TabArena](https://arxiv.org/abs/2506.16791) and [TabRepo](https://arxiv.org/abs/2311.02971) help frame comparisons involving configurations, tuning, and ensembles. A changing leaderboard needs a dated snapshot.

## Metrics and Uncertainty

Use metrics appropriate for the target: for example, discrimination and log loss for classification, and error metrics for regression. Avoid collapsing every task into a single number without explaining normalization and aggregation.

Report uncertainty across datasets and repeated splits. State the treatment of missing runs, timeouts, failed configurations, and ties.

When probabilistic predictions matter, include calibration, predictive distribution quality, and interval coverage and width. Evaluate relevant subgroups. [TabReliBench](https://arxiv.org/abs/2610.13654) focuses on these distinctions.

For deployment under shift, test the expected shift directly. The [OOD evaluation study](https://arxiv.org/abs/2607.26000) provides examples; its dataset coverage is a bounded empirical study.

## Versioned Experiment Record

| Field | What to record |
| --- | --- |
| Data | Source, immutable version or hash, target definition, and split IDs |
| Model | Repository commit, package version, checkpoint ID and hash |
| Access | Training labels, validation labels, feature semantics, and query-feature visibility |
| Pipeline | Preprocessing, context selection, fine-tuning, ensembling, and postprocessing |
| Search | Trials, feedback rounds, validation objective, and stopping rule |
| Resources | Hardware, runtime breakdown, memory, and batch size |
| Results | Per-dataset metrics, uncertainty, failures, and aggregation method |
| Release terms | Separate code, weights, and data licenses or access requirements |

For agent-optimized pipelines, count every validation-guided revision in the budget. Use a final untouched evaluation split after selecting the pipeline.

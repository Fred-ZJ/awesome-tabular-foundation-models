# Awesome Tabular Foundation Models [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of papers, models, benchmarks, and resources for tabular foundation models.

The focus is **prediction on tabular data**: models pretrained or meta-trained across tasks and reused on a new table. This includes prior-data fitted networks, cross-table transfer, semantic models, adaptation, and evaluation. Table question answering and general-purpose tabular deep learning are outside the core scope.

Start with the [reading guide](docs/reading-guide.md), compare the [model families](docs/model-guide.md), or consult the [evaluation guide](docs/evaluation.md).

**41 curated papers and reports** across 9 categories. Initial curation checked on **2026-10-25**. Formal publication years are used when confirmed; otherwise entries are explicitly labeled as preprints or technical reports. The list is selective and does not rank models.

## Contents

- [Surveys](#surveys)
- [Foundations and Prior-Data Fitted Networks](#foundations-and-prior-data-fitted-networks)
- [Synthetic-Prior Pretraining and Scalable In-Context Learning](#synthetic-prior-pretraining-and-scalable-in-context-learning)
- [Real-Data and Cross-Table Pretraining](#real-data-and-cross-table-pretraining)
- [Semantic and Language-Model-Based Prediction](#semantic-and-language-model-based-prediction)
- [Alternative and Unified Architectures](#alternative-and-unified-architectures)
- [Adaptation, Context Selection, and Pipelines](#adaptation-context-selection-and-pipelines)
- [Benchmarks and Evaluation](#benchmarks-and-evaluation)
- [Pretraining Corpora](#pretraining-corpora)
- [Implementations and Model Releases](#implementations-and-model-releases)
- [Benchmark Software and Data Resources](#benchmark-software-and-data-resources)
- [Guides](#guides)
- [Contributing](#contributing)
- [License](#license)

## Surveys

Overviews focused on pretrained models for tabular prediction.

- [The Current Generation of Tabular Foundation Models: A Critical Review](https://www.mdpi.com/2504-4990/8/8/244) - **Machine Learning and Knowledge Extraction 2026**. Reviews model families, pretraining regimes, deployment choices, and limitations of the current TFM literature.

## Foundations and Prior-Data Fitted Networks

The ideas behind learning a predictor across tasks before applying it to a new table.

- [Transformers Can Do Bayesian Inference](https://arxiv.org/abs/2112.10510) - **ICLR 2022**. Introduces prior-data fitted networks that learn to approximate posterior prediction from datasets sampled from a prior. First preprint: 2021.
- [TabPFN: A Transformer That Solves Small Tabular Classification Problems in a Second](https://arxiv.org/abs/2207.01848) - **ICLR 2023**. Uses synthetic prior training to predict small classification datasets from labeled context without target-specific weight updates. First preprint: 2022.
- [Accurate predictions on small data with a tabular foundation model](https://www.nature.com/articles/s41586-024-08328-6) - **Nature 2025**. Extends the TabPFN approach to classification and regression using a pretrained predictor conditioned on the target dataset.

## Synthetic-Prior Pretraining and Scalable In-Context Learning

Models trained on generated tasks, with work on prior diversity, architecture, and inference efficiency.

- [TabICL: A Tabular Foundation Model for In-Context Learning on Large Data](https://arxiv.org/abs/2502.05564) - **ICML 2025**. Combines column and row representations with efficient in-context learning for tabular classification.
- [Mitra: Mixed Synthetic Priors for Enhancing Tabular Foundation Models](https://arxiv.org/abs/2510.21204) - **NeurIPS 2025**. Studies a curated mixture of synthetic task generators for pretrained classification and regression.
- [TabPFN-2.5: Advancing the State of the Art in Tabular Foundation Models](https://arxiv.org/abs/2511.08667) - **Technical report (arXiv) 2025**. Reports a new TabPFN generation with expanded synthetic priors, larger supported tasks, and adaptation options.
- [TabICLv2: A better, faster, scalable, and open tabular foundation model](https://arxiv.org/abs/2602.11139) - **ICML 2026**. Expands TabICL with classification and regression, revised synthetic task generation, and more efficient training and inference.
- [TabPFN-3: Technical Report](https://arxiv.org/abs/2605.13986) - **Technical report (arXiv) 2026**. Describes changes to TabPFN pretraining and inference, alongside extensions to additional data settings.
- [Mitra-v2 Technical Report](https://arxiv.org/abs/2609.04540) - **Technical report (arXiv) 2026**. Expands synthetic pretraining diversity and context capacity for classification and regression.
- [TabPFN-3.5: Technical Report](https://arxiv.org/abs/2609.17895) - **Technical report (arXiv) 2026**. Reports the next TabPFN release and evaluates its behavior across standard and more varied tabular tasks.
- [TabFM: A Zero-Shot Foundation Model for Tabular Data](https://arxiv.org/abs/2609.37959) - **arXiv preprint 2026**. Uses synthetic task pretraining for tabular in-context prediction and studies calibration and ensembling.

## Real-Data and Cross-Table Pretraining

Transfer across heterogeneous tables, including real-data pretraining and knowledge-graph-based representations.

- [TransTab: Learning Transferable Tabular Transformers Across Tables](https://arxiv.org/abs/2205.09328) - **NeurIPS 2022**. Builds transferable representations across tables with changing or partially overlapping feature schemas.
- [XTab: Cross-table Pretraining for Tabular Transformers](https://proceedings.mlr.press/v202/zhu23k.html) - **ICML 2023**. Pretrains shared transformer components across heterogeneous datasets using table-specific input and output components.
- [UniTabE: A Universal Pretraining Protocol for Tabular Foundation Model in Data Science](https://arxiv.org/abs/2307.09249) - **ICLR 2024**. Uses a unified table representation and pretraining protocol to support transfer across schemas and downstream tasks. First preprint: 2023.
- [Towards Cross-Table Masked Pretraining for Web Data Mining](https://arxiv.org/abs/2307.04308) - **The Web Conference 2024**. Introduces CM2, combining semantic column representations with masked pretraining across web tables. First preprint: 2023.
- [CARTE: Pretraining and Transfer for Tabular Learning](https://proceedings.mlr.press/v235/kim24d.html) - **ICML 2024**. Represents rows as graphs and transfers knowledge-graph-pretrained representations to heterogeneous tabular tasks.
- [TabDPT: Scaling Tabular Foundation Models on Real Data](https://arxiv.org/abs/2410.18164) - **NeurIPS 2025**. Pretrains on real tables and uses retrieved examples as context for prediction on a new dataset. First preprint: 2024.
- [TabDPT-Turbo: Efficient In-Context Learning for Tabular Prediction](https://arxiv.org/abs/2608.01400) - **arXiv preprint 2026**. Studies row-based attention and longer-context real-data pretraining to improve in-context prediction efficiency.

## Semantic and Language-Model-Based Prediction

Models that use feature names, text values, or language pretraining. General LLM approaches are marked as adjacent work.

- [TabLLM: Few-shot Classification of Tabular Data with Large Language Models](https://proceedings.mlr.press/v206/hegselmann23a.html) - **AISTATS 2023**. An adjacent LLM approach that serializes table rows into text for few-shot classification.
- [Large Scale Transfer Learning for Tabular Data via Language Modeling](https://arxiv.org/abs/2406.12031) - **NeurIPS 2024**. Introduces TabuLa-8B and transfers language-model pretraining to tabular prediction through a large collection of table tasks.
- [TabSTAR: A Tabular Foundation Model for Tabular Data with Text Fields](https://arxiv.org/abs/2505.18125) - **NeurIPS 2025**. Learns target-aware semantic representations for text-containing tables through cross-dataset pretraining and downstream adaptation.
- [ConTextTab: A Semantics-Aware Tabular In-Context Learner](https://arxiv.org/abs/2506.10707) - **NeurIPS 2025**. Combines real-table pretraining and semantic representations to condition tabular predictions on labeled examples.

## Alternative and Unified Architectures

Complementary mechanisms, including generated classifier weights, conditional distribution modeling, and attention design.

- [HyperFast: Instant Classification for Tabular Data](https://arxiv.org/abs/2402.14335) - **AAAI 2024**. Meta-trains a hypernetwork that generates a task-specific classifier, providing an alternative to direct in-context prediction.
- [LimiX: Unleashing Structured-Data Modeling Capability for Generalist Intelligence](https://arxiv.org/abs/2509.03505) - **Technical report (arXiv) 2025**. Models variables and missingness jointly to answer different conditional prediction queries with a shared structured-data model.
- [Orion-MSP: Multi-Scale Sparse Attention for Tabular In-Context Learning](https://arxiv.org/abs/2511.02818) - **arXiv preprint 2025**. Combines multi-scale sparse attention with memory compression for tabular context processing.
- [Orion-Bix: Bi-Axial Attention for Tabular In-Context Learning](https://arxiv.org/abs/2512.00181) - **The Web Conference 2026**. Uses attention across rows and features to integrate local and global information for tabular in-context prediction. First preprint: 2025.
- [LimiX-2M: Mitigating Low-Rank Collapse and Attention Bottlenecks in Tabular Foundation Models](https://arxiv.org/abs/2606.04485) - **ICML 2026**. Revises feature tokenization and attention order to improve representation capacity and computational efficiency.

## Adaptation, Context Selection, and Pipelines

How pretrained predictors are adapted, supplied with context, and integrated into larger workflows.

- [Fine-tuned In-Context Learning Transformers are Excellent Tabular Data Classifiers](https://arxiv.org/abs/2405.13396) - **arXiv preprint 2024**. Introduces TabForestPFN and studies forest-based synthetic priors together with target-dataset fine-tuning.
- [Exploring Fine-Tuning for Tabular Foundation Models](https://arxiv.org/abs/2601.09654) - **arXiv preprint 2026**. Compares adaptation strategies and investigates when fine-tuning helps or harms tabular foundation models.
- [Active In-Context Learning for Tabular Foundation Models](https://arxiv.org/abs/2603.27385) - **arXiv preprint 2026**. Studies active acquisition of labeled examples to construct more useful in-context learning sets.
- [TabFM-Auto: Self-Evolving Pipelines for Tabular Foundation Models](https://arxiv.org/abs/2609.37989) - **arXiv preprint 2026**. Uses an LLM agent and validation feedback to revise data preparation, feature engineering, context selection, and postprocessing around TabFM.

## Benchmarks and Evaluation

Resources for comparing accuracy, budgets, generalization, and predictive reliability.

- [When Do Neural Nets Outperform Boosted Trees on Tabular Data?](https://arxiv.org/abs/2305.02997) - **NeurIPS Datasets and Benchmarks 2023**. Introduces TabZilla and analyzes dataset-dependent differences between neural networks and boosted trees.
- [TabRepo: A Large Scale Repository of Tabular Model Evaluations and its AutoML Applications](https://arxiv.org/abs/2311.02971) - **arXiv preprint 2023**. Provides cached predictions and evaluations for analyzing model selection, tuning, and ensembles.
- [TabReD: Analyzing Pitfalls and Filling the Gaps in Tabular Deep Learning Benchmarks](https://arxiv.org/abs/2406.19380) - **ICLR 2025**. Examines gaps in existing benchmarks, including time-dependent data and the role of feature engineering. First preprint: 2024.
- [TabArena: A Living Benchmark for Machine Learning on Tabular Data](https://arxiv.org/abs/2506.16791) - **NeurIPS Datasets and Benchmarks 2025**. Provides a maintained benchmarking system with explicit model configurations, tuning, and ensembling comparisons.
- [The Illusion of Generalization in Tabular Language Models](https://arxiv.org/abs/2602.04031) - **arXiv preprint 2026**. Re-evaluates TabuLa-8B and investigates task construction, baseline strength, and contamination in tabular language-model evaluation.
- [Beyond IID: How General Are Tabular Foundation Models, Really?](https://arxiv.org/abs/2606.30410) - **arXiv preprint 2026**. Introduces BeyondArena to compare performance across tabular regimes extending beyond conventional IID benchmarks.
- [Empirical Evaluation of Out-Of-Distribution Performance of Tabular Foundation Models](https://arxiv.org/abs/2607.26000) - **arXiv preprint 2026**. Evaluates selected TFMs under label, social, and geographic distribution shifts.
- [TabReliBench: Evaluating Tabular Foundation Models Beyond Predictive Accuracy](https://arxiv.org/abs/2610.13654) - **arXiv preprint 2026**. Examines distributional predictions, calibration, subgroup coverage, and interval efficiency alongside point accuracy.

## Pretraining Corpora

Data resources relevant to transfer, provenance, and contamination analysis.

- [TabLib: A Dataset of 627M Tables with Context](https://arxiv.org/abs/2310.07875) - **arXiv preprint 2023**. Collects tables and surrounding context from web and code sources for large-scale table research.

## Implementations and Model Releases

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

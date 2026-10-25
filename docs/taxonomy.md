# Taxonomy

[Back to the list](../README.md)

## What Counts as a Tabular Foundation Model?

This list uses a practical inclusion rule: a model learns reusable predictive knowledge across tasks, tables, or a distribution of generated datasets, then applies it to a new tabular problem.

A large parameter count is not required. A transformer trained from scratch independently on every dataset is not a foundation model under this rule. General LLM methods are included as adjacent work when their contribution concerns tabular prediction.

## Three Independent Axes

| Axis | Main choices | Questions to ask |
| --- | --- | --- |
| Pretraining data | Synthetic tasks; real tables; knowledge graphs; language and table mixtures | What transferable information is learned, and where could evaluation overlap arise? |
| Target-task adaptation | Frozen in-context prediction; weight fine-tuning; generated task-specific weights; combinations | Which target labels are consumed, and what changes at deployment? |
| Representation | Numeric or categorical values; row and column attention; graph encodings; semantic text embeddings | Are feature names and text values available and used? |

These axes overlap. Semantic input encoding is compatible with either synthetic or real-data pretraining. An in-context model can also offer an optional fine-tuning mode.

## Main Mechanisms

### Synthetic-Prior Pretraining

The training system repeatedly samples a dataset-generating process and trains a predictor to infer withheld labels from an observed context. The learned prior influences which relationships are easy to recover.

Examples include [PFNs](https://arxiv.org/abs/2112.10510), [TabPFN](https://arxiv.org/abs/2207.01848), [TabICL](https://arxiv.org/abs/2502.05564), and [Mitra](https://arxiv.org/abs/2510.21204). Useful distinctions include generator diversity, treatment of categorical data, attention structure, and context capacity.

### Real-Data and Cross-Table Pretraining

The model transfers information learned from existing tables. Variable schemas make representation and task construction central design choices.

[TransTab](https://arxiv.org/abs/2205.09328) and [XTab](https://proceedings.mlr.press/v202/zhu23k.html) study cross-table transfer. [TabDPT](https://arxiv.org/abs/2410.18164) uses real-data pretraining for in-context prediction. [CARTE](https://proceedings.mlr.press/v235/kim24d.html) is a related route that transfers graph representations pretrained on background knowledge.

### Semantic and Language-Based Prediction

Feature names, target descriptions, and text values can carry useful information beyond numeric patterns. [TabLLM](https://proceedings.mlr.press/v206/hegselmann23a.html) applies an LLM to serialized rows; [TabuLa-8B](https://arxiv.org/abs/2406.12031) trains for transfer across tabular prediction tasks.

[ConTextTab](https://arxiv.org/abs/2506.10707) and [TabSTAR](https://arxiv.org/abs/2505.18125) use semantics in table-focused models. They should not be treated as interchangeable with generic prompting.

### Other Forms of Reuse

[HyperFast](https://arxiv.org/abs/2402.14335) generates classifier weights through a meta-trained hypernetwork. [LimiX](https://arxiv.org/abs/2509.03505) frames structured-data tasks through conditional distribution queries. These mechanisms broaden the space beyond a single frozen predictor architecture.

## Terminology That Needs Care

- **In-context learning:** labeled target-task examples enter the model's context. The base weights can stay fixed.
- **Zero-shot across datasets:** a model may require no gradient updates on the new dataset while still consuming its labeled training rows. State the exact meaning used by each paper.
- **Fine-tuning:** target data update model weights. Report whether tuning changes the full model, adapters, or another component.
- **Retrieval:** context examples are selected from an allowed pool. This is a data access decision even if no model weights change.
- **Foundation model versus AutoML system:** a pretrained model can be one component of an ensemble or search workflow. Compare the complete deployed configuration.
- **Open release:** code, weights, training data, and hosted access are separate questions. Inspect their individual terms.

## Scope Boundaries

The core list emphasizes supervised classification and regression. General table question answering, spreadsheet agents, SQL generation, and standalone synthetic-row generators are outside this scope.

Trees, linear models, and neural models trained from scratch remain important evaluation baselines. Their usefulness does not depend on being called foundation models.

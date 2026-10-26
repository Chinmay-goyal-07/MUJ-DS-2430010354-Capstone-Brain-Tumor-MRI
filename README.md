# Brain Tumor MRI Classification using CNN

Deep-learning classifier that labels brain MRI scans as **glioma**, **meningioma**, **pituitary** or **notumor**, using transfer learning (ImageNet-pretrained ResNet18) with 5-fold cross-validation and early stopping.

> **Disclaimer:** Educational capstone project. Not a medical device; do not use for diagnosis.

## Team

| Name | Registration No. | GitHub Username | Role |
|---|---|---|---|
| ____________________ | ____________________ | ____________________ | ____________________ |
| ____________________ | ____________________ | ____________________ | ____________________ |
| ____________________ | ____________________ | ____________________ | ____________________ |
| ____________________ | ____________________ | ____________________ | ____________________ |

**Team name:** ____________________  |  **Batch:** F  |  **Instructor:** ____________________

## Results at a glance

| Metric | Value |
|---|---|
| Test accuracy (1,600 unseen images) | **95.37%** |
| Best cross-validation validation accuracy | 99.73% |
| Macro F1 (test) | 0.953 |
| Transformer (Swin-T) test accuracy | 95.37% (ties with the CNN) |
| Weakest class | glioma (recall about 0.83 for both models) |

Full reports: [CNN](results/classification_report.txt), [transformer](results/classification_report_transformer.txt) and [docs/PROJECT_REPORT.md](docs/PROJECT_REPORT.md).

## Repository layout

```
.
├── README.md
├── requirements.txt
├── notebooks/brain_tumor_cnn.ipynb          # CNN (ResNet18) training + evaluation (Colab, GPU)
├── notebooks/brain_tumor_transformer.ipynb  # Transformer (Swin-T / ViT-B/16), same pipeline
├── code/predict.py                   # single-image inference script
├── docs/                             # installation guide, report, workflow, issues plan, contributions
├── results/                          # metrics, training curves, confusion matrix
├── screenshots/                      # screenshots for the report/presentation
├── presentations/                    # final slides
└── .github/                          # issue templates + pull request template
```

## Quick start

```bash
git clone https://github.com/____________________/____________________.git
cd ____________________
pip install -r requirements.txt
python code/predict.py --image path/to/mri.jpg --checkpoint best_model.pt
```

Training steps and dataset layout: [docs/INSTALLATION.md](docs/INSTALLATION.md).

## Documentation

| Document | Purpose |
|---|---|
| [docs/INSTALLATION.md](docs/INSTALLATION.md) | Setup, dataset layout, training, inference |
| [docs/PROJECT_REPORT.md](docs/PROJECT_REPORT.md) | Problem, data, method, results, limitations |
| [docs/TRANSFORMER_MODEL.md](docs/TRANSFORMER_MODEL.md) | Transformer model, settings and CNN-vs-transformer comparison table |
| [docs/GITHUB_WORKFLOW.md](docs/GITHUB_WORKFLOW.md) | Branching, pull requests, reviews |
| [docs/ISSUES_PLAN.md](docs/ISSUES_PLAN.md) | Ready-to-create GitHub issues |
| [docs/CONTRIBUTIONS.md](docs/CONTRIBUTIONS.md) | Per-member contribution log |
| [docs/SUBMISSION_CHECKLIST.md](docs/SUBMISSION_CHECKLIST.md) | Final submission checklist |

## Links

- Presentation: [presentations/](presentations/)
- Personal repositories: see [docs/CONTRIBUTIONS.md](docs/CONTRIBUTIONS.md)

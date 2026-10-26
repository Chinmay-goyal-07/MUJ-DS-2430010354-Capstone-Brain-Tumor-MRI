# Results

Test-set results for the two models trained in this project, evaluated on the same 1,600 unseen images (400 per class).

## Files in this folder

| File | Description |
|---|---|
| `classification_report.txt` | ResNet18 (CNN): precision, recall and F1 per class |
| `classification_report_transformer.txt` | Swin-T (transformer): precision, recall and F1 per class |
| `training_curves.png` | ResNet18 loss and accuracy per epoch (best fold) |
| `confusion_matrix.png` | ResNet18 confusion matrix on the test set |
| `training_curves_transformer.png` | Swin-T loss and accuracy per epoch (best fold) |
| `confusion_matrix_transformer.png` | Swin-T confusion matrix on the test set |

The `.png` files are produced by the notebooks. Download them from Colab and add them to this folder.

## Summary

| Metric | ResNet18 (CNN) | Swin-T (Transformer) |
|---|---|---|
| Test accuracy | 0.9537 | 0.9537 |
| Macro F1 | 0.953 | 0.953 |
| Best validation accuracy (5-fold CV) | 0.9973 | ____________________ |
| Parameters | about 11M | about 28M |
| Training time | ____________________ | ____________________ |

## Per-class results (test set)

| Class | ResNet18 precision | ResNet18 recall | Swin-T precision | Swin-T recall |
|---|---|---|---|---|
| glioma | 1.000 | 0.830 | 1.000 | 0.835 |
| meningioma | 0.908 | 0.985 | 0.893 | 0.980 |
| notumor | 0.930 | 1.000 | 0.957 | 1.000 |
| pituitary | 0.990 | 1.000 | 0.978 | 1.000 |

## Figures

### ResNet18
![ResNet18 training curves](training_curves.png)
![ResNet18 confusion matrix](confusion_matrix.png)

### Swin-T
![Swin-T training curves](training_curves_transformer.png)
![Swin-T confusion matrix](confusion_matrix_transformer.png)

## Key findings

- Both models reach the same test accuracy (95.37%, 1,526 of 1,600 images correct). The data does not show either to be better.
- Pituitary and no-tumor scans are classified almost perfectly (recall 1.000 for both).
- Glioma is the weak class for both models: precision is 1.000 but recall is about 0.83, so roughly one in six gliomas is labelled as another class and no other class is mistaken for glioma.
- Validation accuracy (up to 99.7%) is higher than test accuracy (95.4%). The validation figure is also the best over folds and epochs, so it is optimistic. The test accuracy is the number to report.

See [../docs/PROJECT_REPORT.md](../docs/PROJECT_REPORT.md) and [../docs/TRANSFORMER_MODEL.md](../docs/TRANSFORMER_MODEL.md) for the full discussion.

## How to reproduce

1. Run `notebooks/brain_tumor_cnn.ipynb` and `notebooks/brain_tumor_transformer.ipynb` on a GPU, following [../docs/INSTALLATION.md](../docs/INSTALLATION.md).
2. Download the generated `.png` and `classification_report*.txt` files.
3. Put them in this folder and commit them.

Each model was trained once with a fixed random seed for the fold split (42); results may vary slightly between runs.

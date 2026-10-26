# Project Report: Brain Tumor MRI Classification using CNN

**Team:** ____________________  |  **Batch:** F  |  **Date:** ____________________

## 1. Problem statement

Brain tumors are diagnosed from MRI, a slow process that needs specialist review. This project builds an image classifier that assigns an MRI slice to one of four categories: **glioma**, **meningioma**, **pituitary tumor**, or **no tumor**. It is a learning project and not a clinical tool.

## 2. Dataset

| Split | Per class | Total |
|---|---|---|
| Training | 1,400 | 5,600 |
| Testing | 400 | 1,600 |

Classes: glioma, meningioma, notumor, pituitary (perfectly balanced). Source: Kaggle, tombackert/brain-tumor-mri-data (https://www.kaggle.com/datasets/tombackert/brain-tumor-mri-data). Licence: ____________________

## 3. Method

**Preprocessing:** convert to grayscale then replicate to 3 channels, resize to 224x224, normalise with ImageNet mean/std.

**Augmentation (training only):** horizontal flip (p=0.3), rotation up to 10 degrees, brightness and contrast jitter of 0.15.

**Model:** ImageNet-pretrained **ResNet18** with its final layer replaced by `Dropout(0.3)` followed by `Linear(512, 4)`. (`efficientnet_b0` is available as an alternative backbone.)

**Training:**

| Item | Value |
|---|---|
| Optimiser | AdamW (lr 3e-4, weight decay 1e-4) |
| Loss | Cross-entropy |
| LR schedule | ReduceLROnPlateau on validation accuracy (factor 0.5, patience 2) |
| Epochs | up to 15 |
| Early stopping | patience 3 on validation loss |
| Validation | 5-fold cross-validation on the training set (shuffled, seed 42) |
| Model selection | Weights from the epoch with the highest validation accuracy across all folds |
| Batch size | 32 |

## 4. Results

On the 1,600-image held-out test set:

| Class | Precision | Recall | F1 | Support |
|---|---|---|---|---|
| glioma | 1.000 | 0.830 | 0.907 | 400 |
| meningioma | 0.908 | 0.985 | 0.945 | 400 |
| notumor | 0.930 | 1.000 | 0.964 | 400 |
| pituitary | 0.990 | 1.000 | 0.995 | 400 |
| **Accuracy** | | | **0.954** | 1,600 |
| Macro avg | 0.957 | 0.954 | 0.953 | 1,600 |

The best validation accuracy across the five folds was **0.9973**.

Figures (add after exporting from the notebook): `results/training_curves.png`, `results/confusion_matrix.png`.

## 5. Discussion

- **Pituitary and notumor** are classified almost perfectly (recall 1.000).
- **Glioma is the weak spot:** precision is 1.000 but recall is 0.830, so about 68 of 400 gliomas were labelled as another class and no other class was mistaken for glioma. From the per-class precision values, those errors fall on meningioma and notumor. For a tumor-detection task, missed tumors are the costly error type.
- **Validation vs test gap:** validation accuracy (up to 99.73%) is noticeably higher than test accuracy (95.37%). The 99.73% figure is also the maximum over folds and epochs, so it is optimistic. Possible reasons to investigate: the test set may differ in distribution from the training set, or near-duplicate or same-patient slices may be shared across training folds.

## 5a. Model comparison: CNN vs transformer

| Metric (test set, 1,600 images) | ResNet18 | Transformer (Swin-T) |
|---|---|---|
| Accuracy | 0.9537 | 0.9537 |
| Macro F1 | 0.953 | 0.953 |
| Glioma recall | 0.830 | 0.835 |
| Meningioma recall | 0.985 | 0.980 |

The two models tie on accuracy and share the same glioma weakness (precision 1.000, recall about 0.83). Details and the full table are in [TRANSFORMER_MODEL.md](TRANSFORMER_MODEL.md).

## 6. Limitations

- 2D slices only; no patient-level split is documented, so slices from one patient may appear in both train and validation folds.
- Single dataset, no external validation.
- No explainability (e.g. Grad-CAM) yet, so the model's focus regions are unverified.
- Not clinically validated.

## 7. Future work

1. Improve glioma recall (class-weighted loss, stronger augmentation, try `efficientnet_b0`, fine-tune with a lower learning rate).
2. Add Grad-CAM heatmaps to check the model attends to the tumor region.
3. Confirm train/validation splitting is by patient where IDs are available.
4. Deploy a simple Gradio or Streamlit demo for image upload.
5. Compare backbones with a table of accuracy, recall per class, and training time.

## 8. Team contributions

See [CONTRIBUTIONS.md](CONTRIBUTIONS.md).

## 9. References

- He et al., *Deep Residual Learning for Image Recognition*, CVPR 2016.
- Tan & Le, *EfficientNet*, ICML 2019.
- PyTorch torchvision models: https://pytorch.org/vision/stable/models.html
- Dataset: Kaggle, tombackert/brain-tumor-mri-data, https://www.kaggle.com/datasets/tombackert/brain-tumor-mri-data

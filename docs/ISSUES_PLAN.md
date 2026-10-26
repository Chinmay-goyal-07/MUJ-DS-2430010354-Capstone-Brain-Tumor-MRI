# Issues Plan

Create these in GitHub Issues and assign each to a team member. Adjust or split as needed. Mark an item done only when its linked pull request is merged.

| # | Title | Label | Assignee |
|---|---|---|---|
| 1 | Dataset collection and verification | `data` | ____________________ |
| 2 | Preprocessing and augmentation pipeline | `data`, `model` | ____________________ |
| 3 | Model development: ResNet18 transfer learning | `model` | ____________________ |
| 4 | 5-fold cross-validation and early stopping | `model` | ____________________ |
| 5 | Evaluation: classification report and confusion matrix | `model`, `testing` | ____________________ |
| 6 | Testing: inference script and sanity checks | `testing` | ____________________ |
| 7 | Improve glioma recall | `enhancement`, `model` | ____________________ |
| 8 | Deployment: Gradio/Streamlit demo | `deployment` | ____________________ |
| 9 | Documentation: README, report, installation guide | `documentation` | ____________________ |
| 10 | Presentation and screenshots | `documentation` | ____________________ |

## Details

### 1. Dataset collection and verification
- [ ] Download dataset and record source and licence in the README
- [ ] Verify folder layout (`Training/`, `Testing/`, four classes each)
- [ ] Confirm counts (1,400 / 400 per class) and check for corrupt or duplicate images

### 2. Preprocessing and augmentation pipeline
- [ ] Grayscale to 3 channels, resize to 224x224, ImageNet normalisation
- [ ] Augmentations: flip, rotation, brightness/contrast jitter
- [ ] Save sample augmented images to `screenshots/`

### 3. Model development: ResNet18 transfer learning
- [ ] Load pretrained ResNet18 and replace the final layer (Dropout 0.3 + Linear)
- [ ] Support `efficientnet_b0` as an alternative backbone

### 4. 5-fold cross-validation and early stopping
- [ ] KFold (5 splits, seed 42), AdamW, ReduceLROnPlateau
- [ ] Early stopping (patience 3); keep the best weights across folds
- [ ] Save training curves to `results/`

### 5. Evaluation
- [ ] Evaluate on the 1,600-image test set
- [ ] Export `classification_report.txt`, `confusion_matrix.png`, `training_curves.png` to `results/`

### 6. Testing
- [ ] Test `code/predict.py` on at least one image per class
- [ ] Check that the checkpoint loads on a CPU-only machine
- [ ] Record outcomes with screenshots

### 7. Improve glioma recall
- [ ] Inspect misclassified glioma images
- [ ] Try class weights, stronger augmentation, or a different backbone; report before/after recall

### 8. Deployment
- [ ] Build a small upload-and-predict app
- [ ] Add run instructions to `docs/INSTALLATION.md`

### 9. Documentation
- [ ] Finish README, `PROJECT_REPORT.md`, `INSTALLATION.md`
- [ ] Fill in `CONTRIBUTIONS.md`

### 10. Presentation and screenshots
- [ ] Finalise slides in `presentations/`
- [ ] Add demo screenshots to `screenshots/`

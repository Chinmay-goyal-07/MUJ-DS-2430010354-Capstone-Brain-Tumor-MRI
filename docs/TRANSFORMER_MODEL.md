# Transformer Model (Swin-T / ViT-B/16)

Notebook: `notebooks/brain_tumor_transformer.ipynb`. It is a copy of the CNN notebook with the model swapped for a Vision Transformer, so the two can be compared fairly (same data, same 5 folds, same early stopping, same test set).

## Models available

| Backbone | Type | Parameters | Notes |
|---|---|---|---|
| `swin_t` (default) | Shifted-window transformer | about 28M | Local attention windows; usually the better fit for small datasets |
| `vit_b_16` | Plain Vision Transformer | about 86M | Needs more GPU memory; may require `BATCH_SIZE = 16` |

Both start from ImageNet-pretrained weights (torchvision) and get a new head: `Dropout(0.3)` then `Linear(768, 4)`.

## How it works

1. The 224 x 224 image is cut into patches (16 x 16 for ViT-B/16; Swin-T uses 4 x 4 patches that are merged in stages).
2. Each patch becomes a vector (an embedding) with position information added.
3. **Self-attention** layers let every patch look at the other patches (Swin: patches inside a window, with windows shifted between layers), so the model can relate a tumor region to the rest of the brain.
4. The final feature vector goes through the new classification head to give four class scores; softmax turns them into probabilities.

## What differs from the CNN notebook

| Setting | CNN (ResNet18) | Transformer |
|---|---|---|
| Learning rate | 3e-4 | 1e-4 |
| Weight decay | 1e-4 | 0.05 |
| Epochs (max) | 15 | 10 |
| Extras | none | mixed precision (AMP), gradient clipping at 1.0 |
| Output files | `best_model.pt`, ... | `best_model_transformer.pt`, `*_transformer.png/.txt` (so CNN results are not overwritten) |

These transformer settings are common starting values for fine-tuning, **not tuned on this dataset**. Expect to adjust the learning rate if training is unstable or slow to improve.

## Running it

Same steps as `docs/INSTALLATION.md`: open the notebook in Colab with a GPU, upload the dataset zip, run all cells. Predict with:

```bash
python code/predict.py --image path/to/mri.jpg --checkpoint best_model_transformer.pt
```

## Results comparison (fill in after training)

| Metric | ResNet18 (CNN) | Swin-T | ViT-B/16 |
|---|---|---|---|
| Test accuracy | 0.9537 | 0.9537 | ____________________ |
| Macro F1 | 0.953 | 0.953 | ____________________ |
| Glioma recall | 0.830 | 0.835 | ____________________ |
| Meningioma recall | 0.985 | 0.980 | ____________________ |
| Notumor recall | 1.000 | 1.000 | ____________________ |
| Pituitary recall | 1.000 | 1.000 | ____________________ |
| Best validation accuracy | 0.9973 | ____________________ | ____________________ |
| Parameters | about 11M | about 28M | about 86M |
| Total training time | ____________________ | ____________________ | ____________________ |

**Note:** the Swin-T column assumes the default `swin_t` backbone was used; change the column heading if you ran `vit_b_16`. Fill in best validation accuracy and training time from your notebook output.

**Conclusion:** On this dataset the transformer and the CNN tie. Both reach 95.37% test accuracy (1,526 of 1,600 images) and a macro F1 of 0.953. The only differences are within about 8 images, which is within the noise of a single run on a 1,600-image test set, so the data does not show either model to be better. The Swin-T has about 2.5 times as many parameters as ResNet18 (about 28M versus 11M) for no gain in accuracy here. Both models share the same weakness: glioma precision is 1.000 but recall is about 0.83, meaning roughly one in six gliomas is labelled as another class (mostly meningioma, judging from the precision values) and no other class is mistaken for glioma. Because two different architectures fail in the same way, the cause is more likely in the data (for example a train/test distribution gap or near-duplicate slices across folds) than in the model type. Each model was trained once, so a repeat with different random seeds would be needed to claim a real difference.

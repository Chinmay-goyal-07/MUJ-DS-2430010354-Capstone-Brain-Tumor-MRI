# Installation & Usage Guide

## 1. Requirements

- Python 3.9+ 
- A GPU is strongly recommended for training (the notebook was run on a Google Colab Tesla T4; one epoch takes roughly 37 s there). Inference runs fine on CPU.

## 2. Get the code

```bash
git clone https://github.com/____________________/____________________.git
cd ____________________
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 3. Prepare the dataset

Dataset source: Kaggle, tombackert/brain-tumor-mri-data (https://www.kaggle.com/datasets/tombackert/brain-tumor-mri-data)

Download it and arrange it exactly like this (the notebook reads class names from folder names):

```
data/
├── Training/
│   ├── glioma/        (1,400 images)
│   ├── meningioma/    (1,400 images)
│   ├── notumor/       (1,400 images)
│   └── pituitary/     (1,400 images)
└── Testing/
    ├── glioma/        (400 images)
    ├── meningioma/    (400 images)
    ├── notumor/       (400 images)
    └── pituitary/     (400 images)
```

The dataset is **not** stored in this repository (it is in `.gitignore`).

## 4. Train the model

### Option A: Google Colab (as used in this project)
1. Open `notebooks/brain_tumor_cnn.ipynb` in Colab.
2. Runtime → Change runtime type → **GPU**.
3. Zip `Training/` and `Testing/` together as `archive.zip`, then run the upload cell.
4. Run all cells. Outputs: `best_model.pt`, `training_curves.png`, `confusion_matrix.png`, `classification_report.txt`.

### Option B: Local Jupyter
1. `jupyter notebook notebooks/brain_tumor_cnn.ipynb`
2. Skip the Colab-only cells (`google.colab` upload and download) and set `DATA_DIR = 'data'`.

### Key settings (top of the notebook)

| Setting | Default |
|---|---|
| `BACKBONE` | `resnet18` (or `efficientnet_b0`) |
| `EPOCHS` | 15 |
| `BATCH_SIZE` | 32 |
| `LR` | 3e-4 |
| `IMG_SIZE` | 224 |
| `K_FOLDS` | 5 |
| `PATIENCE` | 3 |

## 5. Predict on a new image

```bash
python code/predict.py --image data/Testing/glioma/example.jpg --checkpoint best_model.pt
```

Example output format:

```
Predicted: <class> (<confidence> confidence)
  <class>      <probability>
  ...
```

## 6. Troubleshooting

| Problem | Fix |
|---|---|
| `FileNotFoundError: data/Training` | Zip extracted into a nested folder. Print `os.listdir('data')` and adjust `DATA_DIR`. |
| `CUDA available: False` | Enable a GPU runtime in Colab, or train on CPU (much slower). |
| `Train/Test class order mismatch` | Folder names differ between `Training/` and `Testing/`; make them identical. |
| `ModuleNotFoundError: google.colab` | You are running locally; skip the Colab-only cells. |

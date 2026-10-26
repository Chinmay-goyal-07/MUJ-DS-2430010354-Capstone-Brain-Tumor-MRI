"""Classify a single brain MRI image with a trained checkpoint (best_model.pt).

Usage:
    python code/predict.py --image path/to/mri.jpg --checkpoint best_model.pt

The checkpoint is the file saved by notebooks/brain_tumor_cnn.ipynb:
    {'model_state': ..., 'classes': [...], 'backbone': 'resnet18' | 'efficientnet_b0' | 'swin_t' | 'vit_b_16'}

NOTE: Educational project only - not a medical device.
"""
import argparse

import torch
import torch.nn as nn
import torch.nn.functional as F
from PIL import Image
from torchvision import models, transforms

MEAN, STD = [0.485, 0.456, 0.406], [0.229, 0.224, 0.225]  # ImageNet statistics


def build_model(backbone: str, num_classes: int = 4) -> nn.Module:
    """Same architecture as the notebook (weights=None: the checkpoint supplies them)."""
    if backbone == "resnet18":
        model = models.resnet18(weights=None)
        model.fc = nn.Sequential(nn.Dropout(0.3), nn.Linear(model.fc.in_features, num_classes))
    elif backbone == "efficientnet_b0":
        model = models.efficientnet_b0(weights=None)
        model.classifier = nn.Sequential(
            nn.Dropout(0.3), nn.Linear(model.classifier[1].in_features, num_classes)
        )
    elif backbone == "swin_t":
        model = models.swin_t(weights=None)
        model.head = nn.Sequential(nn.Dropout(0.3), nn.Linear(model.head.in_features, num_classes))
    elif backbone == "vit_b_16":
        model = models.vit_b_16(weights=None)
        model.heads = nn.Sequential(nn.Dropout(0.3), nn.Linear(model.heads.head.in_features, num_classes))
    else:
        raise ValueError(f"Unknown backbone: {backbone}")
    return model


def load_checkpoint(path: str, device: str = "cpu"):
    ckpt = torch.load(path, map_location=device)
    classes = ckpt["classes"]
    model = build_model(ckpt["backbone"], num_classes=len(classes))
    model.load_state_dict(ckpt["model_state"])
    return model.to(device).eval(), classes


def predict_image(image_path: str, model: nn.Module, classes, img_size: int = 224, device: str = "cpu"):
    tf = transforms.Compose([
        transforms.Grayscale(num_output_channels=3),  # MRI is grayscale; replicate to 3 channels
        transforms.Resize((img_size, img_size)),
        transforms.ToTensor(),
        transforms.Normalize(MEAN, STD),
    ])
    x = tf(Image.open(image_path).convert("RGB")).unsqueeze(0).to(device)
    with torch.no_grad():
        probs = F.softmax(model(x), dim=1)[0]
    ranked = sorted(zip(classes, probs.tolist()), key=lambda t: -t[1])
    return ranked[0][0], ranked


def main():
    ap = argparse.ArgumentParser(description="Brain tumor MRI classifier")
    ap.add_argument("--image", required=True)
    ap.add_argument("--checkpoint", default="best_model.pt")
    ap.add_argument("--img-size", type=int, default=224)
    args = ap.parse_args()

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model, classes = load_checkpoint(args.checkpoint, device)
    label, ranked = predict_image(args.image, model, classes, args.img_size, device)
    print(f"Predicted: {label} ({ranked[0][1]:.1%} confidence)")
    for cls, p in ranked:
        print(f"  {cls:12s} {p:.1%}")


if __name__ == "__main__":
    main()

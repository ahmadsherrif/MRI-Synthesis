# Unified 2.5D Attention-GAN for Multi-Modal Brain MRI Synthesis

This repository contains a PyTorch implementation for a 2.5D MRI synthesis pipeline that maps T1 inputs to target modalities (T2, FLAIR). The project is optimized for Google Colab (T4, 12–16GB VRAM) and emphasizes configurable, reproducible experiments.

## Colab setup

```bash
# Clone repo (replace URL with your fork if needed)
!git clone <REPO_URL>
%cd MRI-Synthesis

# Install dependencies
!pip install -r requirements.txt
```

## Quick check

```bash
python scripts/print_config.py --config configs/base.yaml
```

## Project layout

```
configs/        # YAML configs
outputs/        # checkpoints, logs, sample images
scripts/        # entry-point scripts
src/            # source code
  data/
  losses/
  models/
  train/
  utils/
```

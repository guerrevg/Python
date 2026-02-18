# LLM Basics — Large Language Models

> Learn how LLMs work, from architecture to fine-tuning

---

## 📁 Structure

```
LLM(Basics)/
├── Architecture/        # Build GPT from scratch
├── PRE-TRAINING/        # Train your own model
├── WEIGHT-LOADING/      # Load pre-trained weights
└── FINE-TUNING/         # Fine-tune for tasks
```

---

## 🗂️ Modules

### 1. Architecture
Learn the transformer architecture that powers GPT models.

**Files:**
- `main.py` — GPT model implementation
- `supplementary.py` — Components (Attention, LayerNorm, etc.)

**Key Concepts:**
- Token embeddings
- Position embeddings
- Multi-head attention
- Feed-forward networks
- Layer normalization

**Run:**
```bash
cd Architecture
python main.py
```

---

### 2. Pre-Training
Train a GPT model from scratch.

**Files:**
- `main.py` — Training loop
- `supplementary.py` — Data loading & utilities
- `RunOnPreTrainedData.py` — Test trained model
- `RunInNamedFile.py` — Load and run

**Key Concepts:**
- Data preparation
- Loss calculation
- Gradient descent
- Model checkpointing

**Run:**
```bash
cd PRE-TRAINING
python main.py  # Train model
python RunOnPreTrainedData.py  # Test it
```

---

### 3. Weight Loading
Load pre-trained GPT-2 weights into your model.

**Files:**
- `main.py` — Load and generate text
- `gpt_download.py` — Download GPT-2 weights
- `supplementary.py` — Model components
- `run.py` — Quick test

**Key Concepts:**
- Weight transfer
- Model compatibility
- Inference

**Run:**
```bash
cd WEIGHT-LOADING
python main.py
```

---

### 4. Fine-Tuning
Fine-tune a pre-trained model for specific tasks.

**Files:**
- `main.py` — Fine-tuning with LitGPT
- `evaluation.py` — Evaluate performance

**Key Concepts:**
- LoRA (Low-Rank Adaptation)
- Instruction tuning
- Evaluation metrics

**Run:**
```bash
cd FINE-TUNING
python main.py
```

---

## 🛠️ Requirements

```bash
pip install torch tiktoken matplotlib
pip install litgpt  # For fine-tuning
```

---

## 📚 Resources

| Topic | Resource |
|-------|----------|
| Transformers | [Attention Is All You Need](https://arxiv.org/abs/1706.03762) |
| GPT | [OpenAI GPT](https://openai.com/research) |
| PyTorch | [pytorch.org](https://pytorch.org/) |
| LitGPT | [GitHub](https://github.com/Lightning-AI/litgpt) |

---

## 💡 Tips

1. **Start small** — Use smaller models first (124M)
2. **Understand architecture** — Read `supplementary.py` carefully
3. **Experiment** — Change hyperparameters
4. **Monitor loss** — Watch training curves

---

Happy learning! 🤖

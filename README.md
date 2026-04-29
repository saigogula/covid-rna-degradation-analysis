# RNA Degradation Analysis (Kaggle)

##  Overview
This project analyzes RNA sequence data from the Stanford COVID Vaccine Kaggle competition.  
The goal is to explore how RNA sequence characteristics relate to degradation rates under different conditions.

---

##  What I Did
- Downloaded real-world biomedical dataset using Kaggle API
- Processed JSON (nested) data into a structured pandas DataFrame
- Engineered meaningful features:
  - Sequence length
  - Nucleotide counts (A, U, G, C)
  - Nucleotide ratios
  - Average degradation values
- Visualized relationships between features and degradation

---

##  Key Findings
- RNA sequence length showed **no variation**, making it non-predictive
- Nucleotide composition (A, U, G, C counts) showed **weak correlation** with degradation
- Suggests degradation may depend more on **RNA structure** than simple sequence features

---

##  Tech Stack
- Python
- Pandas
- Matplotlib
- KaggleHub API

---

##  How to Run

### 1. Install dependencies
```bash
pip install pandas matplotlib kagglehub

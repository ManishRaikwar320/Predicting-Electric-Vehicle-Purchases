## 📁 Project Structure

```text
ml-project/
│
├── data/
│   ├── raw/
│   │   └── data.csv
│   └── processed/
│
├── models/
│   └── model.pkl
│
├── src/
│   ├── data_preprocessing.py
│   ├── train.py
│   ├── predict.py
│   └── evaluate.py
│
├── api/
│   └── main.py
│
├── tests/
│   └── test_api.py
│
├── notebooks/
│   └── experiments.ipynb
│
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
├── config.py
└── README.md
```

## 📌 Folder Description

| Folder/File                 | Description                     |
| --------------------------- | ------------------------------- |
| `data/raw/`                 | Original/raw dataset            |
| `data/processed/`           | Preprocessed dataset            |
| `models/`                   | Trained ML model                |
| `src/`                      | Main ML source code             |
| `src/data_preprocessing.py` | Data cleaning and preprocessing |
| `src/train.py`              | Model training                  |
| `src/predict.py`            | Prediction logic                |
| `src/evaluate.py`           | Model evaluation                |
| `api/main.py`               | FastAPI application             |
| `tests/`                    | Testing files                   |
| `notebooks/`                | EDA and experiments             |
| `requirements.txt`          | Python dependencies             |
| `Dockerfile`                | Docker configuration            |
| `config.py`                 | Project configuration           |
| `README.md`                 | Project documentation           |

## 🔄 ML Pipeline

```text
Raw Data
   ↓
Data Preprocessing
   ↓
Feature Engineering
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Trained Model
   ↓
FastAPI
   ↓
Docker
   ↓
AWS EC2
```

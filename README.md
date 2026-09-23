# 🚗 EV Purchase Prediction

> **End-to-End Machine Learning Web Application for Predicting Electric Vehicle Purchases**

An end-to-end Machine Learning project that predicts whether a customer is likely to **purchase an Electric Vehicle (EV)** based on customer and vehicle-related information.

The project includes a trained ML model, FastAPI backend, HTML frontend, and Docker-based deployment setup.

---

## 📊 Model Performance

| Metric | Score |
|---|---:|
| 🎯 Model Accuracy | **95%** |

The trained model achieves approximately **95% accuracy** on the evaluated dataset.

---

## ✨ Features

- 🤖 Machine Learning based EV purchase prediction
- 🎯 **95% model accuracy**
- ⚡ FastAPI REST API for model inference
- 🌐 Simple and clean web frontend
- 🐳 Dockerized backend and frontend
- 📦 Large ML model kept outside the Docker image using volume mounting
- 🧪 Test files for API/model testing
- 📓 Jupyter notebooks for experimentation and development
- 📈 Visualizations and data analysis

---

## 🏗️ Project Architecture

```text
                    ┌─────────────────────┐
                    │      Web Browser    │
                    │   Frontend : 3000   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   FastAPI Backend   │
                    │      : 8000         │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   ML Model          │
                    │ EV Purchase         │
                    │ Prediction          │
                    └─────────────────────┘
```

---

## 📁 Project Structure

```text
Predicting Electric Vehicle Purchases/
│
├── backend/
│   ├── Data/                  # Dataset / processed data
│   ├── models/                # Trained ML model
│   ├── src/                   # Prediction/helper source code
│   ├── test_data/             # Test data
│   ├── __pycache__/           # Python cache
│   │
│   ├── .dockerignore
│   ├── .gitignore
│   ├── Dockerfile             # Backend Docker configuration
│   ├── main.py                # FastAPI application
│   ├── requirements.txt       # Python dependencies
│   └── test.ipynb             # Testing notebook
│
├── frontend/
│   ├── Dockerfile             # Frontend Docker configuration
│   └── index.html             # Web interface
│
├── notebook/
│   ├── notebook_v1.ipynb      # ML experiments
│   └── working_notebook.ipynb # Model development
│
├── Visual_Graph/              # Data/model visualizations
│
├── .dockerignore
├── docker-compose.yml         # Multi-container deployment
└── README.md
```

---

## 🛠️ Tech Stack

### Machine Learning
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

### Backend
- FastAPI
- Uvicorn
- Python

### Frontend
- HTML
- CSS
- JavaScript

### Deployment
- Docker
- Docker Compose
- Nginx

---

## 🔄 Application Workflow

```text
User enters customer information
            ↓
       Frontend UI
            ↓
      FastAPI REST API
            ↓
       Data Processing
            ↓
       ML Model
            ↓
    Prediction / Probability
            ↓
       Result on UI
```

---

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd "Predicting Electric Vehicle Purchases"
```

### 2. Run Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend will be available at:

```text
http://localhost:8000
```

FastAPI documentation:

```text
http://localhost:8000/docs
```

---

## 🐳 Run with Docker

From the project root:

```bash
docker compose up --build
```

After the containers start:

| Service | URL |
|---|---|
| 🌐 Frontend | http://localhost:3000 |
| ⚡ Backend | http://localhost:8000 |
| 📚 API Docs | http://localhost:8000/docs |

To run in background:

```bash
docker compose up -d
```

To stop the containers:

```bash
docker compose down
```

---

## 💾 Large Model Handling

The trained ML model is approximately **1.5 GB**.

Instead of copying this large model into the Docker image, the project mounts the model directory as a Docker volume.

Example:

```yaml
volumes:
  - ./backend/models:/app/models
```

This keeps the Docker image smaller and allows the model to remain outside the image.

---

## 🧪 API Example

Example prediction request:

```json
{
  "Age": 30,
  "Salary": 60000,
  "Range_Anxiety_Level": "Low"
}
```

The API processes the input and returns the EV purchase prediction.

> The exact input fields depend on the features used by the trained model.

---

## 📈 Model Development

The `notebook/` directory contains notebooks used for:

- Data exploration
- Data preprocessing
- Feature engineering
- Model training
- Model evaluation
- Visualization
- Experimentation

The `Visual_Graph/` directory contains generated graphs and visualizations.

---

## 🎯 Project Goal

The main goal of this project is to demonstrate a complete **Machine Learning → API → Web Application → Docker** workflow.

```text
Dataset
   ↓
Data Preprocessing
   ↓
Feature Engineering
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Model Saving
   ↓
FastAPI
   ↓
Frontend
   ↓
Docker Deployment
```

---

## 🔮 Future Improvements

- ☁️ Deploy application on AWS
- 🔐 Add API authentication
- 📊 Add prediction probability visualization
- 📈 Add model monitoring
- 🔄 Add automated CI/CD pipeline
- 🧪 Add more automated tests
- 📱 Improve responsive UI
- 🚀 Production deployment with HTTPS

---

## 👨‍💻 Author

**Manish Raikwar**

**Linkedin Profile:**
www.linkedin.com/in/manish-raikwar-209878264

Machine Learning Engineer | AI/ML | Deep Learning | GenAI

---

## ⭐ If you find this project useful

Give the repository a ⭐ on GitHub and feel free to explore the code!

---

### 📌 Project Status

**Completed — Local Docker Deployment Ready 🚀**

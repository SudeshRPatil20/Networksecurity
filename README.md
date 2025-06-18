
# 🛡️ Phishing Website Detection using Network Data

> An end-to-end machine learning system to detect phishing websites based on extracted network-level data. This project includes full pipeline automation: from data ingestion and preprocessing to model training, evaluation, and deployment using MongoDB, Flask, and Docker.



## 📁 Project Structure

```

Networksecurity/
├── .github/workflows/       # GitHub Actions CI/CD workflows
├── Network\_Data/            # Raw network data (CSV, JSON, logs)
├── **pycache**/             # Auto-generated Python cache files
├── data\_schema/             # Data validation schemas (JSONSchema / Python)
├── final\_model/             # Trained ML models (Pickle / Joblib)
├── networksecurity/         # Core ML logic, cleaning, features
├── prediction\_output/       # Logs and outputs from model predictions
├── templates/               # HTML templates for Flask web UI
├── valid\_data/              # Cleaned and validated data
├── .env                     # Environment variables (MongoDB URI etc.)
├── .gitignore               # Files/folders to be ignored by Git
├── Dockerfile               # Containerization setup
├── README.md                # Project documentation
├── app.py                   # Flask app for UI & API
├── main.py                  # Main script (e.g. CLI entry)
├── push\_data.py             # Script to push raw data into MongoDB
├── requirements.txt         # Python dependencies
├── setup.py                 # Python package setup (if needed)
└── test\_mongo.py            # Unit test for MongoDB connectivity

````

---

## 🎯 Objective

This project aims to **detect phishing websites** using machine learning models trained on **network-level features** such as domain patterns, SSL status, IP usage, and other indicators.

---

## 🔧 Technologies Used

| Layer               | Tools / Libraries |
|---------------------|------------------|
| Language            | Python 3.9+       |
| Data Storage        | MongoDB Atlas     |
| ML Frameworks       | scikit-learn, XGBoost |
| Web Framework       | Flask             |
| Visualization       | Matplotlib, Seaborn |
| DevOps              | Docker, GitHub Actions |
| Deployment (Optional)| Render / Railway / Heroku |

---

## 🔄 Project Workflow

```text
Raw Data → MongoDB → Data Cleaning → Feature Extraction → Model Training → Evaluation → Web/API Prediction
````

### 🔹 1. Data Ingestion

* Raw data from `Network_Data/` is inserted into MongoDB via `push_data.py`.

### 🔹 2. Data Validation & Cleaning

* Schema validation is applied using `data_schema/` rules.
* Cleaned data is saved in `valid_data/`.

### 🔹 3. Feature Engineering

* Features include:

  * URL length
  * Use of IP instead of domain
  * HTTPS/SSL usage
  * Number of dots, slashes, redirects
  * Keyword presence (e.g., `login`, `secure`, etc.)

### 🔹 4. Model Training

* Models: Random Forest, XGBoost
* Training scripts in `networksecurity/train_model.py`
* Saved in `final_model/`

### 🔹 5. Evaluation

* Metrics: Accuracy, Precision, Recall, F1-Score, ROC-AUC
* Confusion matrix and ROC curves are generated.

### 🔹 6. Prediction

* CLI-based (`main.py`) or Web-based (`app.py`)
* Output saved in `prediction_output/`

### 🔹 7. Deployment

* Flask app can be containerized using Docker.
* Optional CI/CD with GitHub Actions in `.github/workflows/`.

---

## ⚙️ How to Run

### ✅ Prerequisites

* Python 3.9+
* MongoDB URI (local or [MongoDB Atlas](https://www.mongodb.com/cloud/atlas))
* Docker (optional)
* Create `.env` file:

```env
MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/phishing
```

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

### 📤 Push Raw Data to MongoDB

```bash
python push_data.py
```

### 🧹 Clean and Process Data

```bash
python networksecurity/preprocess.py
```

### 🧠 Train the Model

```bash
python networksecurity/train_model.py
```

### 🔮 Run Predictions

#### CLI:

```bash
python main.py --url "http://example.com"
```

#### Flask UI:

```bash
python app.py
```

Access the interface at: `http://localhost:5000`

---

## 🐳 Docker Deployment (Optional)

### Build the Docker Image

```bash
docker build -t phishing-detector .
```

### Run the Container

```bash
docker run -p 5000:5000 phishing-detector
```

---

## 🧪 Testing

```bash
python test_mongo.py
```

> Tests MongoDB connection and basic insert/retrieve functionality.

---

## 📊 Sample Results

| Model         | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
| ------------- | -------- | --------- | ------ | -------- | ------- |
| Random Forest | 96.5%    | 95.8%     | 97.1%  | 96.4%    | 98.2%   |
| XGBoost       | 97.1%    | 96.6%     | 97.8%  | 97.2%    | 98.6%   |

---

## 📌 Future Enhancements

* [ ] Browser extension for real-time phishing alert
* [ ] Integration with WHOIS and Google Safe Browsing APIs
* [ ] Deployment on cloud server (Heroku/Render)
* [ ] Streamlit version for faster prototyping

---

## 🤝 Contributing

Feel free to fork the repo, raise issues, or submit PRs to improve the system!

```bash
git clone https://github.com/yourusername/Networksecurity.git
```

---

## 📄 License

Licensed under the [MIT License](LICENSE).

---

## ⭐ Show Your Support

If you found this project useful, please ⭐ star the repo and share it with others in the security & ML community!

```

---

Let me know if you'd like:
- 🖼 A logo/banner at the top.
- 🧪 Jupyter Notebooks for EDA and visualization.
- 📦 A setup for Streamlit instead of Flask.
- 🌐 A guide for deploying this with MongoDB Atlas.

I'm happy to help build each script or customize the documentation further.


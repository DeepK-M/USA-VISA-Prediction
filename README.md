# USA Visa Prediction using Machine Learning  

## 📌 Project Overview  
This project aims to predict the approval or denial of **USA Visa applications** based on historical data.  
It leverages **XGBoost**, **RandomizedSearchCV** for hyperparameter tuning, and **Streamlit** for an interactive web interface.

## 🎯 Features  
✅ Data Preprocessing & Cleaning  
✅ Machine Learning Model using **XGBoost**  
✅ Hyperparameter tuning with **RandomizedSearchCV**  
✅ Web Application using **Streamlit**  
✅ Visualization of Predictions  

---

## 📂 Folder Structure  
```
📦 USA-VISA-Prediction    
├── 📜 notebook          # Jupyter Notebooks for EDA & experiments   
├── 📜 app.py            # Main Streamlit app  
├── 📜 requirements.txt  # Dependencies  
├── 📜 README.md         # Project Documentation  
└── 📜 visa_model.pkl    # Trained ML Model  
```

---

## ⚙️ Installation & Setup  
### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/DeepK-M/USA-VISA-Prediction.git
cd USA-VISA-Prediction
```

### 2️⃣ Create a Virtual Environment  
```sh
python -m venv venv
```
Activate the environment:  
- **Windows:** `venv\Scripts\activate`  
- **Mac/Linux:** `source venv/bin/activate`  

### 3️⃣ Install Dependencies  
```sh
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit App  
```sh
streamlit run app.py
```

---

## 🛠️ Model Training  
To train the XGBoost model, run:  
```sh
run jupyter notebook
```
This will save the trained model as `visa_model.pkl`.

---

## 📊 Prediction Results  
Example **Confusion Matrix** & **Classification Report** for model evaluation

---

## 🖥️ Web Application  
A **Streamlit-based Web App** allows users to input Visa application details and get real-time predictions.  

**🔹 To run the app locally:**  
```sh
streamlit run app.py
```
Dataset : 
---

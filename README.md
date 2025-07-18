# 💼 Employee Salary Prediction using Machine Learning

This project predicts whether an employee earns more than ₹50K based on features such as age, education, hours worked, and more. Built as part of my AICTE-Edunet Foundation Internship, it involves the full machine learning pipeline — from data preprocessing to model comparison and Streamlit app deployment.

---

## 📌 Overview

This project was initiated as part of my AI internship with **Edunet Foundation** under the **IBM SkillsBuild Program (June–July 2025)**.

The goal is to build a machine learning model that can predict whether an individual's salary is above or below 50K based on demographic and work-related features.

---

## 🧠 What’s Done So Far

✅ Mounted Google Drive in Colab  
✅ Loaded and explored dataset  
✅ Handled missing values and unknowns (`?`)  
✅ Cleaned and encoded categorical features  
✅ Removed outliers in `age`, `educational-num`, etc.  
✅ Visualized data with boxplots  
✅ Scaled features using StandardScaler  
✅ Trained ML models (Logistic, KNN, XGBoost, etc.)  
✅ Evaluated performance using accuracy and ROC-AUC  
✅ Built a Streamlit app for live prediction  
✅ Deployed app for public use (pending)

---

## 🚀 Project Overview

This ML-powered web app allows users to input various employee attributes and predicts whether the salary is more than ₹50K or not. It uses the XGBoost model trained on the UCI Adult Income dataset and deployed via Streamlit.

👨‍💼 **Use Case:** HR analytics, salary estimation, AI demo project  
📦 **Frameworks:** Python, Scikit-learn, XGBoost, Streamlit  
🧠 **Model:** XGBoost (best performing), others for comparison

---

## 🧪 ML Models Used

| Model                 | Accuracy  |
|----------------------|-----------|
| Logistic Regression  | 83.1%     |
| K-Nearest Neighbors  | 82.7%     |
| MLP Classifier       | 83.9%     |
| Random Forest        | 85.4%     |
| **XGBoost** ✅        | **86.8%** |

---

## 📊 Dataset Used

- Adapted version of the **UCI Adult Census Income** dataset  
- 48,842 rows, 15 columns (after cleaning)

---

## 📊 Visual Comparison

> 📈 Model performance compared via accuracy and ROC-AUC

![Model Comparison](model_comparison.png)

---

## 🌐 Live App Demo

👉 [Try it on Streamlit](https://yourname-employee-salary-prediction.streamlit.app/)  
_(Replace the URL above after deploying on Streamlit Cloud)_

---

## 🖥️ How to Run This Project Locally

### 1. Clone the repository

git clone https://github.com/AmanBasu20/employee-salary-prediction.git
cd employee-salary-prediction

### 2. Install the dependencies

pip install -r requirements.txt

### 3. 3. Run the Streamlit app

streamlit run app.py

---

## 📁 Project Structure

employee-salary-prediction/
### ├── app.py                       # Streamlit application
### ├── employee_salary_prediction.ipynb  # Colab notebook (model training)
### ├── xgboost_salary_model.pkl     # Trained XGBoost model
### ├── salary_scaler.pkl            # StandardScaler object
### ├── requirements.txt             # Python dependencies
### ├── model_comparison.png         # Accuracy chart
### └── README.md                    # Project documentation

---

## 🙋‍♂️ About Me

Aman Basu
B.Tech CSE (AI & ML) | Intern @ AICTE x Edunet | Aspiring AI/Quant Researcher

---

## 📬 Contact

📧 vadlasadvik99@@gmail.com 
🔗 [LinkedIn](https://www.linkedin.com/in/sadvikkumar/)  
🔗 [GitHub](https://github.com/sadvik-asus)

---

*Learning in public. Built with curiosity. 🚀*
*Test your Limits 🤗*

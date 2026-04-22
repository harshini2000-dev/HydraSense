# 💧 HydraSense_ML: Dehydration Risk Detection System using Machine Learning

Access Portal: https://hydrasense-ml.streamlit.app/

## 📌 Project Overview
This project implements a machine learning based system to monitor hydration levels and predict personalized water intake requirements. The system combines classification and regression models to detect dehydration risk and recommend appropriate water consumption based on individual lifestyle and environmental factors.

---

## 🎯 Objectives
- Detect whether a person is dehydrated or well hydrated
- Predict daily water intake requirements (in liters)
- Apply machine learning to a real-world health monitoring problem

---

## 📊 Dataset
**Daily Water Intake and Hydration Patterns Dataset**  
Source: Kaggle  
Link: https://www.kaggle.com/datasets/sonalshinde123/daily-water-intake-and-hydration-patterns-dataset

### Features Used
- Age
- Gender
- Weight (kg)
- Physical Activity Level
- Weather Conditions
- Daily Water Intake (liters)

### Target Variables
- **Hydration Level** (Classification: Dehydrated / Not Dehydrated)
- **Daily Water Intake (liters)** (Regression)

---

## 🧠 Machine Learning Models
### Dehydration Detection (Classification)
- Logistic Regression
- Evaluation Metrics:
  - Accuracy: ~98%
  - Recall (Dehydrated): 100%
  - F1-score: 0.96

### Water Intake Prediction (Regression)
- Linear Regression
- Evaluation Metrics:
  - MAE: ~0.25 liters
  - RMSE: ~0.29 liters
  - R² Score: ~0.87

---

## 🛠️ Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn / Sklearn
- Matplotlib
- Seaborn
- Jupyter Notebook
- Streamlit

---

## 📈 Key Results
- Highly accurate dehydration detection with zero false negatives
- Reliable water intake prediction with low error margin
- Practical, real-world applicable health monitoring system

---

## Images
### 1. Hydrated Case
<img width="600" height="600" alt="image" src="https://github.com/user-attachments/assets/dff64d82-f05b-4b78-8494-702e2b16f693" />

<img width="500" height="440" alt="image" src="https://github.com/user-attachments/assets/250b50af-d7ba-4b65-b818-4243826dda72" />

### 2. Dehydrated Case
<img width="600" height="600" alt="image" src="https://github.com/user-attachments/assets/95abd81f-d7e4-4d80-990e-b3717287ef49" />

<img width="500" height="440" alt="image" src="https://github.com/user-attachments/assets/8bd40e32-5cd6-4927-a3a4-7d3306851633" />

---

## 🚀 Future Enhancements
- Deploy as a Streamlit web application
- Add real-time water intake tracking
- Water Reminder System
- Implement MLOps pipelines for monitoring and retraining

---

## 📌 Conclusion
This project demonstrates the application of machine learning techniques to solve a real-world health problem by combining predictive modeling with rule-based decision logic to create a smart hydration monitoring system.





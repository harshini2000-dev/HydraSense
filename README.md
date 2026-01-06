# 💧 HydraSense: Smart Hydration Monitoring & Water Reminder System

## 📌 Project Overview
This project implements a machine learning based system to monitor daily hydration levels, predict personalized water intake requirements, and provide smart water reminders. The system combines classification and regression models to detect dehydration risk and recommend appropriate water consumption based on individual lifestyle and environmental factors.

---

## 🎯 Objectives
- Detect whether a person is dehydrated or well hydrated
- Predict daily water intake requirements (in liters)
- Generate personalized water intake reminders
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

## ⚙️ Smart Water Reminder Logic
The system combines predictions from both models to:
1. Estimate daily water intake requirements
2. Detect dehydration risk
3. Trigger personalized reminders based on remaining water deficit

Example Output:
- “High dehydration risk! Drink 1.2 liters of water today.”
- “You are well hydrated. Keep it up!”

---

## 🛠️ Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib / Seaborn
- Jupyter Notebook

---

## 📈 Key Results
- Highly accurate dehydration detection with zero false negatives
- Reliable water intake prediction with low error margin
- Practical, real-world applicable health monitoring system

---

## 🚀 Future Enhancements
- Deploy as a Streamlit web application
- Add real-time water intake tracking
- Integrate wearable or mobile app data
- Implement MLOps pipelines for monitoring and retraining

---

## 📌 Conclusion
This project demonstrates the application of machine learning techniques to solve a real-world health problem by combining predictive modeling with rule-based decision logic to create a smart hydration monitoring system.


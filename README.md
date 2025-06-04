# Income-Prediction-ML-Pipeline
End-to-end machine learning pipeline for predicting whether an adult earns more or less than $50K/year using census income data.

This project is an end-to-end machine learning pipeline built to predict whether an individual's annual income exceeds $50,000 using census data. It demonstrates the full lifecycle of a data science project—from setting up the environment, implementing logging and custom exception handling, data ingestion, preprocessing, model training, evaluation, and finally building training and prediction pipelines. The solution includes production-ready components and serves as a strong foundation for scalable ML deployments.

## 📌 Project Highlights

✅ End-to-End Machine Learning Workflow  
✅ Clean, Modular Codebase (production-ready)  
✅ Training and Inference Pipelines  
✅ Custom Logging and Exception Handling  
✅ FastAPI  
✅ Interactive UI with Streamlit  
✅ Scalable Architecture for Deployment

---

## 📊 Business Problem

The goal is to build a classification model that can predict whether a person earns more than \$50,000 per year based on demographic attributes. This can be useful for:

- Targeted marketing and customer segmentation  
- economic research  
- Policy-making and resource allocation
- And many more....  

---

## 🧾 Dataset Description

We use the Adult Census Income dataset from the UCI Machine Learning Repository. It includes both categorical and continuous features.

### Key Features:
- `age`: Age of the individual (Continuous)
- `workclass`: Employment type (e.g., Private, Self-emp, Govt)
- `education` & `education-num`: Education level and years
- `marital-status`: Marital status
- `occupation`: Type of job
- `relationship`: Relationship within the household
- `race`, `sex`: Demographic attributes
- `capital-gain`, `capital-loss`: Investment gains/losses
- `hours-per-week`: Weekly working hours
- `native-country`: Country of origin
- `salary`: **Target label** — whether income is `>50K` or `<=50K`

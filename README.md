# 🚀 Rock vs Mine Prediction System

This repository contains a Machine Learning project aimed at predicting whether a given object is a **rock** or a **mine** based on various features extracted from sonar signals. The prediction model is built using **Logistic Regression** and is deployed using **Streamlit** for easy access and interaction.

## 📄 Project Overview

The goal of this project is to classify sonar returns obtained from rocks and mines into two categories: **Rock** or **Mine**. We use a dataset containing **60 different types of features** derived from sonar signals. The machine learning model is trained using **Logistic Regression** and has achieved the following accuracies:
- **Training Accuracy**: 83%
- **Test Accuracy**: 76%

## ✨ Features

The dataset contains 60 features, each representing a specific characteristic of the sonar signal, which helps in classifying the object.

## 🛠️ Technologies Used

- **Python** 🐍
- **Pandas**: For data manipulation and analysis 📊
- **Scikit-Learn**: For building the logistic regression model 📈
- **Streamlit**: For deploying the model as a web application 🌐

## ⚙️ Installation

To run this project locally, please follow these steps:

### 1. 📥 Clone the Repository

Navigate to the desired location on your local machine and clone the repository:

```bash
git clone https://github.com/KunalSingh5431/Rock-vs-Mine-Prediction-System.git
```

### 2. 📂Navigate to the Project Directory

Move into the project directory:

```bash
cd Rock-vs-Mine-Prediction-System
```

### 3. 📦Install the Required Dependencies
Install the necessary dependencies listed in the requirements.txt file:

```bash
pip install -r requirements.txt
```

### 🚀Usage
To use the model for prediction, you can run the Streamlit app locally:
```bash
streamlit run app.py
```
After running the above command, open your browser and go to http://localhost:8501 to access the web app interface.

### 🌍Deployment

The model has been deployed using Streamlit for a more user-friendly experience. You can access the live deployment through the following link:

👉 [Rock vs Mine Prediction Web App](https://kunalsingh5431-rock-vs-mine-prediction-system-app-ykfub4.streamlit.app/?embed_options=show_toolbar)


### 📊Results
Training Accuracy: 83%
Test Accuracy: 76%
These results indicate that the model performs well on unseen data and can accurately distinguish between rocks and mines based on sonar signals.

### 🤝Contributing
If you want to contribute to this project, feel free to fork the repository and submit a pull request.

### 📧Contact
For any queries or feedback, feel free to contact me at kunalsingh5431@gmail.com.




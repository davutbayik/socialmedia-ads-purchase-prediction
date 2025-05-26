# 📊 Social Media Ads Purchase Prediction

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-🧠_App-brightgreen?logo=streamlit)
![FastAPI](https://img.shields.io/badge/FastAPI-🚀_API-green?logo=fastapi)
![Made with love](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red)

---

A machine learning-powered web app that predicts whether a user will purchase a product based on their ***Gender***, ***Age***, and ***Estimated Salary***.

👉 [Live App](https://socialmedia-ads-purchase-prediction.onrender.com/)

## 🚀 Features

- 📈 Predict purchase behavior in real-time
- 🧠 ML pipeline with preprocessor and trained model
- 🌍 Deployed Streamlit UI for user interaction
- 🧪 FastAPI backend for live predictions
- ⚡ Clean and responsive UI with emoji-powered UX

### 🧰 Tech Stack

| Tool         | Role                          |
|--------------|-------------------------------|
| Streamlit    | Front-end / UI                |
| FastAPI      | Backend API for ML model      |
| scikit-learn | ML modeling & preprocessing   |
| Python       | Core language                 |
| Uvicorn      | ASGI server for FastAPI       |


## 📊 Data Source

The dataset used for this project is sourced from Kaggle:  
[Social Network Ads Dataset](https://www.kaggle.com/datasets/rakeshrau/social-network-ads)

## 🧠 ML Model Details
<b>Dataset</b>: Social Network Ads (includes Gender, Age, EstimatedSalary)

<b>Model</b>: XGBoost Classifier with Hyper-parameter tuning

<b>Pipeline</b>:

   - ```PowerTransformer``` for numerical features (Age and EstimatedSalary)
   - ```OneHotEncoder``` for categorical features (Gender)
   - Combined via ```ColumnTransformer```

## 🛠️ Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone https://github.com/davutbayik/socialmedia-ads-purchase-prediction.git
   cd socialmedia-ads-purchase-prediction

2. **Create and activate a virtual environment (Optional-Recommended)**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt

4. **Run the application**

   Use the provided Python script to launch both the API and UI (comment server URL and uncomment local URL before running from ```streamlit_app.py```):
    ```bash
   python run_app.py
   ```
   - FastAPI will be available at (locally): ```http://127.0.0.1:8000```
   - Streamlit app will be available at (locally): ```http://localhost:8501```

## 📡 Deployment
   - 🔵 [<b>Streamlit App</b>](https://socialmedia-ads-purchase-prediction.onrender.com/): To be deployed on services like Koyeb, Render or Streamlit Community Cloud
   - ⚙️ <b>FastAPI Backend</b>: To be deployed on services like Koyeb, Render, Railway, or Fly.io

## 📷 Screenshot
Live example of the app

![Streamlit App](assets/streamlit_app.png)

## 🎥 Example Demo


https://github.com/user-attachments/assets/6e3a524a-7a46-4f84-ba9c-542e5cac1bfb


### 🤝 Contributing

Contributions are welcome and appreciated! If you’d like to improve this project, here’s how you can help:

- 🐞 Report bugs or issues.
- 🌟 Suggest new features or improvements.
- 🔀 Fork the repo, make your changes, and submit a pull request.

Please make sure your code follows best practices and includes proper documentation where necessary.

### 📄 License

This project is licensed under the terms of the [MIT License](LICENSE).  
You are free to use, modify, and distribute this software as long as you include the original license.

### 📬 Contact

Made with ❤️ by [Davut Bayık](https://github.com/davutbayik) — feel free to reach out via GitHub for questions, feedback, or collaboration ideas.

---

⭐ If you found this project helpful, consider giving it a star!

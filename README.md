# Amazon Reviews Sentiment Analysis [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An interactive **Streamlit + NLP** web application that classifies Amazon product reviews into **Positive, Negative, or Neutral** sentiments. The app allows users to upload CSV datasets, preview raw data, select custom review columns, and visualize sentiment insights using charts and WordClouds.

## ✨ Features
- **Sentiment Classification:** Uses **TextBlob NLP** to analyze reviews and categorize them into positive, negative, or neutral.
- **Interactive Web App:** Built with **Streamlit** for a user-friendly and interactive interface.
- **Data Upload & Preview:** Users can easily upload their own CSV files and explore the raw data directly in the app.
- **Custom Column Selection:** Flexibility to choose the specific review column to be analyzed from the uploaded dataset.
- **Visual Insights:** Get a quick overview of sentiment with distribution bar charts and WordClouds generated for positive and negative reviews.

## 🚀 Tech Stack
- **Python:** The core programming language for the application.
- **Streamlit:** Used for creating the web application interface.
- **TextBlob:** The NLP library used for sentiment analysis.
- **Pandas:** Utilized for data manipulation and handling CSV files.
- **Matplotlib & WordCloud:** Libraries for generating visualizations.

## 💻 Installation & Usage

### Prerequisites
Make sure you have Python installed on your system.

### Steps
1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/amazon-sentiment-app.git
    cd amazon-sentiment-app
    ```
2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the Streamlit application from your terminal:
    ```bash
    streamlit run app.py
    ```
4.  Open your browser and navigate to `http://localhost:8501` to start analyzing reviews.

## 📂 Project Structure
```bash
amazon-sentiment-app/
│
├── app.py            # The main Streamlit application script
├── requirements.txt  # List of project dependencies
└── README.md         # Project documentation (this file)
```

## 🔗 Live Demo
Try out the live application here:  
[https://sentiment-analysis-dbwjqpwxc2opv8tmejpwu5.streamlit.app/](https://sentiment-analysis-dbwjqpwxc2opv8tmejpwu5.streamlit.app/)

## 👨‍💻 Author
**Koushikya Maroju**  
- GitHub: [https://github.com/koushikya04](https://github.com/koushikya04)  
- LinkedIn: [https://www.linkedin.com/in/koushikya-maroju](https://www.linkedin.com/in/koushikya-maroju)


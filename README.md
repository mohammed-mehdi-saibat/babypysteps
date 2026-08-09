# babypysteps

## Description

This project tracks the preparation phases for the AI ecosystem. It covers the transition from traditional web development to Python, and builds up to mastering the professional Data Science stack for data manipulation, cleaning, visualization, and deploying machine learning models as web microservices.

### 🚀 Week 1: Python & OOP Foundations

- Transitioning from Object-Oriented Programming to Python.
- Setting up virtual environments and basic data pipelines.
- Building custom modules and natively handling CSV files.

### 📊 Week 2: The Data Stack

- **NumPy:** Speed testing Python loops vs. C-optimized vectorization, and Boolean Indexing.
- **Pandas:** Loading datasets into DataFrames, statistical summaries, and filtering.
- **Data Cleaning:** Handling `NaN` (missing values), dropping duplicates, and grouping data.
- **Data Visualization:** Building static and themed charts using Matplotlib and Seaborn.

### 🤖 Week 3 & 4: Machine Learning & Microservices

- **Scikit-Learn:** Building end-to-end predictive pipelines using the Titanic dataset.
- **Feature Engineering:** Translating text to mathematics using One-Hot Encoding and handling missing values dynamically.
- **Baseline Models:** Training and evaluating Logistic Regression algorithms.
- **Deployment:** Bridging data science and web development by serializing models (`joblib`) and deploying a predictive FastAPI microservice.

### 🌲 Week 5: Advanced Algorithms (Ensembles)

- **Decision Trees:** Visualizing Gini impurity, mapping non-linear algorithmic flowcharts, and analyzing model overfitting.
- **Random Forests:** Implementing 100-tree ensemble models to leverage "the wisdom of the crowd," optimizing the confusion matrix, and breaking the 80% accuracy threshold.

## Prerequisites

- Python 3.11+
- Git

## Installation

1. Clone the repository:

   ```bash
   git clone <REPOSITORY_URL>
   cd prep-ia-mehdisaibat
   ```

2. Create and activate the virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the main Python script:

```bash
python main.py
```

To run the Machine Learning FastAPI microservice:

```bash
uvicorn api:app --reload
```

Once running, navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to test the API via Swagger UI.

To explore the interactive Data Science & Machine Learning notebooks:

```bash
jupyter lab
```

OR open directly in VS Code using the Jupyter extension.

## Project Structure

- `data/` : Contains the sample datasets (`sample.csv`).
- `docs/` : Learning notes and documentation (e.g., OOP concepts).
- `notebooks/` : Jupyter notebooks detailing the progression from basic Python modules to Pandas data cleaning, Seaborn visualizations, and Scikit-Learn model training.
- `src/` : Core Python modules (`utils.py`, `dataset.py`).
- `api.py` : The FastAPI web server acting as the predictive microservice.
- `titanic_model.pkl` : The serialized machine learning model used by the API.
- `main.py` : The main entry point of the terminal application.

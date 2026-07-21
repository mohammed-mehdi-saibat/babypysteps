# babypysteps

## Description

This project tracks the preparation phases for the AI ecosystem. It covers the transition from traditional web development (PHP/OOP) to Python, and builds up to mastering the professional Data Science stack for data manipulation, cleaning, and visualization.

### 🚀 Week 1: Python & OOP Foundations

- Transitioning from PHP Object-Oriented Programming to Python.
- Setting up virtual environments and basic data pipelines.
- Building custom modules and natively handling CSV files.

### 📊 Week 2: The Data Stack

- **NumPy:** Speed testing Python loops vs. C-optimized vectorization, and Boolean Indexing.
- **Pandas:** Loading datasets into DataFrames, statistical summaries, and filtering.
- **Data Cleaning:** Handling `NaN` (missing values), dropping duplicates, and grouping data.
- **Data Visualization:** Building static and themed charts using Matplotlib and Seaborn.

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

To run the main script from the terminal:

```bash
python main.py
```

To explore the interactive notebooks (containing the Week 1 & Week 2 data exercises):

```bash
jupyter lab
# OR open directly in VS Code using the Jupyter extension
```

## Project Structure

- `data/` : Contains the sample datasets (`sample.csv`).
- `docs/` : Learning notes and documentation (e.g., OOP concepts).
- `notebooks/` : Jupyter notebooks detailing the progression from basic Python modules to Pandas data cleaning and Seaborn visualizations.
- `src/` : Core Python modules (`utils.py`, `dataset.py`).
- `main.py` : The main entry point of the application.

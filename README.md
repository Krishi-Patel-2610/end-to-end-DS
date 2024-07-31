# Student Performance Data Analysis

![License](https://img.shields.io/badge/License-MIT-green)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)

## Overview

This repository contains an end-to-end data science project focused on analyzing and predicting student performance. The project adheres to best practices in software development and data science, including custom exception handling, logging, and a well-organized structure for code, data, and artifacts.

## Table of Contents

1. [Project Structure](#project-structure)
2. [Features](#features)
3. [Setup Instructions](#setup-instructions)
4. [Data](#data)
5. [Modeling](#modeling)
6. [Results](#results)
7. [License](#license)
8. [Contact](#contact)

## Project Structure
```bash
student-performance/
│
├── artifacts/ # Contains all generated artifacts like datasets, models, etc.
│ ├── data/
│ ├── models/
│
├── src/ # Source code for the project
│ ├── features/
│ ├── models/
│ ├── utils/
│ ├── init.py
│ ├── main.py
│ ├── custom_exceptions.py
│ └── logger.py
│
├── setup.py # Installation file
├── requirements.txt # Required packages and dependencies
└── README.md # Project documentation
```
## Features

- **Custom Exception Handling**: Custom exception classes to manage errors effectively.
- **Logging**: Detailed logging for better traceability and debugging.
- **Modular Code Structure**: Clean and modular structure for easy navigation and understanding.
- **Data Pipelines**: Well-defined pipelines for data processing, feature engineering, and model training.

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- [Virtualenv](https://pypi.org/project/virtualenv/) (recommended)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Krishi-Patel-2610/end-to-end-DS.git
   cd end-to-end-DS

2. Create and activate a virtual environment:

    ```bash
    virtualenv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install dependencies:

    ```bash
    pip install -r requirements.txt

4. Run the project:
    ```bash
    python src/main.py

## Dataset
The dataset used for this project consists of student academic performance records. It includes various features such as study time, previous grade scores, and demographic information. The data is preprocessed and stored in the `artifacts/data/` directory.

Link: https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977

## Modelling
The project explores multiple machine learning models to predict student performance. These include:

- Linear Regression
- Decision Trees
- Random Forests
- Gradient Boosting

The best model is selected based on performance metrics such as accuracy, precision, recall, and F1-score.

## Results
Key findings and model performance metrics are documented in the `artifacts/` folder. The final model provides an accurate prediction of student performance, helping educators and policymakers in decision-making.

## License
This project is licensed under the MIT License

## Contact
For any inquiries, please contact:
- Krishi Patel
- GitHub: Krishi-Patel-2610
- Email: krishi.patel9426@gmail.com
# Data Cleaning RESTful API

This project provides a RESTful API for `cleaning CSV files`.
- It removes duplicates,
- Fills missing values,
- Standardizes data formats (e.g., dates, currency), and
- Returns the cleaned CSV file for download.
This tool is useful for data scientists and analysts who frequently deal with messy datasets.

---

### Contents

1. **Introduction**: Briefly describes the project's purpose and its `features.`
2. **Technology Stack**: Lists the technologies and libraries used.
3. **Getting Started**: Provides installation and setup instructions to help users get the project running locally.
4. **Prerequisites**:
5. **Installation**:
6. **API Endpoints**: Clearly describes each API endpoint, including request and response details.
7. **Deployment Instructions**: Provides steps for deploying the application to a cloud platform.
8. **Testing**: Explains how to run tests to verify the functionality.
9. **Contributing**: Includes guidelines for contributing to the project.
10. **License**: States the project's license.
11. **Contact**: Provides contact information for further inquiries or contributions.

---

## Features

- Remove duplicates from the dataset.
- Fill missing values with appropriate placeholders.
- Standardize data formats (e.g., dates, currency).
- Output the cleaned data to a new CSV file.

---

## Technology Stack

- **Python**: Programming language used for developing the API.
- **Flask**: A lightweight WSGI web application framework used to build the API.
- **Pandas**: Python library for data manipulation and analysis.

---

## Getting Started

These instructions will help you set up the project on your local machine for development and testing purposes.

...
---

### Prerequisites

- Python 3.8 or higher
- pip3 (Python package installer)

---

### Installation

1. **Clone the repository**:
	```bash
	git clone 
	cd data_cleaning_api.
	```

2. **Create a virtual environment**:
	```bash
	python3 -m venv venv
	source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
	```

3. **Install dependencies**:
	```bash
	pip install -r requirements.txt
	```

4. **Run the application**:
	```bash
	python run.py
	```
The API will be available at http://localhost:____.


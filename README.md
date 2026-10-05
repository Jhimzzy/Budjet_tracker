# Budget Tracker

A simple Python-based budget tracker for managing income and expenses.

## Features

- Add income transactions
- Add expense transactions
- Categorize transactions
- Add notes to transactions
- Store transaction data
- Automated testing with pytest
- Continuous Integration using GitHub Actions

## Technologies Used

- Python
- Pytest
- GitHub Actions
- Git/GitHub

## Project Structure

```text
Budget_tracker/
│
├── project.py
├── transactions.json
├── tests/
│   └── test_project.py
├── .gitignore
└── README.md

## Automated Testing  

The project uses Pytest to test the income and expense functionality.

Run the tests locally with:

```bash
python -m pytest

## Continuous Integration

GitHub Actions is used to automatically run the project's tests whenever changes are pushed to the repository.

The workflow:

- Checks out the repository
- Sets up Python
- Installs the required dependencies
- Runs the Pytest test suite
- Reports whether the tests passed or failed

This helps ensure that new changes do not introduce errors into the application.

## How to Run the Project

Clone the repository and navigate into the project directory:

```bash
git clone <repository-url>
cd Budget_tracker-main

## Continuous Integration

GitHub Actions is used to automatically run the project's tests whenever changes are pushed to the repository.

The workflow:

- Checks out the repository
- Sets up Python
- Installs the required dependencies
- Runs the Pytest test suite
- Reports whether the tests passed or failed

This helps ensure that new changes do not introduce errors into the application.

## How to Run the Project

Clone the repository and navigate into the project directory:

```bash
git clone <repository-url>
cd Budget_tracker-main

## Installation

Install the required dependencies:

```bash
pip install pytest

## Run Budjet tracker

python project.py

## Run automated test

python -m pytest


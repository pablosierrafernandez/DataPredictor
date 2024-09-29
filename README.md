# **Data Predictor: AI-Powered Data Analysis Tool**
![intro](https://github.com/user-attachments/assets/e88699c7-50f4-4dbb-8896-026e1416c6bd)

![DataPredictor-1](https://github.com/user-attachments/assets/d7464bb7-9f2f-4aba-9ac7-787fb9c99ef5)
![DataPredictor-2](https://github.com/user-attachments/assets/2d9c32f3-e823-432b-b69a-9bf3cbc9549a)
![DataPredictor-3](https://github.com/user-attachments/assets/8835ce09-f2c8-4e72-acb5-6895e6a20736)


## Table of Contents

1.  [Introduction](#introduction)
2.  [Objective](#objective)
3.  [Features](#features)
4.  [Architecture](#architecture)
5.  [Requirements](#requirements)
6.  [Application](#application)
    *   [Backend with FastAPI](#backend-with-fastapi)
    *   [Frontend with Vue.js](#frontend-with-vuejs)
7.  [Usage Instructions](#usage-instructions)
8.  [Contributions](#contributions)
9.  [License](#license)
10.  [Authors](#authors)

## Introduction

Data Predictor is a web application designed to facilitate the analysis of CSV data using AI models. Users can upload their datasets, select target columns, and receive predictions powered by advanced AI algorithms.
![screencapture-localhost-8080-2024-09-29-15_14_04](https://github.com/user-attachments/assets/2abef1a8-55b2-4c41-99bb-948483787557)


## Objective

The main objective of this project is to provide an intuitive interface for users to upload their data and obtain predictions seamlessly. By leveraging PyCaret and FastAPI, this tool aims to simplify data analysis and empower users with actionable insights.

## Features

- Upload CSV files for analysis
- Dynamic selection of target columns
- Automatic data preprocessing using PyCaret
- User-friendly interface built with Vue.js
- Responsive design for optimal user experience

## Architecture

The application consists of two main components: the backend and the frontend. 

- **Backend**: Built using FastAPI, the backend handles data uploads, processes the data, and returns predictions.
- **Frontend**: Developed with Vue.js, the frontend provides an interactive user interface for uploading files and displaying predictions.

![DataPredictor](https://github.com/user-attachments/assets/5b1d5d68-d12b-4169-9b5c-cb35ec01138a)


## Requirements

To run this project, you'll need the following:

- Python 3.8 or higher
- Node.js 14 or higher
- FastAPI
- PyCaret

## Application

### Backend with FastAPI

The backend is structured to handle data processing and predictions efficiently.

1. Navigate to the backend directory:

    ```bash
    cd D:\DataPredictor\backend
    ```

2. Create a virtual environment and install dependencies:

    ```bash
    python -m venv env
    # Activate the virtual environment:
    # Windows
    env\Scripts\activate
    # Linux/MacOS
    source env/bin/activate
    pip install -r requirements.txt
    ```

### Frontend with Vue.js

The frontend is designed to be responsive and user-friendly.

1. Navigate to the frontend directory:

    ```bash
    cd D:\DataPredictor\frontend
    ```

2. Install the necessary Node.js packages:

    ```bash
    npm install
    ```

## Usage Instructions

To use the application, follow these steps:

1. **Clone the repository**

    ```bash
    git clone https://github.com/pablosierrafernandez/DataPredictor.git
    ```

2. **Set up the backend** by following the instructions in the [Backend with FastAPI](#backend-with-fastapi) section.

3. **Set up the frontend** by following the instructions in the [Frontend with Vue.js](#frontend-with-vuejs) section.

4. **Start the backend server**

    ```bash
    uvicorn main:app --reload
    ```

5. **Start the frontend development server**

    ```bash
    npm run serve
    ```

6. **Access the application**

    Open your browser and navigate to `http://localhost:8080` to use the application.


## Contributions

Contributions are welcome! Please follow the [contributing guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).  
See the `LICENSE` file for details.

## Authors

*   [@pablosierrafernandez](https://github.com/pablosierrafernandez): Developer of the project.



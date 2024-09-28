# Import necessary libraries and modules
from fastapi import FastAPI, File, UploadFile, Form  
from fastapi.responses import JSONResponse  
import pandas as pd  
from fastapi.middleware.cors import CORSMiddleware  
from pycaret.classification import (
    setup as setup_classification, 
    compare_models as compare_models_classification, 
    predict_model as predict_model_classification
)  
from pycaret.regression import (
    setup as setup_regression, 
    compare_models as compare_models_regression, 
    predict_model as predict_model_regression
)  

# Initialize FastAPI app
app = FastAPI()

# Allowed origins for CORS (localhost settings)
origins = [
    "http://localhost:8080",  
    "http://127.0.0.1:8080",
]

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,  # Whether to allow credentials (cookies, HTTP authentication)
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers in requests
)

# Route to handle CSV file uploads
@app.post("/upload-csv/")
async def upload_csv(file: UploadFile = File(...)):
    """
    Endpoint to handle the uploading of a CSV file and return the column names.
    
    Parameters:
    - file: The uploaded CSV file.
    
    Returns:
    - A JSON object containing the column names of the CSV file.
    """
    df = pd.read_csv(file.file)  # Read CSV file into a DataFrame
    columns = df.columns.tolist()  # Get list of column names
    return {"columns": columns}  # Return column names as JSON

# Route to handle predictions based on the uploaded CSV and the provided target column
@app.post("/predict/")
async def predict_csv(
    target_column: str = Form(...),  # The name of the target column for prediction
    file: UploadFile = File(...),  # The uploaded CSV file
    columns: str = Form(...)  # A stringified dictionary representing the input data for prediction
):
    """
    Endpoint to handle predictions based on an uploaded CSV file and the provided target column.
    Determines whether the task is classification or regression based on the target column's data type.

    Parameters:
    - target_column: The target column in the CSV used for model training.
    - file: The uploaded CSV file.
    - columns: A stringified dictionary representing the input data for prediction.

    Returns:
    - A JSON response containing the predicted values.
    """
    
    # Read the uploaded CSV file into a DataFrame
    df = pd.read_csv(file.file)

    # Check if the target column exists in the DataFrame
    if target_column not in df.columns:
        return JSONResponse(status_code=400, content={"detail": "Column not found in CSV"})

    # Convert the stringified columns input into a dictionary
    columns_dict = eval(columns)

    # Determine if the task is regression or classification based on the target column data type
    if pd.api.types.is_numeric_dtype(df[target_column]):
        # If the target column is numeric, it's a regression task
        setup_regression(df, target=target_column, session_id=123)  # Set up regression environment
        best_model = compare_models_regression()  # Find the best regression model
        input_df = pd.DataFrame([columns_dict])  # Create a DataFrame from input data
        predictions = predict_model_regression(best_model, data=input_df)  # Make predictions

        # Filter relevant prediction fields for regression (only prediction label)
        filtered_predictions = predictions[['prediction_label']].to_dict(orient='records')

    else:
        # If the target column is not numeric, it's a classification task
        setup_classification(df, target=target_column, session_id=123)  # Set up classification environment
        best_model = compare_models_classification()  # Find the best classification model
        input_df = pd.DataFrame([columns_dict])  # Create a DataFrame from input data
        predictions = predict_model_classification(best_model, data=input_df)  # Make predictions
        print(predictions)
        
        # Filter relevant prediction fields for classification (prediction label and score)
        filtered_predictions = predictions[['prediction_label', 'prediction_score']].to_dict(orient='records')

    # Return the filtered predictions as a JSON response
    return JSONResponse(content=filtered_predictions)

import pandas as pd

#filepath = '/data/Climate_Change_Indicators.csv'
def load_and_clean_data(filepath):
    # Load the data
    df = pd.read_csv(filepath)
    
    # Check for missing values
    if df.isnull().sum().any():
        df = df.dropna()  # or handle missing data as needed
    
    # Return the cleaned DataFrame
    return df

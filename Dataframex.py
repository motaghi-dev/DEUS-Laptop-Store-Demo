import csv
import sys
import os
import pandas as pd
import ast


def dataframa(location="fetch_data.txt"):
    """
    Read laptop data from file and create a structured DataFrame.
    
    Args:
        location (str): Path to the data file
        
    Returns:
        pd.DataFrame: DataFrame containing laptop names, specs, and prices
    """
    # Read and parse the data file
    with open(location, "r", encoding="utf8") as file:
        input_string = file.read()
    data_dict = ast.literal_eval(input_string)

    # Create initial DataFrame from dictionary
    df = pd.DataFrame(data_dict.items(), columns=['Name', 'Laptop Specs and Price'])

    # Split specs and price into separate columns
    df[['Specs', 'Price']] = pd.DataFrame(
        df['Laptop Specs and Price'].tolist(), 
        index=df.index
    )
    
    return df.drop(columns=['Laptop Specs and Price'])


def filtered_dataframa(x):
    """
    Filter the laptop DataFrame based on user-provided conditions.
    
    Args:
        x (str): Filter conditions provided by user
        
    Returns:
        pd.DataFrame: Filtered DataFrame based on conditions
    """
    # Normalize user input for SQL-like query
    x = (x.replace('"', "'")
          .replace(" OR ", " or ")
          .replace(" AND ", " and "))
    
    tokens = x.split()
    
    # Convert atomic conditions to pandas query format
    for i in range(len(tokens)):
        if tokens[i] == "in":
            query = f"{tokens[i+1]}.str.contains('{tokens[i-1]}', case=False)"
            query = query.replace("''", "'")
            tokens[i-1:i+2] = ["", "", query]
            
        if tokens[i] in (">", "<", ">=", "<=", "=="):
            query = f"{tokens[i-1]} {tokens[i]} {tokens[i+1]}"
            tokens[i-1:i+2] = ["", "", query]
    
    # Build the query string and apply to DataFrame
    df = dataframa()
    query_str = " ".join(token for token in tokens if token)
    
    return df.query(query_str)

import pandas as pd

# Load dataset
def load_data(file):
    try:
        df = pd.read_csv(file)
        print("Dataset Loaded Successfully\n")
        return df
    except FileNotFoundError:
        print("File not found!")
        return None

# Main function
def clean_transform_data():
    df = load_data("hr_data.csv")

    if df is None:
        return

    print("Original Data:\n", df)

    # 1. Handle Missing Values (replace with mean for numeric columns)
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    for col in numeric_cols:
        df[col].fillna(df[col].mean(), inplace=True)

    # 2. Remove Duplicate Rows
    df.drop_duplicates(inplace=True)

    # 3. Convert Date column to proper format (if exists)
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # 4. Example: Convert Salary column to numeric (if needed)
    if 'Salary' in df.columns:
        df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')

    print("\nCleaned Data:\n", df)

    # Save cleaned data
    df.to_csv("cleaned_hr_data.csv", index=False)
    print("\nCleaned data saved to 'cleaned_hr_data.csv'")

# Run program
clean_transform_data()

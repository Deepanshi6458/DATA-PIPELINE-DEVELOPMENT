import pandas as pd

def extract_data():
    df = pd.read_csv("data.csv")
    return df

def transform_data(df):
    df = df.dropna()
    return df

def load_data(df):
    print("cleaned data:")
    print(df)

if __name__ == "__main__":
    data = extract_data()
    cleaned_data = transform_data(data)
    load_data(cleaned_data)    


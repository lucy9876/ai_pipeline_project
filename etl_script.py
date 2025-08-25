import pandas as pd

def simple_etl(input_file, output_db):
    df = pd.read_csv(input_file)
    df = df.dropna()
    if df.empty:
        raise ValueError("No data after cleaning")

    df.to_sql('processed_data', 'sqlite:///' + output_db, if_exists='replace')
    print(f"Data saved to {output_db}")

if __name__ == "__main__":
    simple_etl('sample_data.csv', 'output.db')
import pandas as pd

def fetch_data(source):
    # Function to fetch data from the source
    data = pd.read_csv(source)
    return data

def save_data(data, filename):
    data.to_csv(filename, index=False)

if __name__ == "__main__":
    data = fetch_data('path/to/data/source')
    save_data(data, 'data/data.csv')


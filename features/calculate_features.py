import pandas as pd

def calculate_features(data):
    data['Feature1'] = data['Column1'].rolling(window=10).mean()
    data['Feature2'] = data['Column2'].rolling(window=50).mean()
    data = data.dropna()
    return data

if __name__ == "__main__":
    data = pd.read_csv('data/data.csv')
    features = calculate_features(data)
    features.to_csv('data/features.csv', index=False)


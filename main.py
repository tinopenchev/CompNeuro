import data.fetch_data as fetch
import features.calculate_features as calc
import models.train_model as train

def main():
    data = fetch.fetch_data('path/to/data/source')
    fetch.save_data(data, 'data/data.csv')
    
    data = pd.read_csv('data/data.csv')
    features = calc.calculate_features(data)
    features.to_csv('data/features.csv', index=False)

    data = pd.read_csv('data/features.csv')
    features = ['Feature1', 'Feature2']
    X = data[features]
    y = data['Target']
    train.train_model(X, y)

if __name__ == "__main__":
    main()


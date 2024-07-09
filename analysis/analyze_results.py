import pandas as pd

def analyze_results(data):
    summary = data.describe()
    correlation = data.corr()
    return summary, correlation

if __name__ == "__main__":
    data = pd.read_csv('data/features.csv')
    summary, correlation = analyze_results(data)
    print("Summary:\n", summary)
    print("\nCorrelation:\n", correlation)


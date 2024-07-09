import pandas as pd
import matplotlib.pyplot as plt

def visualize_data(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Timestamp'], data['EEG'], label='EEG')
    plt.plot(data['Timestamp'], data['MEG'], label='MEG')
    plt.xlabel('Time')
    plt.ylabel('Signal')
    plt.title('EEG and MEG Data')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    data = pd.read_csv('data/features.csv')
    visualize_data(data)


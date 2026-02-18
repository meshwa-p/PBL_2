import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_and_preprocess(path):
    df = pd.read_csv(path)

    X = df.drop("label", axis=1)
    y = df["label"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y


if __name__ == "__main__":
    X, y = load_and_preprocess("../data/sample_dataset.csv")
    print("Preprocessing completed successfully.")

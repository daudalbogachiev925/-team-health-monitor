import argparse
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

def train(data_path: str, out_path: str):
    df = pd.read_csv(data_path)
    X = df[["engagement", "burnout", "workload", "conflicts"]]
    y = df["churn"]

    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=300, max_depth=8, random_state=42)
    model.fit(X_tr, y_tr)

    auc = roc_auc_score(y_te, model.predict_proba(X_te)[:, 1])
    print(f"ROC AUC: {auc:.3f}")

    joblib.dump(model, out_path)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--data", required=True)
    p.add_argument("--out", required=True)
    args = p.parse_args()
    train(args.data, args.out)

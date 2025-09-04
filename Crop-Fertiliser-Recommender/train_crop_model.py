import os
import json
import joblib
import pandas as pd
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

# 2) Paths
DATA_PATH = Path("data/crop_recommendation.csv")   # your dataset
MODELS_DIR = Path("models")
MODELS_DIR.mkdir(parents=True, exist_ok=True)

MODEL_FILE = MODELS_DIR / "crop_model.pkl"
META_FILE = MODELS_DIR / "crop_targets.json"
REPORT_FILE = MODELS_DIR / "training_report.txt"

# 3) Load dataset
print(f"📂 Loading dataset from {DATA_PATH} ...")
df = pd.read_csv(DATA_PATH)

# Check columns
required_cols = ["N","P","K","temperature","humidity","ph","rainfall","label"]
assert set(required_cols).issubset(df.columns), \
       f"Dataset missing required columns! Found: {df.columns}"

# 4) Split into features and labels
FEATURES = ["N","P","K","temperature","humidity","ph","rainfall"]
X = df[FEATURES]
y = df["label"]

# 5) Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 6) Train RandomForest (simple params for speed)
print("🌱 Training RandomForest model...")
model = RandomForestClassifier(
    n_estimators=300, max_depth=None, random_state=42, n_jobs=-1
)
model.fit(X_train, y_train)

# 7) Evaluate
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)

# Use string report for now; can switch to dict if needed
report = classification_report(y_test, y_pred)  # string
print(f"✅ Accuracy: {acc:.4f}")

# Save training report (type-safe)
with open(REPORT_FILE, "w") as f:
    f.write(f"Accuracy: {acc:.4f}\n\n")
    if isinstance(report, dict):
        f.write(json.dumps(report, indent=4))
    else:
        f.write(report)

# 8) Fertilizer targets (avg NPK per crop)
print("🧪 Computing fertilizer targets (avg NPK per crop)...")
fertilizer_targets = (
    df.groupby("label")[["N","P","K"]]
    .mean()
    .round(2)
    .to_dict(orient="index")
)

with open(META_FILE, "w") as f:
    json.dump(fertilizer_targets, f, indent=2)

# 9) Save trained model
joblib.dump(model, MODEL_FILE)

print(f"✅ Model saved to {MODEL_FILE}")
print(f"📄 Fertilizer targets saved to {META_FILE}")
print(f"📊 Training report saved to {REPORT_FILE}")

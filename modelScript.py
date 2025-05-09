import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib

df = pd.read_csv("trainData3.csv")

# Compute required features
df["health_difference"] = df["Player1_health"] - df["Player2_health"]
df["distance_x"] = df["Player2_x"] - df["Player1_x"]
df["distance_y"] = df["Player2_y"] - df["Player1_y"]

# Select only required input features
input_features = [
    "Player1_ID",
    "Player2_ID",
    "health_difference",
    "Player2_up", "Player2_down", "Player2_right", "Player2_left",
    "Player2_Y", "Player2_B", "Player2_X", "Player2_A", "Player2_L", "Player2_R",
    "distance_x", "distance_y"
]

# Ensure inputs are integers
df[input_features] = df[input_features].astype(int)

# Output labels (multi-label classification)
output_labels = [
    "Player1_up", "Player1_down", "Player1_right", "Player1_left",
    "Player1_Y", "Player1_B", "Player1_X", "Player1_A", "Player1_L", "Player1_R"
]

df[output_labels] = df[output_labels].astype(int)

# Split dataset
X = df[input_features]
y = df[output_labels]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
base_model = RandomForestClassifier(n_estimators=100, random_state=42)
multi_model = MultiOutputClassifier(base_model)
multi_model.fit(X_train, y_train)

# Evaluate
y_pred = multi_model.predict(X_test)
print(classification_report(y_test, y_pred, zero_division=0))

# Exact match accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Exact Match Accuracy: {accuracy:.4f}")

# Save model
joblib.dump(multi_model, "street_fighter_model3.pkl")
print("📦 Model saved as 'street_fighter_model3.pkl'")

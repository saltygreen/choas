import pandas as pd
import joblib   
from sklearn.model_selection import train_test_split
from sklearn.esemble import RandomForestClassifier
from sklearn.metrics import accuracy_score



# Load game data
data = pd.read_races.py('races_stats')
# save the trained model
joblib.dump(model, 'monstars_stats_model')
# load and use the model in the game scripts
model = joblib.load('monstars_stats_model')

# Split dat in feartures (x) and target (y)
x = data[['Attack', 'block_with_shield', 'parry_with_sword_or_dagger']]
y = data['monstars_action'] # Target variable

# Split data into training and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Train a RandomForestClassifier
model = RandomForestClassifier()
model.fit(x_train, y_train)

# Evaluate the model
y_pred = model.predict(x_test)
print('Accuracy:', accuracy_score(y_test, y_pred))


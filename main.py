#This is a main py file you have to run for model training

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Load the dataset
df = pd.read_csv('synthetic_seed_dropping_dataset.csv')

# Encoding categorical features
label_encoder = LabelEncoder()
df['Obstacle_Present'] = label_encoder.fit_transform(df['Obstacle_Present'])
df['Water_Body'] = label_encoder.fit_transform(df['Water_Body'])
df['Soil_Type'] = label_encoder.fit_transform(df['Soil_Type'])

# Selecting features (X) and target (y)
X = df[['Obstacle_Present', 'Water_Body', 'Soil_Type', 'Vegetation_Density (%)']]
y = df['Label']

# Splitting the dataset into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initializing the Random Forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Training the model
clf.fit(X_train, y_train)

# Making predictions on the test set
y_pred = clf.predict(X_test)

# Evaluating model performance
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

#Take new data to check is it suitable or not
# New data point for prediction with feature names
new_data = pd.DataFrame([[0, 0, 1, 50]], columns=['Obstacle_Present', 'Water_Body', 'Soil_Type', 'Vegetation_Density (%)'])

# Make a prediction
prediction = clf.predict(new_data)

# Check if suitable for seed dropping
if prediction[0] == 1:
    print("Area is suitable for seed dropping")
else:
    print("Area is not suitable for seed dropping")


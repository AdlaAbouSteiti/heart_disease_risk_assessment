# Instal necessary libraries
pip install pandas
pip install matplotlib.pyplot

# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt

# the path to csv file
file_path = 'C:\Users\GOTECH\Documents\Heart.csv'

# Load the dataset
data = pd.read_csv(file_path)

# print the first few raws to ensure loaded well
print(data.head())

# Create categories for BMI
data['BMI_Category'] = pd.cut(data['BMI'], bins=[0, 18.5, 25, 30, float('inf')], labels=['Underweight', 'Normal', 'Overweight', 'Obese'])

# Create categories for blood pressure
data['BloodPressure_Category'] = pd.cut(data['ap_hi'], bins=[0, 120, 130, 140, float('inf')], labels=['Normal', 'Elevated', 'Stage 1 Hypertension', 'Stage 2 Hypertension'])

# Display the updated DataFrame
print(data.head())

# Define the features
X = data[['BMI_Category', 'BloodPressure_Category', 'cholesterol']]
y = data['cardio']

# Convert categorical variables to dummy/indicator variables
X = pd.get_dummies(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the Decision Tree Classifier
clf = DecisionTreeClassifier()

# Train the classifier with the training data
clf.fit(X_train,y_train)

# Make predictions on the test data
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# Print the classification report
print('Classification Report:')
print(classification_report(y_test, y_pred))

# Print the confusion matrix
print('Confusion Matrix:')
print(confusion_matrix(y_test, y_pred))

# Plot the decision tree
plt.figure(figsize=(20, 10))
plot_tree(clf, filled=True, feature_names=X.columns, class_names=['No Heart Disease', 'Heart Disease'])
plt.show()


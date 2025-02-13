from sklearn.metrics import confusion_matrix
from modeltraining import clf,X_test,y_test

# Predict on the test set
y_test_pred = clf.predict(X_test)

# Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_test_pred)
print("Confusion Matrix:\n", conf_matrix)

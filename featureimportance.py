import matplotlib.pyplot as plt
import numpy as np
from modeltraining import clf

# Get feature importance
feature_importances = clf.feature_importances_

# Plot feature importance
feature_names = ['Obstacle_Present', 'Water_Body', 'Soil_Type', 'Vegetation_Density (%)']
plt.barh(feature_names, feature_importances)
plt.xlabel("Feature Importance")
plt.title("Feature Importance in Seed Dropping Model")
plt.show()

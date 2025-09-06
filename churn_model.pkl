import pickle
from google.colab import files

# Save model as churn_model.pkl
with open("churn_model.pkl", "wb") as f:
    pickle.dump(model, f)

# Download to your laptop
files.download("churn_model.pkl")

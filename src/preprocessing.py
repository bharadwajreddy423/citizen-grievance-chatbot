import pandas as pd
import json
import os

# Define dataset path
DATASET_PATH = os.path.join("data", "synthetic_grievances.json")

def load_dataset(file_path):
    """Loads the grievance dataset from a JSON file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataset file not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Debugging: Print first record to check field names
    print(" First Record:", data[0])

    return pd.DataFrame(data)  # Convert JSON to DataFrame


def preprocess_data(df):
    """Preprocesses the complaint data."""
    
    #  Rename 'description' → 'complaint_text' for consistency
    df.rename(columns={"description": "complaint_text"}, inplace=True)
    
    
    df["complaint_text"] = df["complaint_text"].str.strip()
    
    # Other preprocessing steps...
    return df


if __name__ == "__main__":
    print("Loading dataset...")
    df = load_dataset(DATASET_PATH)
    
    print("Preprocessing dataset...")
    df = preprocess_data(df)

    print(f" Dataset loaded & processed: {df.shape[0]} records")
    print(df.head())  # Print first few records




# Load the dataset
df = pd.read_json("../data/synthetic_grievances.json")  # Update path if needed

# Extract unique categories
unique_categories = df["category"].unique()

# Print the categories
print("Unique Complaint Categories:", unique_categories)

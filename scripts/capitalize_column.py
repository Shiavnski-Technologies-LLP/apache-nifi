import pandas as pd
import os

# Function to capitalize a specific column in CSV
def capitalize_column(input_file, output_file, column_name="Occupation"):
    try:
        # Check if input file exists
        if not os.path.exists(input_file):
            print(f"Error: File {input_file} not found!")
            return

        # Read CSV file
        df = pd.read_csv(input_file)

        # Capitalize the specified column
        if column_name in df.columns:
            df[column_name] = df[column_name].str.upper()
        else:
            print(f"Warning: Column '{column_name}' not found in CSV!")

        # Save the processed file
        df.to_csv(output_file, index=False)
        print(f"Success: Column '{column_name}' capitalized and saved to {output_file}")

    except Exception as e:
        print(f"Error processing file: {e}")

if __name__ == "__main__":
    input_path = "../data/input/anxiety_attack_dataset.csv"
    output_path = "../data/output/processed_data.csv"
    
    capitalize_column(input_path, output_path)

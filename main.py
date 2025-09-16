import pandas as pd
import json
import os

# Folder containing your 19 JSON files
folder_path = "json"   # change to your folder path
output_folder = "output_csv"
os.makedirs(output_folder, exist_ok=True)

encodings = ["utf-8", "utf-16", "ascii", "latin1"]

def read_json_with_encodings(file_path):
    """Try different encodings and return loaded JSON data"""
    for enc in encodings:
        try:
            with open(file_path, "r", encoding=enc) as f:
                return json.load(f), enc
        except UnicodeDecodeError:
            continue
        except Exception as e:
            print(f"⚠️ Error reading {file_path} with {enc}: {e}")
    return None, None

all_dataframes = []

for file_name in os.listdir(folder_path):
    if file_name.endswith(".json"):
        file_path = os.path.join(folder_path, file_name)
        print(f"\n📂 Processing {file_name}...")

        data, used_enc = read_json_with_encodings(file_path)

        if data:
            print(f"✅ Successfully read with encoding: {used_enc}")
            
            # Flatten JSON
            df = pd.json_normalize(data)

            # Add length columns
            df["subject_length"] = df["subject"].apply(lambda x: len(x) if isinstance(x, str) else 0)
            df["description_length"] = df["description"].apply(lambda x: len(x) if isinstance(x, str) else 0)
            df["resolution_length"] = df["resolution"].apply(lambda x: len(x) if isinstance(x, str) else 0)
            df["resolution_steps_length"] = df["resolution_steps"].apply(lambda x: len(x) if isinstance(x, list) else 0)

            # Save individual CSV
            csv_path = os.path.join(output_folder, file_name.replace(".json", ".csv"))
            df.to_csv(csv_path, index=False, encoding="utf-8")
            print(f"💾 Saved as {csv_path}")
            
            all_dataframes.append(df)
        else:
            print(f"❌ Could not read {file_name}")

# Merge all into one DataFrame
if all_dataframes:
    final_df = pd.concat(all_dataframes, ignore_index=True)
    final_df.to_csv("all_tickets.csv", index=False, encoding="utf-8")
    print("\n✅ All JSON files merged into 'all_tickets.csv'")

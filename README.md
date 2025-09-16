# JSON to DataFrame Converter

This project automates the process of reading multiple JSON files, handling different encodings, flattening nested JSON structures, and converting them into Pandas DataFrames. It also adds useful metadata such as the length of text fields and number of resolution steps.  

---

## 🚀 Features
- Reads multiple JSON files from a folder.
- Handles multiple encodings (`utf-8`, `utf-16`, `ascii`, `latin1`) with exception handling.
- Flattens nested JSON structures (e.g., `user.name`, `user.department`).
- Adds new columns for:
  - **`subject_length`** → number of characters in the subject
  - **`description_length`** → number of characters in the description
  - **`resolution_length`** → number of characters in the resolution
  - **`resolution_steps_length`** → number of steps in the resolution steps list
- Saves individual CSV files for each JSON file.
- Merges all DataFrames into a single `all_tickets.csv`.

---

## 📂 Project Structure
json-to-dataframe/
│── json_files/ # your JSON input files
│── output_csv/ # generated CSV files (ignored in Git)
│── process_jsons.py # Python script
│── requirements.txt # Python dependencies
│── .gitignore
│── README.md

---

## 🛠 Requirements
Install dependencies before running:

```bash
pip install -r requirements.txt
Minimum dependencies:

pandas

▶️ Usage

Place all JSON files inside the json_files/ folder.

Run the script:

python process_jsons.py


Output:

Individual CSV files for each JSON file inside output_csv/.

A merged all_tickets.csv file with all data combined.

📝 Example Output

For a JSON ticket file, you’ll get a DataFrame like this:

ticket_id	priority	subject	subject_length	description_length	resolution_length	resolution_steps_length
TKT-006	HIGH	Backup Data Corruption	23	156	54	6
📌 Next Steps

Optionally expand tags and resolution_steps into separate rows for advanced analysis.

Extend script to support nested directories or other file formats.

👩‍💻 Author: SUPRIYA CM
🔗 Repo:https://github.com/Sypriya/json_to_dataframe
# journal_utils.py

import json
from datetime import datetime

# Load all saved journal entries
def load_entries(file_path='storage.json'):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save a new journal entry to the JSON file
def save_entry(entry, file_path='storage.json'):
    entries = load_entries(file_path)
    entries.append(entry)
    with open(file_path, 'w') as file:
        json.dump(entries, file, indent=4)

# Format and print all journal entries
def display_entries(entries):
    print("\n🗓️  Your Journal Entries:\n")
    for entry in entries:
        print(f"Date: {entry['timestamp']}")
        print(f"Mood: {entry['sentiment']}")
        print(f"Entry: {entry['text']}\n{'-'*40}")
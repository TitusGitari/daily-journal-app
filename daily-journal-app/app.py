# app.py

from journal_utils import save_entry, load_entries, display_entries
from sentiment import analyze_sentiment
from datetime import datetime

def main():
    print("\n📔 Welcome to Your Daily Journal!")
    print("1. Write a new entry")
    print("2. View past entries")
    choice = input("Select an option (1 or 2): ")

    if choice == '1':
        # Ask user to write a journal entry
        entry_text = input("\nWhat's on your mind today?\n> ")
        sentiment = analyze_sentiment(entry_text)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Create the entry object
        entry = {
            "text": entry_text,
            "sentiment": sentiment,
            "timestamp": timestamp
        }

        save_entry(entry)
        print(f"\n✅ Entry saved! Mood detected: {sentiment}")

    elif choice == '2':
        # Display past entries
        entries = load_entries()
        if entries:
            display_entries(entries)
        else:
            print("\nNo entries found yet.")
    else:
        print("❌ Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()

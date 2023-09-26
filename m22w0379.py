# student Id: M22W0379
# Name: Kanwar Prashant
# Topic: Digital Diary Management System
# Final Project
# Computer programming python

import datetime


class Entry:
    # Initialize the Entry object with the given date and content
    def __init__(self, date, content):
        self.date = date
        self.content = content


class Diary:
    # Initialize the Diary object with an empty list for entries

    def __init__(self):
        # Create an attribute 'entries' and assign an empty list to it
        self.entries = []

    def add_entry(self, entry):
        self.entries.append(entry)
        print("Entry added to the diary.")

    def view_entries(self):
        if self.entries:
            print("All Diary notes:")
            for entry in self.entries:
                print(f"Date: {entry.date}")
                print(f"Content: {entry.content}")
                print("-----------------------")
        else:
            print("Diary is empty.")

    def search_entries(self, keyword):
        # Create an empty list to store found entries that match the keyword.
        found_entries = []
        # Loop through each entry in the diary's list of entries.
        for entry in self.entries:
            # Check if the lowercase version of the keyword is present in the lowercase content of the entry.
            if keyword.lower() in entry.content.lower():
                found_entries.append(entry)
        # Check if any entries were found.
        if found_entries:
            # If entries were found, display the count and details of each found entry.
            print(f"Found {len(found_entries)} entries matching '{keyword}':")
            for entry in found_entries:
                print(f"Date: {entry.date}")
                print(f"Content: {entry.content}")
                print("-----------------------")
        else:
            print(f"No entries found matching '{keyword}'.")

    def edit_entry(self, keyword):
        found_entries = []
        for entry in self.entries:
            if keyword.lower() in entry.content.lower():
                # If the keyword is found in the content, add the entry to the list of found_entries.
                found_entries.append(entry)

        if found_entries:
            # If entries were found, display the count and details of each found entry.
            print(f"Found {len(found_entries)} entries matching '{keyword}':")
            for i, entry in enumerate(found_entries):
                print(f"{i + 1}. Date: {entry.date}")
                print(f"   Content: {entry.content}")
                print("-----------------------")

            entry_choice = int(input("Enter the entry number to edit: "))
            # Check if the user input is within a valid range of entries.
            if 1 <= entry_choice <= len(found_entries):
                # If the input is valid, prompt the user to enter the new content for the selected entry.
                new_content = input("Enter the new content for the entry: ")
                # Update the content of the selected entry with the new content.
                found_entries[entry_choice - 1].content = new_content
                print("Entry edited successfully.")
            else:
                print("Invalid entry number!")
        else:
            print(f"No entries found matching '{keyword}'.")

    def delete_entry(self, keyword):
        found_entries = []
        for entry in self.entries:
            if keyword.lower() in entry.content.lower():
                found_entries.append(entry)
        if found_entries:
            print(f"Found {len(found_entries)} entries matching '{keyword}':")
            for i, entry in enumerate(found_entries):
                print(f"{i + 1}. Date: {entry.date}")
                print(f"   Content: {entry.content}")
                print("-----------------------")

            entry_choice = int(input("Enter the number of the entry to delete: "))
            if 1 <= entry_choice <= len(found_entries):
                entry_to_delete = found_entries[entry_choice - 1]
                self.entries.remove(entry_to_delete)
                print("Entry deleted successfully.")
            else:
                print("Invalid entry number.")
        else:
            print(f"No entries found matching '{keyword}'.")


def main():
    diary = Diary()

    while True:
        print("\nMenu:")
        print("1. Add note")
        print("2. View notes")
        print("3. Search from notes")
        print("4. Edit note")
        print("5. delete note")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")
        # Add note
        if choice == "1":
            content = input("write your note: ")
            entry = Entry(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), content)
            diary.add_entry(entry)
        # View notes
        elif choice == "2":
            diary.view_entries()
        # Search note from diary
        elif choice == "3":
            keyword = input("Enter the keyword to search: ")
            diary.search_entries(keyword)
        #Edit note from diary
        elif choice == "4":
            keyword = input("Enter the keyword to search for the entry to edit: ")
            diary.edit_entry(keyword)
        #delete note
        elif choice == "5":
            keyword = input("Enter the keyword to search for the entry to delete: ")
            diary.delete_entry(keyword)
        elif choice == "6":  # Exit
            break

        else:
            print("Invalid choice!")

    print("Thank you for using the Digital Diary!")


if __name__ == "__main__":
    main()

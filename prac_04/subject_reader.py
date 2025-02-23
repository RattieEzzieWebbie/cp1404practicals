"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subject_details(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students.
    If the file is empty or doesn't exist, load predefined data."""
    subjects = []

    try:
        with open(FILENAME) as input_file:
            for line in input_file:
                line = line.strip()
                parts = line.split(',')
                parts[2] = int(parts[2])  # Convert student count to integer
                subjects.append(parts)
    except FileNotFoundError:
        print(f"File {FILENAME} not found. Loading predefined data.")
        # Predefined data if file is missing or empty
        subjects = [
            ["CP1401", "Ada Lovelace", 192],
            ["CP1404", "Alan Turing", 98],
            ["CP4321", "Bill Gates", 676],
            ["CP1234", "Steve Jobs", 123]
        ]

    return subjects


def display_subject_details(subjects):
    """Display formatted subject details."""
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")


main()

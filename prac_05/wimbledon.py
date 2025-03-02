"""
Wimbledon Data Processing
Estimate: 30 minutes
Actual:   25 minutes
"""

FILENAME = "wimbledon.csv"

def read_wimbledon_data(filename):
    """Read Wimbledon data from a CSV file and return a list of matches."""
    with open(filename, "r", encoding="utf-8-sig") as file:
        lines = file.readlines()[1:]  # Skip header line
    return [line.strip().split(",") for line in lines]

def process_wimbledon_data(data):
    """Process data to extract champion counts and their countries."""
    champion_counts = {}
    champion_countries = set()

    for match in data:
        champion, country = match[2], match[1]  # Winner and their country
        champion_counts[champion] = champion_counts.get(champion, 0) + 1
        champion_countries.add(country)

    return champion_counts, champion_countries

def display_results(champion_counts, champion_countries):
    """Display champions and the number of times they have won, and the sorted countries."""
    print("Wimbledon Champions:")
    for champion, wins in sorted(champion_counts.items()):
        print(f"{champion} {wins}")

    print("\nThese", len(champion_countries), "countries have won Wimbledon:")
    print(", ".join(sorted(champion_countries)))

def main():
    """Main function to run the Wimbledon data processing program."""
    data = read_wimbledon_data(FILENAME)
    champion_counts, champion_countries = process_wimbledon_data(data)
    display_results(champion_counts, champion_countries)

if __name__ == "__main__":
    main()
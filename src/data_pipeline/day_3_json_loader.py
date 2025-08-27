import json #import json module to handle JSON files

# Import functions from day2_deck_stats.py
from day2_deck_stats import deck_analysis, avg_elxr, count_types, count_rarity

# Path to the JSON file containing the deck data
DECK_FILE="../../data/raw/deck.json"

with open(DECK_FILE, 'r') as file:
    cards = json.load(file)  # Load the JSON data into a Python list
    deck_analysis(cards)  # Perform deck analysis using the imported function

    cards.append({"name": "Fireball", "elixir": 4, "type": "Spell", "Rarity": "Rare"})

# Save back
with open(DECK_FILE, "w") as f:
    json.dump(cards, f, indent=4)

print(cards)  # Print the list of cards to the console
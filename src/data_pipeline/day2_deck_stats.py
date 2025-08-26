Deck=[
    {"name":"Hog Rider","Elixir": 4,"Type":"Win Condition","Rarity":"Rare"},
    {"name":"Musketeer","Elixir": 4,"Type":"Ranged Support","Rarity":"Rare"},
    {"name":"Cannon","Elixir": 3,"Type":"Defensive Building","Rarity":"Common"},
    {"name":"Log","Elixir": 2,"Type":"Spell","Rarity":"Legendary"},
    {"name":"Fireball","Elixir": 4,"Type":"Spell","Rarity":"Rare"},
    {"name":"Skeletons","Elixir": 1,"Type":"Cycle","Rarity":"Common"},
    {"name":"Ice Spirit","Elixir": 1,"Type":"Cycle","Rarity":"Common"},
    {"name":"Fireball","Elixir": 3,"Type":"Ranged Support","Rarity":"Common"}    
]

#count avg elix in the deck
def avg_elxr(deck):
    average_elixir=0
    for card in deck:
        average_elixir+=card['Elixir']

    return (average_elixir/len(deck))

#count each type of cards in the deck
def count_types(deck):
    types_count={}
    for card in deck:
        t=card['Type']
        types_count[t]= types_count.get(t ,0)+1
    return types_count

#count the rarity of each card in deack
def count_rarity(deck):
    rarity_count={}
    for card in deck:
        r=card["Rarity"]
        rarity_count[r]=rarity_count.get(r , 0)+1
    return(rarity_count)

#present a analysis of the deck(avg elixir,count,etc...)
def deck_analysis(deck):
    print(f"The Average Elixir Cost in the Deck : {avg_elxr(deck)}")
    print(f"Types of Card in Deck :\n{count_types(deck)}")
    print(f"The Rarity in the deck : \n{count_rarity(deck)}")


deck_analysis(Deck)
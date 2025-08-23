cards=[
    {"name":"Knight","elixir":3,"type":"Ground Troop","Rarity":"Common"},
    {"name":"Prince","elixir":5,"type":"Ground Troop","Rarity":"Epic"},
    {"name":"Knight","elixir":3,"type":"Ground Troop","Rarity":"Common"},
    {"name":"Mini P.E.K.K.A","elixir":4,"type":"Ground Troop","Rarity":"Rare"},
    {"name":"Minions","elixir":3,"type":"Air Troop","Rarity":"Common"}

]


'''
for card in cards:
    for key in card:
        if key=="name":
            print(card[key],"\t")
        elif key=="elixr":
            print(card[key])
tried to loop but is inefficient
'''

#cleaner approach
for card in cards:
    print(f"Troop:{card['name']:<10}\t\t\tCost:{card['elixir']}")

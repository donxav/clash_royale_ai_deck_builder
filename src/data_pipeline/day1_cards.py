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
def card_display(cards):
    for card in cards:
        print(f"Troop:{card['name']:<10}\t\t\tCost:{card['elixir']}")


#funtion to delete cards
def del_card(cards,name):
    for card in cards:
        if card['name']==name:
            cards.remove(card)
            break #stop after one match 

card_display(cards)
del_card(cards,"Knight")
print(" ")
card_display(cards)

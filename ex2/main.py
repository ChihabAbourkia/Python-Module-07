from .EliteCard import EliteCard

card  = EliteCard("Arcane Warrior", 4,"Rare", 5, 20 , 4)

print("=== DataDeck Ability System ===\n")
print("EliteCard capabilities:")
print("""- Card: ['play', 'get_card_info', 'is_playable']
- Combatable: ['attack', 'defend', 'get_combat_stats']
- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']\n""")

print("Playing Arcane Warrior (Elite Card):\n")
print("Attack result: ", card.attack("Enemy"))
print("Defense result:", card.defend(5))

print("\nMagic phase:")
print("Spell cast:" , card.cast_spell("Fireball", ['Enemy1', 'Enemy2']))
print("Mana channel:", card.channel_mana(3))

print("\nMultiple interface implementation successful!")



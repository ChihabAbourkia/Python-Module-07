from .Deck import Deck
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard
from ex0.CreatureCard import CreatureCard

print("=== DataDeck Deck Builder ===\n")
print("Building deck with different card types...")
fire_dragon = CreatureCard(
    "Fire Dragon",
    5,
    "Legendary",
    7,
    5
)
mana_crystal = ArtifactCard(
    "Mana Crystal",
    4,
    "Rare",
    5,  
    "Permanent: +1 mana per turn"
)
lightning_bolt = SpellCard(
    "Lightning Bolt",
    3,
    "Common",
    "Deal 3 damage to target"
)
deck = Deck()

deck.add_card(fire_dragon)
deck.add_card(lightning_bolt)
deck.add_card(mana_crystal)

print("Deck stats:" , deck.get_deck_stats())

print("\nDrawing and playing cards:\n")


while True:
    card = deck.draw()
    if card is None:
        break
    info = card.get_card_info()
    print("Drew:", card.name, f"({info['type']})")
    print("Play result", card.play({"available_mana" : 20}),"\n")

print("Polymorphism in action: Same interface, different card behaviors!")
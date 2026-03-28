from .CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
import random


class FantasyCardFactory(CardFactory):

    def create_creature(self, name_or_power=None):
        if name_or_power == "dragon":
            return CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
        elif name_or_power == "goblin":
            return CreatureCard("Goblin Warrior", 2, "Common", 2, 2)
        else:
            return CreatureCard("Goblin Warrior", 2, "Common", 2, 2)

    def create_spell(self, name_or_power=None):
        if name_or_power == "fire":
            return SpellCard("Fireball", 4, "Common", "Deal 4 damage")
        elif name_or_power == "lightning":
            return SpellCard("Lightning Bolt", 3, "Common", "Deal 3 damage")
        else:
            return SpellCard("Lightning Bolt", 3, "Common", "Deal 3 damage")

    def create_artifact(self, name_or_power=None):
        if name_or_power == "ring":
            return ArtifactCard("Mana Ring", 2, "Rare", 5, "+1 mana")
        elif name_or_power == "staff":
            return ArtifactCard("Magic Staff", 3, "Rare", 6, "+2 mana")
        else:
            return ArtifactCard("Mana Ring", 2, "Rare", 5, "+1 mana")

    def create_themed_deck(self, size: int) -> dict:
        deck = []

        for _ in range(size):
            choice = random.choice(["creature", "spell", "artifact"])

            if choice == "creature":
                deck.append(self.create_creature(random.choice(["dragon", "goblin"])))
            elif choice == "spell":
                deck.append(self.create_spell(random.choice(["fire", "lightning"])))
            else:
                deck.append(self.create_artifact(random.choice(["ring", "staff"])))

        return {"deck": deck}

    def get_supported_types(self) -> dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fire", "lightning"],
            "artifacts": ["ring", "staff"]
        }
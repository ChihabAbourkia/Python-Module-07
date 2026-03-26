from ex0.Card import Card
class ArtifactCard(Card):   
    def __init__(self, name: str, cost: int, rarity: str, durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def get_card_info(self):
        info = super().get_card_info()
        info["durability"] = self.durability
        info["effect"] = self.effect
        info["type"] = "Artifact"
        return info

    def play(self, game_state: dict) -> dict:
        available_mana = game_state.get("available_mana", 0)
        if self.is_playable(available_mana):
            return{"card_played":self.name, "mana_used": self.cost, "effect": self.effect }
        else:
            return {"card_played":self.name, "mana_used": 0, "effect": None }

    def activate_ability(self) -> dict:
        return{ "effect" : self.effect, "durability_left": self.durability}
   
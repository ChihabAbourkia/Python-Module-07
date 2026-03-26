from ex0.Card import Card
class  SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
    
    def get_card_info(self):
        info = super().get_card_info()
        info["effect_type"] = self.effect_type
        info["type"] = "Spell"
        return info
    def play(self, game_state: dict) -> dict:
        available_mana = game_state["available_mana"]
        if self.is_playable(available_mana):
            return{"card_played":self.name, "mana_used": self.cost, "effect": self.effect_type }
        else:
            return {"card_played":self.name, "mana_used": 0, "effect": None }
    
    def resolve_effect(self, targets: list) -> dict:
        return {"effect" : self.effect_type , "targets" : targets, "resolved": True }

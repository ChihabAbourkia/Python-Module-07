from .Card import Card
class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, 
                 attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health
    
    def get_card_info(self):
       info =  super().get_card_info()
       info["type"] = "Creature"
       info["attack"] = self.attack
       info["health"] = self.health
       return info
    
    def play(self, game_state: dict) -> dict:
        available_mana = game_state.get("available_mana", 0)
        if self.is_playable(available_mana):
            return {"card_played":self.name, "mana_used": self.cost,
                     "effect": "Creature summoned to battlefield"}
        else:
            return {"card_played":self.name, "mana_used":0,
                     "effect": None}

    def attack_target(self, target) -> dict:
        return {"attacker": self.name, "target" : target, "damage_dealt" : self.attack,"combat_resolved" : True }  
from ex0.Card import Card
from  .Magical import Magical
from .Combatable import Combatable

class EliteCard(Card, Magical, Combatable ):
     def __init__(self, name: str, cost: int, rarity: str,attack_value: int, health: int, mana: int):
        super().__init__(name, cost, rarity)
        self.attack_value = attack_value
        self.health =health
        self.mana = mana

     def play(self, game_state: dict) -> dict:
        available_mana = game_state.get("available_mana", 0)
        if self.is_playable(available_mana):
            return{"card_played":self.name, "mana_used": self.cost }
        else:
            return {"card_played":self.name, "mana_used": 0}
     
     def attack(self, target) -> dict:
        return  {"attacker": self.name, "target": target,
                "damage": self.attack_value , "combat_type": "melee"}
    
     def defend(self, incoming_damage: int) -> dict:
        blocked_damage = 3
        damage_taken = incoming_damage - blocked_damage
        self.health -= damage_taken
        return  {"defender": self.name, "damage_taken": damage_taken,
              "damage_blocked": blocked_damage, 'still_alive': self.health > 0}
    
     def get_combat_stats(self) -> dict:
        return {"attack" : self.attack_value, "health": self.health}
     
     def cast_spell(self, spell_name: str, targets: list) -> dict:
        return  {"caster": self.name, "spell": spell_name,
                    "targets": targets, "mana_used": self.cost}
    
     def channel_mana(self, amount: int) -> dict:
            self.mana += amount 
            return {"channeled": amount, 'total_mana': self.mana}
    
     def get_magic_stats(self) -> dict:
        return{"mana" : self.mana} 
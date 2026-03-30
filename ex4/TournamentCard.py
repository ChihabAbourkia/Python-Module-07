from ex2.Combatable import Combatable
from ex0.Card import Card
from .Rankable import Rankable
class TournamentCard (Card  ,Combatable ,Rankable):
    def __init__(self, name: str, cost: int , rarity: str, id, rating, record, attack, win, losses )-> None:
        super().__init__(name, cost, rarity)
        self.id = id
        self.rating  = rating
        self.record = record
        self.win = 0
        self.losses = 0
        self.attack_value = attack
        
    def play(self, game_state: dict) -> dict:
        available_mana = game_state.get("available_mana", 0)
        if self.is_playable(available_mana):
            return{"card_played":self.name, "mana_used": self.cost }
        else:
            return {"card_played":self.name, "mana_used": 0}
        
    def attack(self, target) -> dict:
        return  {"attacker": self.name, "target": target,
				"damage": self.attack_value , "combat_type": "tournement"}
    
    def defend(self, incoming_damage: int) -> dict:
        blocked_damage = 3
        damage_taken = incoming_damage - blocked_damage
        self.health -= damage_taken
        return  {"defender": self.name, "damage_taken": damage_taken,
			"damage_blocked": blocked_damage, 'still_alive': self.health > 0}
    
    def calculate_rating(self) -> int:
        return self.rating
    
    def get_combat_stats(self) -> dict:
        return {"attack" : self.attack_value, "health": self.health}
    
    
    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += 16
    
    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating -= 16
	
    def get_rank_info(self) -> dict:
         return {
            'name': self.name,
            'rating': self.rating,
            'wins': self.wins,
            'losses': self.losses
        }
    
    
    def get_tournament_stats(self) -> dict:
        return {
			'name': self.name,
            'rating': self.rating,
            'record': f'{self.wins}-{self.losses}',
            'interfaces': ['Card', 'Combatable', 'Rankable']
		}
     
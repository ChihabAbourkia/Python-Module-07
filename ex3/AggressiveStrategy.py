
from .GameStrategy import GameStrategy
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cards_played = []
        mana_used = 0
        damage_dealt = 0
        for card in hand:
            cards_played.append(card.name)
            mana_used += card.cost
            if isinstance(card, CreatureCard):
                damage_dealt += card.attack
            elif isinstance(card,  SpellCard):
                damage_dealt += card.cost
        targets = self.prioritize_targets(battlefield)
        return {
            "strategy": self.get_strategy_name(),
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": targets,
            "damage_dealt": damage_dealt
        }
    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"
    
    def prioritize_targets(self, available_targets: list) -> list:
        player_targets = []
        other_targets = []
        for target in available_targets:
            enemy = str(target)
            if "Enemy player" in enemy.lower():
                player_targets.append(target)
            else:
                other_targets.append(target)
        return player_targets + other_targets

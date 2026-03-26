from ex0.Card import Card
import random

class Deck:
    def __init__(self):
            self.cards = []
    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
             if card.name == card_name:
                  self.cards.remove(card)
                  return True
        return False
    def shuffle(self) -> None:
         random.shuffle(self.cards)
    
    def draw(self):
         if  not self.cards:
              return None
         else:
              return self.cards.pop()
    
    def get_deck_stats(self) -> dict:
         total_cards = 0
         creatures = 0
         spells = 0
         artifacts = 0
         total_cost = 0
         for card in self.cards:
              info = card.get_card_info()
              if info["type"] == "Creature":
                creatures += 1
              elif info["type"] == "Spell":
                spells += 1
              elif info["type"] == "Artifact":
                artifacts += 1
              total_cost += info["cost"]
              total_cards +=1
         if total_cards > 0:
            avg_cost =  avg_cost = total_cost / total_cards     
         else:
            avg_cost = 0
         return {
                 "total_cards": total_cards,
                "creatures": creatures,
                "spells": spells,
                "artifacts": artifacts,
                "avg_cost": avg_cost
                }
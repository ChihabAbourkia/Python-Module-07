from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggressiveStrategy
from .GameEngine import GameEngine


print("=== DataDeck Game Engine ===")
print("Configuring Fantasy Card Game...")

# create engine + components
engine = GameEngine()
factory = FantasyCardFactory()
strategy = AggressiveStrategy()

# configure engine
engine.configure_engine(factory, strategy)

# show config
print("Factory:", factory.__class__.__name__)
print("Strategy:", strategy.get_strategy_name())
print("Available types:", factory.get_supported_types())

print("\nSimulating aggressive turn...")

# generate hand (for display)
deck_data = factory.create_themed_deck(3)
hand = deck_data["deck"]
# display hand like expected output
print("hand:" ,[f"{card.name} {card.cost}"for card in hand] )
# simulate turn
result = strategy.execute_turn(hand, ["Enemy Player"])
# print result
print("Turn execution:")
print("Strategy:", result["strategy"])
print("Actions:", {
    "cards_played": result["cards_played"],
    "mana_used": result["mana_used"],
    "targets_attacked": result["targets_attacked"],
    "damage_dealt": result["damage_dealt"]
})

# update engine manually (since we didn’t call simulate_turn here)
engine.turns += 1
engine.total_damage += result["damage_dealt"]
engine.cards_created += len(hand)

# final report
print("\nGame Report:")
print(engine.get_engine_status())

print("\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!")
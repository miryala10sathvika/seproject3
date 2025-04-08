from abc import ABC, abstractmethod

# --- Factory Pattern for Trading Scenarios ---
class TradingScenario(ABC):
    @abstractmethod
    def simulate(self):
        pass

class BullMarketScenario(TradingScenario):
    def simulate(self):
        return "Simulating Bull Market scenario..."

class BearMarketScenario(TradingScenario):
    def simulate(self):
        return "Simulating Bear Market scenario..."

class VolatileMarketScenario(TradingScenario):
    def simulate(self):
        return "Simulating Volatile Market scenario..."

class TradingScenarioFactory:
    @staticmethod
    def create_scenario(scenario_type: str) -> TradingScenario:
        if scenario_type == "bull":
            return BullMarketScenario()
        elif scenario_type == "bear":
            return BearMarketScenario()
        elif scenario_type == "volatile":
            return VolatileMarketScenario()
        else:
            raise ValueError(f"Unknown scenario type: {scenario_type}")

def run_simulation(scenario_type: str):
    scenario = TradingScenarioFactory.create_scenario(scenario_type)
    result = scenario.simulate()
    # --- Observer Pattern: Notify all WebSocket observers ---
    from app.core.websocket import simulation_notifier
    simulation_notifier.notify({"update": result})
    return result

"""Gas estimation utilities."""
import requests
from dataclasses import dataclass

@dataclass
class GasEstimate:
    base_fee: int
    priority_fee: int
    estimated_cost_eth: float
    estimated_cost_usd: float

class GasEstimator:
    def __init__(self, rpc_url: str, eth_price_usd: float = 3500.0):
        self.rpc_url = rpc_url
        self.eth_price = eth_price_usd
    
    def estimate(self, gas_limit: int = 21000) -> GasEstimate:
        """Estimate gas cost for a transaction."""
        # Would call eth_gasPrice and eth_maxPriorityFeePerGas
        return GasEstimate(
            base_fee=20_000_000_000,
            priority_fee=1_500_000_000,
            estimated_cost_eth=gas_limit * 21.5e-9,
            estimated_cost_usd=gas_limit * 21.5e-9 * self.eth_price
        )
    
    def suggest_priority_fee(self, urgency: str = "medium") -> int:
        """Suggest priority fee based on urgency."""
        fees = {"low": 1e9, "medium": 1.5e9, "high": 3e9}
        return int(fees.get(urgency, 1.5e9))

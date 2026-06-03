"""ENS resolution utilities."""
from web3 import Web3

class ENSResolver:
    def __init__(self, rpc_url: str):
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
    
    def resolve(self, name: str) -> str:
        """Resolve ENS name to address."""
        try:
            return self.w3.ens.address(name)
        except Exception:
            return None
    
    def reverse(self, address: str) -> str:
        """Reverse resolve address to ENS name."""
        try:
            return self.w3.ens.name(address)
        except Exception:
            return None

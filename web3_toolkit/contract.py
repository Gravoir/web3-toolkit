"""Smart contract interaction utilities."""
from web3 import Web3
from eth_abi import decode, encode

# Common ABIs
ERC20_ABI = [
    {"constant": True, "inputs": [{"name": "_owner", "type": "address"}], "name": "balanceOf", "outputs": [{"name": "balance", "type": "uint256"}], "type": "function"},
    {"constant": True, "inputs": [], "name": "decimals", "outputs": [{"name": "", "type": "uint8"}], "type": "function"},
    {"constant": True, "inputs": [], "name": "symbol", "outputs": [{"name": "", "type": "string"}], "type": "function"},
    {"constant": True, "inputs": [], "name": "totalSupply", "outputs": [{"name": "", "type": "uint256"}], "type": "function"},
]

class ContractReader:
    def __init__(self, rpc_url: str):
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
    
    def erc20_balance(self, token: str, wallet: str) -> dict:
        """Get ERC20 token balance for a wallet."""
        contract = self.w3.eth.contract(
            address=Web3.to_checksum_address(token),
            abi=ERC20_ABI
        )
        balance = contract.functions.balanceOf(Web3.to_checksum_address(wallet)).call()
        decimals = contract.functions.decimals().call()
        symbol = contract.functions.symbol().call()
        return {
            "raw": balance,
            "formatted": balance / (10 ** decimals),
            "symbol": symbol,
            "decimals": decimals
        }
    
    def eth_balance(self, wallet: str) -> float:
        """Get ETH balance."""
        balance = self.w3.eth.get_balance(Web3.to_checksum_address(wallet))
        return self.w3.from_wei(balance, 'ether')
    
    def batch_call(self, calls: list) -> list:
        """Execute multiple read calls in a single batch."""
        # Simplified multicall pattern
        results = []
        for call in calls:
            contract = self.w3.eth.contract(
                address=Web3.to_checksum_address(call['target']),
                abi=call.get('abi', ERC20_ABI)
            )
            fn = getattr(contract.functions, call['function'])
            result = fn(*call.get('args', [])).call()
            results.append(result)
        return results

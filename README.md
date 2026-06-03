# Web3 Toolkit 🔗

Collection of Web3 utilities for contract interaction, on-chain analytics, and DeFi operations.

## Modules

### Contract Interaction
- ABI encoding/decoding helpers
- Multi-call batch reader
- Event log parser & decoder

### On-chain Analytics
- Wallet profiler — token holdings, tx history, P&L
- DEX trade aggregator (Uniswap, SushiSwap)
- Gas estimator with priority fee optimization

### DeFi Helpers
- Uniswap V2/V3 price quoting
- Aave supply/borrow rate fetcher
- ENS name resolver

## Quick Start

```python
from web3_toolkit import ContractReader, WalletProfiler

# Read contract state
reader = ContractReader("https://eth.llamarpc.com")
balance = reader.erc20_balance(token="0x...", wallet="0x...")

# Profile a wallet
profiler = WalletProfiler("0x...")
summary = profiler.get_summary()
print(f"Total value: ${summary.total_value_usd:,.2f}")
```

## Setup

```bash
pip install web3 eth-abi
cp .env.example .env  # Add your RPC URL
```

## License

MIT

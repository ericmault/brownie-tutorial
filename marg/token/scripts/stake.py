from brownie import Contract, accounts
from brownie_tokens import MintableForkToken

def main():
    dai_addr = '0x6b175474e89094c44da98b954eedeac495271d0f'
    usdc_addr = '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48'
    registrary_addr = '0x90E00ACe148ca3b23Ac1bC8C240C2a7Dd9c2d7f5'
    
    amount = 100_000 * 10 ** 18
    dai = MintableForkToken(dai_addr)
    dai._mint_for_testing(accounts[0],amount)
    
    registrary = Contract(registrary_addr)
    
    pool_addr = registrary.find_pool_for_coins(dai_addr,usdc_addr)
    
    pool = Contract(pool_addr)
    
    dai.approve(pool_addr, amount,{'from':accounts[0]})
    
    pool.add_liquidity([amount,0,0],0,{'from':accounts[0]})
# brownie-tutorial


node = v16.1.0
npm = 7.11.2
Python = 3.8.6
Ganache CLI v6.12.2 (ganache-core: 2.13.2)


### commands
brownie init 
brownie console
my_token = Token.deploy("Test token","tst",18, 1e21,{'from':accounts[0]})
my_token.transfer(accounts[1],1e10,{'from':accounts[0]})
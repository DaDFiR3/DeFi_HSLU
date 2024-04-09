# Python script for Shiny app 

# load libraries
import json
from web3 import Web3
from datetime import datetime    
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import requests






# This data should come as parameters
#ETHEREUM_ADDRESS = '0x46e84ddb17aa374f623d3d843a641bb84436b4e9'
#FROM = 18848761 #18848761  # Replace this with a suitable value based on your requirements
#TO =  'latest'
#SCENARIO = "DeFI Scenario"
#PROTOCOL = "Tether"
MAX_TRANSACTIONS = 50 # max number of transactions before a hard cut is done to save costs
INFURA_PROJECT_ID = "empty"
ACTUS_SERVER = "http://localhost:8080"


PARAMS = '''
{
    "protocols": [
      {
        "name": "Tether",
        "display": "Tether UDST",
        "address": "0xdAC17F958D2ee523a2206206994597C13D831ec7",
        "event" : "transfer",
        "contract": "UMP",      
        "ABI":  [{"constant": true, "inputs": [], "name": "name", "outputs": [{"name": "", "type": "string"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": false, "inputs": [{"name": "_upgradedAddress", "type": "address"}], "name": "deprecate", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": false, "inputs": [{"name": "_spender", "type": "address"}, {"name": "_value", "type": "uint256"}], "name": "approve", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": true, "inputs": [], "name": "deprecated", "outputs": [{"name": "", "type": "bool"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": false, "inputs": [{"name": "_evilUser", "type": "address"}], "name": "addBlackList", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": true, "inputs": [], "name": "totalSupply", "outputs": [{"name": "", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": false, "inputs": [{"name": "_from", "type": "address"}, {"name": "_to", "type": "address"}, {"name": "_value", "type": "uint256"}], "name": "transferFrom", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": true, "inputs": [], "name": "upgradedAddress", "outputs": [{"name": "", "type": "address"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [{"name": "", "type": "address"}], "name": "balances", "outputs": [{"name": "", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [], "name": "decimals", "outputs": [{"name": "", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [], "name": "maximumFee", "outputs": [{"name": "", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [], "name": "_totalSupply", "outputs": [{"name": "", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": false, "inputs": [], "name": "unpause", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": true, "inputs": [{"name": "_maker", "type": "address"}], "name": "getBlackListStatus", "outputs": [{"name": "", "type": "bool"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [{"name": "", "type": "address"}, {"name": "", "type": "address"}], "name": "allowed", "outputs": [{"name": "", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [], "name": "paused", "outputs": [{"name": "", "type": "bool"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [{"name": "who", "type": "address"}], "name": "balanceOf", "outputs": [{"name": "", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": false, "inputs": [], "name": "pause", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": true, "inputs": [], "name": "getOwner", "outputs": [{"name": "", "type": "address"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [], "name": "owner", "outputs": [{"name": "", "type": "address"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [], "name": "symbol", "outputs": [{"name": "", "type": "string"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": false, "inputs": [{"name": "_to", "type": "address"}, {"name": "_value", "type": "uint256"}], "name": "transfer", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": false, "inputs": [{"name": "newBasisPoints", "type": "uint256"}, {"name": "newMaxFee", "type": "uint256"}], "name": "setParams", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": false, "inputs": [{"name": "amount", "type": "uint256"}], "name": "issue", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": false, "inputs": [{"name": "amount", "type": "uint256"}], "name": "redeem", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": true, "inputs": [{"name": "_owner", "type": "address"}, {"name": "_spender", "type": "address"}], "name": "allowance", "outputs": [{"name": "remaining", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [], "name": "basisPointsRate", "outputs": [{"name": "", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [{"name": "", "type": "address"}], "name": "isBlackListed", "outputs": [{"name": "", "type": "bool"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": false, "inputs": [{"name": "_clearedUser", "type": "address"}], "name": "removeBlackList", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": true, "inputs": [], "name": "MAX_UINT", "outputs": [{"name": "", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": false, "inputs": [{"name": "newOwner", "type": "address"}], "name": "transferOwnership", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": false, "inputs": [{"name": "_blackListedUser", "type": "address"}], "name": "destroyBlackFunds", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"name": "_initialSupply", "type": "uint256"}, {"name": "_name", "type": "string"}, {"name": "_symbol", "type": "string"}, {"name": "_decimals", "type": "uint256"}], "payable": false, "stateMutability": "nonpayable", "type": "constructor"}, {"anonymous": false, "inputs": [{"indexed": false, "name": "amount", "type": "uint256"}], "name": "Issue", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": false, "name": "amount", "type": "uint256"}], "name": "Redeem", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": false, "name": "newAddress", "type": "address"}], "name": "Deprecate", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": false, "name": "feeBasisPoints", "type": "uint256"}, {"indexed": false, "name": "maxFee", "type": "uint256"}], "name": "Params", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": false, "name": "_blackListedUser", "type": "address"}, {"indexed": false, "name": "_balance", "type": "uint256"}], "name": "DestroyedBlackFunds", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": false, "name": "_user", "type": "address"}], "name": "AddedBlackList", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": false, "name": "_user", "type": "address"}], "name": "RemovedBlackList", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": true, "name": "owner", "type": "address"}, {"indexed": true, "name": "spender", "type": "address"}, {"indexed": false, "name": "value", "type": "uint256"}], "name": "Approval", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": true, "name": "from", "type": "address"}, {"indexed": true, "name": "to", "type": "address"}, {"indexed": false, "name": "value", "type": "uint256"}], "name": "Transfer", "type": "event"}, {"anonymous": false, "inputs": [], "name": "Pause", "type": "event"}, {"anonymous": false, "inputs": [], "name": "Unpause", "type": "event"}]     
      },
      {
        "name": "UniswapLiq",
        "display": "UniswapV2 ETH-USDT Liquidity",
        "address": "0x0d4a11d5EEaaC28EC3F61d100daF4d40471f1852",
        "event" : "transfer",
        "contract": "STK",  
        "ABI": [{"inputs": [], "payable": false, "stateMutability": "nonpayable", "type": "constructor"}, {"anonymous": false, "inputs": [{"indexed": true, "internalType": "address", "name": "owner", "type": "address"}, {"indexed": true, "internalType": "address", "name": "spender", "type": "address"}, {"indexed": false, "internalType": "uint256", "name": "value", "type": "uint256"}], "name": "Approval", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": true, "internalType": "address", "name": "sender", "type": "address"}, {"indexed": false, "internalType": "uint256", "name": "amount0", "type": "uint256"}, {"indexed": false, "internalType": "uint256", "name": "amount1", "type": "uint256"}, {"indexed": true, "internalType": "address", "name": "to", "type": "address"}], "name": "Burn", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": true, "internalType": "address", "name": "sender", "type": "address"}, {"indexed": false, "internalType": "uint256", "name": "amount0", "type": "uint256"}, {"indexed": false, "internalType": "uint256", "name": "amount1", "type": "uint256"}], "name": "Mint", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": true, "internalType": "address", "name": "sender", "type": "address"}, {"indexed": false, "internalType": "uint256", "name": "amount0In", "type": "uint256"}, {"indexed": false, "internalType": "uint256", "name": "amount1In", "type": "uint256"}, {"indexed": false, "internalType": "uint256", "name": "amount0Out", "type": "uint256"}, {"indexed": false, "internalType": "uint256", "name": "amount1Out", "type": "uint256"}, {"indexed": true, "internalType": "address", "name": "to", "type": "address"}], "name": "Swap", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": false, "internalType": "uint112", "name": "reserve0", "type": "uint112"}, {"indexed": false, "internalType": "uint112", "name": "reserve1", "type": "uint112"}], "name": "Sync", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": true, "internalType": "address", "name": "from", "type": "address"}, {"indexed": true, "internalType": "address", "name": "to", "type": "address"}, {"indexed": false, "internalType": "uint256", "name": "value", "type": "uint256"}], "name": "Transfer", "type": "event"}, {"constant": true, "inputs": [], "name": "DOMAIN_SEPARATOR", "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [], "name": "MINIMUM_LIQUIDITY", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [], "name": "PERMIT_TYPEHASH", "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [{"internalType": "address", "name": "", "type": "address"}, {"internalType": "address", "name": "", "type": "address"}], "name": "allowance", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": false, "inputs": [{"internalType": "address", "name": "spender", "type": "address"}, {"internalType": "uint256", "name": "value", "type": "uint256"}], "name": "approve", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": true, "inputs": [{"internalType": "address", "name": "", "type": "address"}], "name": "balanceOf", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": false, "inputs": [{"internalType": "address", "name": "to", "type": "address"}], "name": "burn", "outputs": [{"internalType": "uint256", "name": "amount0", "type": "uint256"}, {"internalType": "uint256", "name": "amount1", "type": "uint256"}], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": true, "inputs": [], "name": "decimals", "outputs": [{"internalType": "uint8", "name": "", "type": "uint8"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [], "name": "factory", "outputs": [{"internalType": "address", "name": "", "type": "address"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [], "name": "getReserves", "outputs": [{"internalType": "uint112", "name": "_reserve0", "type": "uint112"}, {"internalType": "uint112", "name": "_reserve1", "type": "uint112"}, {"internalType": "uint32", "name": "_blockTimestampLast", "type": "uint32"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": false, "inputs": [{"internalType": "address", "name": "_token0", "type": "address"}, {"internalType": "address", "name": "_token1", "type": "address"}], "name": "initialize", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": true, "inputs": [], "name": "kLast", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": false, "inputs": [{"internalType": "address", "name": "to", "type": "address"}], "name": "mint", "outputs": [{"internalType": "uint256", "name": "liquidity", "type": "uint256"}], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": true, "inputs": [], "name": "name", "outputs": [{"internalType": "string", "name": "", "type": "string"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [{"internalType": "address", "name": "", "type": "address"}], "name": "nonces", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": false, "inputs": [{"internalType": "address", "name": "owner", "type": "address"}, {"internalType": "address", "name": "spender", "type": "address"}, {"internalType": "uint256", "name": "value", "type": "uint256"}, {"internalType": "uint256", "name": "deadline", "type": "uint256"}, {"internalType": "uint8", "name": "v", "type": "uint8"}, {"internalType": "bytes32", "name": "r", "type": "bytes32"}, {"internalType": "bytes32", "name": "s", "type": "bytes32"}], "name": "permit", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": true, "inputs": [], "name": "price0CumulativeLast", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [], "name": "price1CumulativeLast", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": false, "inputs": [{"internalType": "address", "name": "to", "type": "address"}], "name": "skim", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": false, "inputs": [{"internalType": "uint256", "name": "amount0Out", "type": "uint256"}, {"internalType": "uint256", "name": "amount1Out", "type": "uint256"}, {"internalType": "address", "name": "to", "type": "address"}, {"internalType": "bytes", "name": "data", "type": "bytes"}], "name": "swap", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": true, "inputs": [], "name": "symbol", "outputs": [{"internalType": "string", "name": "", "type": "string"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": false, "inputs": [], "name": "sync", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": true, "inputs": [], "name": "token0", "outputs": [{"internalType": "address", "name": "", "type": "address"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [], "name": "token1", "outputs": [{"internalType": "address", "name": "", "type": "address"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [], "name": "totalSupply", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": false, "inputs": [{"internalType": "address", "name": "to", "type": "address"}, {"internalType": "uint256", "name": "value", "type": "uint256"}], "name": "transfer", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": false, "inputs": [{"internalType": "address", "name": "from", "type": "address"}, {"internalType": "address", "name": "to", "type": "address"}, {"internalType": "uint256", "name": "value", "type": "uint256"}], "name": "transferFrom", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "payable": false, "stateMutability": "nonpayable", "type": "function"}]  
      },
      {
        "name": "UniswapV2Exchange",
        "display": "UniswapV2 ETH-USDT Exchange",
        "address": "0x0d4a11d5EEaaC28EC3F61d100daF4d40471f1852",
        "event" : "swap",
        "contract": "FXOUT", 
        "ABI": [{"inputs": [], "payable": false, "stateMutability": "nonpayable", "type": "constructor"}, {"anonymous": false, "inputs": [{"indexed": true, "internalType": "address", "name": "owner", "type": "address"}, {"indexed": true, "internalType": "address", "name": "spender", "type": "address"}, {"indexed": false, "internalType": "uint256", "name": "value", "type": "uint256"}], "name": "Approval", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": true, "internalType": "address", "name": "sender", "type": "address"}, {"indexed": false, "internalType": "uint256", "name": "amount0", "type": "uint256"}, {"indexed": false, "internalType": "uint256", "name": "amount1", "type": "uint256"}, {"indexed": true, "internalType": "address", "name": "to", "type": "address"}], "name": "Burn", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": true, "internalType": "address", "name": "sender", "type": "address"}, {"indexed": false, "internalType": "uint256", "name": "amount0", "type": "uint256"}, {"indexed": false, "internalType": "uint256", "name": "amount1", "type": "uint256"}], "name": "Mint", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": true, "internalType": "address", "name": "sender", "type": "address"}, {"indexed": false, "internalType": "uint256", "name": "amount0In", "type": "uint256"}, {"indexed": false, "internalType": "uint256", "name": "amount1In", "type": "uint256"}, {"indexed": false, "internalType": "uint256", "name": "amount0Out", "type": "uint256"}, {"indexed": false, "internalType": "uint256", "name": "amount1Out", "type": "uint256"}, {"indexed": true, "internalType": "address", "name": "to", "type": "address"}], "name": "Swap", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": false, "internalType": "uint112", "name": "reserve0", "type": "uint112"}, {"indexed": false, "internalType": "uint112", "name": "reserve1", "type": "uint112"}], "name": "Sync", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": true, "internalType": "address", "name": "from", "type": "address"}, {"indexed": true, "internalType": "address", "name": "to", "type": "address"}, {"indexed": false, "internalType": "uint256", "name": "value", "type": "uint256"}], "name": "Transfer", "type": "event"}, {"constant": true, "inputs": [], "name": "DOMAIN_SEPARATOR", "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [], "name": "MINIMUM_LIQUIDITY", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [], "name": "PERMIT_TYPEHASH", "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [{"internalType": "address", "name": "", "type": "address"}, {"internalType": "address", "name": "", "type": "address"}], "name": "allowance", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": false, "inputs": [{"internalType": "address", "name": "spender", "type": "address"}, {"internalType": "uint256", "name": "value", "type": "uint256"}], "name": "approve", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": true, "inputs": [{"internalType": "address", "name": "", "type": "address"}], "name": "balanceOf", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": false, "inputs": [{"internalType": "address", "name": "to", "type": "address"}], "name": "burn", "outputs": [{"internalType": "uint256", "name": "amount0", "type": "uint256"}, {"internalType": "uint256", "name": "amount1", "type": "uint256"}], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": true, "inputs": [], "name": "decimals", "outputs": [{"internalType": "uint8", "name": "", "type": "uint8"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [], "name": "factory", "outputs": [{"internalType": "address", "name": "", "type": "address"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [], "name": "getReserves", "outputs": [{"internalType": "uint112", "name": "_reserve0", "type": "uint112"}, {"internalType": "uint112", "name": "_reserve1", "type": "uint112"}, {"internalType": "uint32", "name": "_blockTimestampLast", "type": "uint32"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": false, "inputs": [{"internalType": "address", "name": "_token0", "type": "address"}, {"internalType": "address", "name": "_token1", "type": "address"}], "name": "initialize", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": true, "inputs": [], "name": "kLast", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": false, "inputs": [{"internalType": "address", "name": "to", "type": "address"}], "name": "mint", "outputs": [{"internalType": "uint256", "name": "liquidity", "type": "uint256"}], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": true, "inputs": [], "name": "name", "outputs": [{"internalType": "string", "name": "", "type": "string"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [{"internalType": "address", "name": "", "type": "address"}], "name": "nonces", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": false, "inputs": [{"internalType": "address", "name": "owner", "type": "address"}, {"internalType": "address", "name": "spender", "type": "address"}, {"internalType": "uint256", "name": "value", "type": "uint256"}, {"internalType": "uint256", "name": "deadline", "type": "uint256"}, {"internalType": "uint8", "name": "v", "type": "uint8"}, {"internalType": "bytes32", "name": "r", "type": "bytes32"}, {"internalType": "bytes32", "name": "s", "type": "bytes32"}], "name": "permit", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": true, "inputs": [], "name": "price0CumulativeLast", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [], "name": "price1CumulativeLast", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": false, "inputs": [{"internalType": "address", "name": "to", "type": "address"}], "name": "skim", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": false, "inputs": [{"internalType": "uint256", "name": "amount0Out", "type": "uint256"}, {"internalType": "uint256", "name": "amount1Out", "type": "uint256"}, {"internalType": "address", "name": "to", "type": "address"}, {"internalType": "bytes", "name": "data", "type": "bytes"}], "name": "swap", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": true, "inputs": [], "name": "symbol", "outputs": [{"internalType": "string", "name": "", "type": "string"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": false, "inputs": [], "name": "sync", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": true, "inputs": [], "name": "token0", "outputs": [{"internalType": "address", "name": "", "type": "address"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [], "name": "token1", "outputs": [{"internalType": "address", "name": "", "type": "address"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [], "name": "totalSupply", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": false, "inputs": [{"internalType": "address", "name": "to", "type": "address"}, {"internalType": "uint256", "name": "value", "type": "uint256"}], "name": "transfer", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": false, "inputs": [{"internalType": "address", "name": "from", "type": "address"}, {"internalType": "address", "name": "to", "type": "address"}, {"internalType": "uint256", "name": "value", "type": "uint256"}], "name": "transferFrom", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "payable": false, "stateMutability": "nonpayable", "type": "function"}]  
      },
      {
        "name": "AaveV3Liquidity", 
        "display": "AAVE V3 USDT Liquidity",
        "address": "0x23878914EFE38d27C4D67Ab83ed1b93A74D4086a",
        "event" : "transfer",
        "contract": "STK",  
        "ABI": [{"inputs": [{"internalType": "contract IPool", "name": "pool", "type": "address"}], "stateMutability": "nonpayable", "type": "constructor"}, {"anonymous": false, "inputs": [{"indexed": true, "internalType": "address", "name": "owner", "type": "address"}, {"indexed": true, "internalType": "address", "name": "spender", "type": "address"}, {"indexed": false, "internalType": "uint256", "name": "value", "type": "uint256"}], "name": "Approval", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": true, "internalType": "address", "name": "from", "type": "address"}, {"indexed": true, "internalType": "address", "name": "to", "type": "address"}, {"indexed": false, "internalType": "uint256", "name": "value", "type": "uint256"}, {"indexed": false, "internalType": "uint256", "name": "index", "type": "uint256"}], "name": "BalanceTransfer", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": true, "internalType": "address", "name": "from", "type": "address"}, {"indexed": true, "internalType": "address", "name": "target", "type": "address"}, {"indexed": false, "internalType": "uint256", "name": "value", "type": "uint256"}, {"indexed": false, "internalType": "uint256", "name": "balanceIncrease", "type": "uint256"}, {"indexed": false, "internalType": "uint256", "name": "index", "type": "uint256"}], "name": "Burn", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": true, "internalType": "address", "name": "underlyingAsset", "type": "address"}, {"indexed": true, "internalType": "address", "name": "pool", "type": "address"}, {"indexed": false, "internalType": "address", "name": "treasury", "type": "address"}, {"indexed": false, "internalType": "address", "name": "incentivesController", "type": "address"}, {"indexed": false, "internalType": "uint8", "name": "aTokenDecimals", "type": "uint8"}, {"indexed": false, "internalType": "string", "name": "aTokenName", "type": "string"}, {"indexed": false, "internalType": "string", "name": "aTokenSymbol", "type": "string"}, {"indexed": false, "internalType": "bytes", "name": "params", "type": "bytes"}], "name": "Initialized", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": true, "internalType": "address", "name": "caller", "type": "address"}, {"indexed": true, "internalType": "address", "name": "onBehalfOf", "type": "address"}, {"indexed": false, "internalType": "uint256", "name": "value", "type": "uint256"}, {"indexed": false, "internalType": "uint256", "name": "balanceIncrease", "type": "uint256"}, {"indexed": false, "internalType": "uint256", "name": "index", "type": "uint256"}], "name": "Mint", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": true, "internalType": "address", "name": "from", "type": "address"}, {"indexed": true, "internalType": "address", "name": "to", "type": "address"}, {"indexed": false, "internalType": "uint256", "name": "value", "type": "uint256"}], "name": "Transfer", "type": "event"}, {"inputs": [], "name": "ATOKEN_REVISION", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "DOMAIN_SEPARATOR", "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "EIP712_REVISION", "outputs": [{"internalType": "bytes", "name": "", "type": "bytes"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "PERMIT_TYPEHASH", "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "POOL", "outputs": [{"internalType": "contract IPool", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "RESERVE_TREASURY_ADDRESS", "outputs": [{"internalType": "address", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "UNDERLYING_ASSET_ADDRESS", "outputs": [{"internalType": "address", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "owner", "type": "address"}, {"internalType": "address", "name": "spender", "type": "address"}], "name": "allowance", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "spender", "type": "address"}, {"internalType": "uint256", "name": "amount", "type": "uint256"}], "name": "approve", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "address", "name": "user", "type": "address"}], "name": "balanceOf", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "from", "type": "address"}, {"internalType": "address", "name": "receiverOfUnderlying", "type": "address"}, {"internalType": "uint256", "name": "amount", "type": "uint256"}, {"internalType": "uint256", "name": "index", "type": "uint256"}], "name": "burn", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [], "name": "decimals", "outputs": [{"internalType": "uint8", "name": "", "type": "uint8"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "spender", "type": "address"}, {"internalType": "uint256", "name": "subtractedValue", "type": "uint256"}], "name": "decreaseAllowance", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [], "name": "getIncentivesController", "outputs": [{"internalType": "contract IAaveIncentivesController", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "user", "type": "address"}], "name": "getPreviousIndex", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "user", "type": "address"}], "name": "getScaledUserBalanceAndSupply", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}, {"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "user", "type": "address"}, {"internalType": "address", "name": "onBehalfOf", "type": "address"}, {"internalType": "uint256", "name": "amount", "type": "uint256"}], "name": "handleRepayment", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "address", "name": "spender", "type": "address"}, {"internalType": "uint256", "name": "addedValue", "type": "uint256"}], "name": "increaseAllowance", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "contract IPool", "name": "initializingPool", "type": "address"}, {"internalType": "address", "name": "treasury", "type": "address"}, {"internalType": "address", "name": "underlyingAsset", "type": "address"}, {"internalType": "contract IAaveIncentivesController", "name": "incentivesController", "type": "address"}, {"internalType": "uint8", "name": "aTokenDecimals", "type": "uint8"}, {"internalType": "string", "name": "aTokenName", "type": "string"}, {"internalType": "string", "name": "aTokenSymbol", "type": "string"}, {"internalType": "bytes", "name": "params", "type": "bytes"}], "name": "initialize", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "address", "name": "caller", "type": "address"}, {"internalType": "address", "name": "onBehalfOf", "type": "address"}, {"internalType": "uint256", "name": "amount", "type": "uint256"}, {"internalType": "uint256", "name": "index", "type": "uint256"}], "name": "mint", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "amount", "type": "uint256"}, {"internalType": "uint256", "name": "index", "type": "uint256"}], "name": "mintToTreasury", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [], "name": "name", "outputs": [{"internalType": "string", "name": "", "type": "string"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "owner", "type": "address"}], "name": "nonces", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "owner", "type": "address"}, {"internalType": "address", "name": "spender", "type": "address"}, {"internalType": "uint256", "name": "value", "type": "uint256"}, {"internalType": "uint256", "name": "deadline", "type": "uint256"}, {"internalType": "uint8", "name": "v", "type": "uint8"}, {"internalType": "bytes32", "name": "r", "type": "bytes32"}, {"internalType": "bytes32", "name": "s", "type": "bytes32"}], "name": "permit", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "address", "name": "token", "type": "address"}, {"internalType": "address", "name": "to", "type": "address"}, {"internalType": "uint256", "name": "amount", "type": "uint256"}], "name": "rescueTokens", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "address", "name": "user", "type": "address"}], "name": "scaledBalanceOf", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "scaledTotalSupply", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "contract IAaveIncentivesController", "name": "controller", "type": "address"}], "name": "setIncentivesController", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [], "name": "symbol", "outputs": [{"internalType": "string", "name": "", "type": "string"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "totalSupply", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "recipient", "type": "address"}, {"internalType": "uint256", "name": "amount", "type": "uint256"}], "name": "transfer", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "address", "name": "sender", "type": "address"}, {"internalType": "address", "name": "recipient", "type": "address"}, {"internalType": "uint256", "name": "amount", "type": "uint256"}], "name": "transferFrom", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "address", "name": "from", "type": "address"}, {"internalType": "address", "name": "to", "type": "address"}, {"internalType": "uint256", "name": "value", "type": "uint256"}], "name": "transferOnLiquidation", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "address", "name": "target", "type": "address"}, {"internalType": "uint256", "name": "amount", "type": "uint256"}], "name": "transferUnderlyingTo", "outputs": [], "stateMutability": "nonpayable", "type": "function"}]
      },
      {
        "name": "AaveV3Lending", 
        "display": "AAVE V3 USDT Lending",
        "address": "0x23878914EFE38d27C4D67Ab83ed1b93A74D4086a",
        "event" : "swap",
        "contract": "PAM",  
        "ABI": [{"inputs": [{"internalType": "contract IPool", "name": "pool", "type": "address"}], "stateMutability": "nonpayable", "type": "constructor"}, {"anonymous": false, "inputs": [{"indexed": true, "internalType": "address", "name": "owner", "type": "address"}, {"indexed": true, "internalType": "address", "name": "spender", "type": "address"}, {"indexed": false, "internalType": "uint256", "name": "value", "type": "uint256"}], "name": "Approval", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": true, "internalType": "address", "name": "from", "type": "address"}, {"indexed": true, "internalType": "address", "name": "to", "type": "address"}, {"indexed": false, "internalType": "uint256", "name": "value", "type": "uint256"}, {"indexed": false, "internalType": "uint256", "name": "index", "type": "uint256"}], "name": "BalanceTransfer", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": true, "internalType": "address", "name": "from", "type": "address"}, {"indexed": true, "internalType": "address", "name": "target", "type": "address"}, {"indexed": false, "internalType": "uint256", "name": "value", "type": "uint256"}, {"indexed": false, "internalType": "uint256", "name": "balanceIncrease", "type": "uint256"}, {"indexed": false, "internalType": "uint256", "name": "index", "type": "uint256"}], "name": "Burn", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": true, "internalType": "address", "name": "underlyingAsset", "type": "address"}, {"indexed": true, "internalType": "address", "name": "pool", "type": "address"}, {"indexed": false, "internalType": "address", "name": "treasury", "type": "address"}, {"indexed": false, "internalType": "address", "name": "incentivesController", "type": "address"}, {"indexed": false, "internalType": "uint8", "name": "aTokenDecimals", "type": "uint8"}, {"indexed": false, "internalType": "string", "name": "aTokenName", "type": "string"}, {"indexed": false, "internalType": "string", "name": "aTokenSymbol", "type": "string"}, {"indexed": false, "internalType": "bytes", "name": "params", "type": "bytes"}], "name": "Initialized", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": true, "internalType": "address", "name": "caller", "type": "address"}, {"indexed": true, "internalType": "address", "name": "onBehalfOf", "type": "address"}, {"indexed": false, "internalType": "uint256", "name": "value", "type": "uint256"}, {"indexed": false, "internalType": "uint256", "name": "balanceIncrease", "type": "uint256"}, {"indexed": false, "internalType": "uint256", "name": "index", "type": "uint256"}], "name": "Mint", "type": "event"}, {"anonymous": false, "inputs": [{"indexed": true, "internalType": "address", "name": "from", "type": "address"}, {"indexed": true, "internalType": "address", "name": "to", "type": "address"}, {"indexed": false, "internalType": "uint256", "name": "value", "type": "uint256"}], "name": "Transfer", "type": "event"}, {"inputs": [], "name": "ATOKEN_REVISION", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "DOMAIN_SEPARATOR", "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "EIP712_REVISION", "outputs": [{"internalType": "bytes", "name": "", "type": "bytes"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "PERMIT_TYPEHASH", "outputs": [{"internalType": "bytes32", "name": "", "type": "bytes32"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "POOL", "outputs": [{"internalType": "contract IPool", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "RESERVE_TREASURY_ADDRESS", "outputs": [{"internalType": "address", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "UNDERLYING_ASSET_ADDRESS", "outputs": [{"internalType": "address", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "owner", "type": "address"}, {"internalType": "address", "name": "spender", "type": "address"}], "name": "allowance", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "spender", "type": "address"}, {"internalType": "uint256", "name": "amount", "type": "uint256"}], "name": "approve", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "address", "name": "user", "type": "address"}], "name": "balanceOf", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "from", "type": "address"}, {"internalType": "address", "name": "receiverOfUnderlying", "type": "address"}, {"internalType": "uint256", "name": "amount", "type": "uint256"}, {"internalType": "uint256", "name": "index", "type": "uint256"}], "name": "burn", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [], "name": "decimals", "outputs": [{"internalType": "uint8", "name": "", "type": "uint8"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "spender", "type": "address"}, {"internalType": "uint256", "name": "subtractedValue", "type": "uint256"}], "name": "decreaseAllowance", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [], "name": "getIncentivesController", "outputs": [{"internalType": "contract IAaveIncentivesController", "name": "", "type": "address"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "user", "type": "address"}], "name": "getPreviousIndex", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "user", "type": "address"}], "name": "getScaledUserBalanceAndSupply", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}, {"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "user", "type": "address"}, {"internalType": "address", "name": "onBehalfOf", "type": "address"}, {"internalType": "uint256", "name": "amount", "type": "uint256"}], "name": "handleRepayment", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "address", "name": "spender", "type": "address"}, {"internalType": "uint256", "name": "addedValue", "type": "uint256"}], "name": "increaseAllowance", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "contract IPool", "name": "initializingPool", "type": "address"}, {"internalType": "address", "name": "treasury", "type": "address"}, {"internalType": "address", "name": "underlyingAsset", "type": "address"}, {"internalType": "contract IAaveIncentivesController", "name": "incentivesController", "type": "address"}, {"internalType": "uint8", "name": "aTokenDecimals", "type": "uint8"}, {"internalType": "string", "name": "aTokenName", "type": "string"}, {"internalType": "string", "name": "aTokenSymbol", "type": "string"}, {"internalType": "bytes", "name": "params", "type": "bytes"}], "name": "initialize", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "address", "name": "caller", "type": "address"}, {"internalType": "address", "name": "onBehalfOf", "type": "address"}, {"internalType": "uint256", "name": "amount", "type": "uint256"}, {"internalType": "uint256", "name": "index", "type": "uint256"}], "name": "mint", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "uint256", "name": "amount", "type": "uint256"}, {"internalType": "uint256", "name": "index", "type": "uint256"}], "name": "mintToTreasury", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [], "name": "name", "outputs": [{"internalType": "string", "name": "", "type": "string"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "owner", "type": "address"}], "name": "nonces", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "owner", "type": "address"}, {"internalType": "address", "name": "spender", "type": "address"}, {"internalType": "uint256", "name": "value", "type": "uint256"}, {"internalType": "uint256", "name": "deadline", "type": "uint256"}, {"internalType": "uint8", "name": "v", "type": "uint8"}, {"internalType": "bytes32", "name": "r", "type": "bytes32"}, {"internalType": "bytes32", "name": "s", "type": "bytes32"}], "name": "permit", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "address", "name": "token", "type": "address"}, {"internalType": "address", "name": "to", "type": "address"}, {"internalType": "uint256", "name": "amount", "type": "uint256"}], "name": "rescueTokens", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "address", "name": "user", "type": "address"}], "name": "scaledBalanceOf", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "scaledTotalSupply", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "contract IAaveIncentivesController", "name": "controller", "type": "address"}], "name": "setIncentivesController", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [], "name": "symbol", "outputs": [{"internalType": "string", "name": "", "type": "string"}], "stateMutability": "view", "type": "function"}, {"inputs": [], "name": "totalSupply", "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "stateMutability": "view", "type": "function"}, {"inputs": [{"internalType": "address", "name": "recipient", "type": "address"}, {"internalType": "uint256", "name": "amount", "type": "uint256"}], "name": "transfer", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "address", "name": "sender", "type": "address"}, {"internalType": "address", "name": "recipient", "type": "address"}, {"internalType": "uint256", "name": "amount", "type": "uint256"}], "name": "transferFrom", "outputs": [{"internalType": "bool", "name": "", "type": "bool"}], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "address", "name": "from", "type": "address"}, {"internalType": "address", "name": "to", "type": "address"}, {"internalType": "uint256", "name": "value", "type": "uint256"}], "name": "transferOnLiquidation", "outputs": [], "stateMutability": "nonpayable", "type": "function"}, {"inputs": [{"internalType": "address", "name": "target", "type": "address"}, {"internalType": "uint256", "name": "amount", "type": "uint256"}], "name": "transferUnderlyingTo", "outputs": [], "stateMutability": "nonpayable", "type": "function"}]
      }
    ]
  }
  
'''










def set_infura(infura_id, max_transactions, actus_server):
    """ 
    Sets the global variables for the infura id and the max transactions before hard cut 
    """
    global INFURA_PROJECT_ID 
    global MAX_TRANSACTIONS
    global ACTUS_SERVER
    INFURA_PROJECT_ID = infura_id
    MAX_TRANSACTIONS = int(max_transactions)
    ACTUS_SERVER = actus_server

def load_latest():
    """
    Load the latest block number in the Ethereum blockchain. Needed for the GUI
    """
    # infura id needed
    if INFURA_PROJECT_ID == "empty":
        print("NO INFURA DEFINED")
        return 19010000
    
    # set the connection to infura
    w3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{INFURA_PROJECT_ID}'))
    
    # Check if the connection is successful
    if w3.is_connected():
        # Get the latest block
        return w3.eth.block_number
    else:
        # if error return a high number
        print("NOT CONNECTED")
        return 19020000

def get_time(block_number):
    """
    Retrieves the time when a block with block_number has been created
    """
    # infura id needed
    if INFURA_PROJECT_ID == "empty":
        print("NO INFURA DEFINED")
        return "1970-01-01T00:00:00"
    
    # set the connection to infura
    w3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{INFURA_PROJECT_ID}'))

    # Check if the connection is successful
    if w3.is_connected():
        # Get the block details
        block = w3.eth.get_block(block_number)

        # Extract the timestamp and convert it to a human-readable format
        timestamp = block['timestamp']
        from datetime import datetime
        block_time = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%dT%H:%M:%S')
        return block_time
    else:
        # if error return a 1970
        return "1970-01-01T00:00:00"

def get_transactions(address, fromblock, toblock):
    """
    Reads the number of transactions between fromblock and toblock of address from Ethereum blockchain
    """

    # infura id needed
    if INFURA_PROJECT_ID == "empty":
        return 0
    
    # set the connection to infura
    w3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{INFURA_PROJECT_ID}'))

    # Check if the connection is successful
    if w3.is_connected():
        return w3.eth.get_transaction_count(address, fromblock, toblock)
    else :
        return 0

def load_transactions(address, fromblock, toblock, protocol_name):
    """
    Load all transactions between fromblock and toblock of address from Ethereum blockchain (ERC-20 contract)
    """
    counter = 0

    # Path to your JSON file where the parameters are stored
    #file_path = '/Users/fbweinga/Documents/20_Eigene_Forschung/14_DaDFiR3/Source/FEMSDadfir3/python/app/param.json'
    
    # Opening JSON file and loading the data
    #with open(file_path, 'r') as file:
        #param = json.load(file)
    
    param = json.loads(PARAMS)

    token_contract_address = ""
    abi = ""
    contract_name = ""
    found = False
    # Search for the protocol data in the list of protocols (json)
    for protocol in param['protocols']:
        # if found => read data
        if protocol['name'] == protocol_name:
            print(f"Found protocol: {protocol_name}")
            abi = protocol['ABI']
            token_contract_address = protocol['address']
            contract_name = protocol['contract']
            found = True
            break
    
    if not found:  # This else corresponds to the for loop
        print(f"No protocol found with the name {protocol_name}")
        return 1,2,3,4
         
    # Connect to Infura Ethereum node
    if INFURA_PROJECT_ID == "empty":
        print("NO INFURA DEFINED")
        return 1,2,3,4
    w3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{INFURA_PROJECT_ID}'))
    
    # Create contract object
    contract = w3.eth.contract(address=Web3.to_checksum_address(token_contract_address), abi=abi)
    
    # Get basic values of contract
    # decimals used
    decimals = contract.functions.decimals().call()
    print(f"Decimals: {decimals}")
    
    # Total token supply and symbol of the token
    total_supply = contract.functions.totalSupply().call() / (10**decimals)
    symbol = contract.functions.symbol().call()
    print(f"Total Supply: {total_supply:,} {symbol}")
    
    # Get the actual balance
    actual_balance = contract.functions.balanceOf(Web3.to_checksum_address(address)).call()
    # actual balance in full (devided by decimals)
    actual_balance_full = actual_balance/(10**decimals)
    print(f"Actual balance of {address}: {actual_balance_full:,} {symbol}")
    
    # init for later calculation
    initial_balance = contract.functions.balanceOf(Web3.to_checksum_address(address)).call(block_identifier=fromblock)
    last_balance = contract.functions.balanceOf(Web3.to_checksum_address(address)).call(block_identifier=toblock)
    deposit_data = []
    
    # Get past Transfer events for withdrawals (transaction send from the address to someone else => payout)
    withdrawal_event = contract.events.Transfer.create_filter(address=token_contract_address, fromBlock=fromblock, toBlock=toblock, argument_filters={'from': Web3.to_checksum_address(address)})
    withdrawal_events = withdrawal_event.get_all_entries()
    
    # Get past Transfer events for deposits (transaction send to the address from someone else => payin)
    deposit_event = contract.events.Transfer.create_filter(address=token_contract_address,fromBlock=fromblock, toBlock=toblock, argument_filters={'to': Web3.to_checksum_address(address)})
    deposit_events = deposit_event.get_all_entries()
    
    # get all deposit events and add them to deposit_data with positive amount
    # also update initial_balance (calculate backwards)
    print(f"Deposits for {address}:")
    for event in deposit_events:
        counter = counter +1
        # break if maximum transaction is reached to save money
        if counter > MAX_TRANSACTIONS:
            print("TOO MANY TRANSACTIONS")
            break
        timestamp = w3.eth.get_block(event['blockNumber'])['timestamp']
        deposit_date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%dT%H:%M:%S')
        amount = event['args']['value']
        deposit_data.append((deposit_date, amount))
        #print(f"Time:  {deposit_date} , Amount:  {amount/(10**decimals):,} {symbol}" )
    
    # get all withdrawl events and add them to deposit_data with negative amount
    # also update initial_balance (calculate backwards)
    print(f"Withdrawals for {address}:")
    for event in withdrawal_events:
        counter = counter +1
        # break if maximum transaction is reached to save money
        if counter > MAX_TRANSACTIONS:
            print("TOO MANY TRANSACTIONS")
            break
        timestamp = w3.eth.get_block(event['blockNumber'])['timestamp']
        withdrawal_date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%dT%H:%M:%S')
        amount = event['args']['value']
        deposit_data.append((withdrawal_date, -amount))
        #print(f"Time:  {withdrawal_date} , Amount:  {amount/(10**decimals):,} {symbol} " )
    
    if counter > MAX_TRANSACTIONS:
        return 0, 0, [], "TOO MANY TRANSACTIONS", 1, 0, "TOO MANY TRANSACTIONS"

    # Sort deposit_data by date
    deposit_data.sort(key=lambda x: x[0])
    
    initial_balance_full = initial_balance/(10**decimals)
    last_balance_full = last_balance/(10**decimals)
    # initial and acutal balance in  this currency 
    print("")
    print(f"Balance for {address}:")
    print(f"Initial balance: {initial_balance_full:,} {symbol}")
    print(f"Actual balance (last block): {last_balance_full:,} {symbol}")
    return initial_balance_full, last_balance_full, deposit_data, symbol, decimals, total_supply, contract_name

        
def call_actus(address, initial_balance_full, actual_balance_full, deposit_data, symbol, decimals, actus_contract):
    """
    Transform the data into an ACTUS json and call the ACTUS server.
    Returns the ACTUS response as Dataframe (events)
    """
    print(deposit_data)
    # transform the deposit_data into strints for the json
    deposit_times = ', '.join(f'"{date}"' for date, amount in deposit_data)
    deposit_amounts = ', '.join(str(amount/(10**decimals)) for date, amount in deposit_data)
    
    # set the actual time form some ACTUS values
    now = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    # set the scenario id => must be always a new one to make sure that there are no errors
    scenario_id = "DeFi " + now
    # get the first transaction time for startdate
    df = pd.DataFrame(deposit_data, columns=['time', 'amount'])
    print(df)
    # Getting the first and last time
    startdate = df['time'].iloc[0]
    enddate = df['time'].iloc[-1]
    #startdate = '2023-12-24T06:21:11' # df['time'][0].strftime('%Y-%m-%dT%H:%M:%S')
    print(f"FROM : {startdate} to {enddate}")

    # create the scenario json
    scenario_json = f""" {{
        "scenarioId" : "{scenario_id}",
        "timeSeriesData" : [],
        "termStructureData" : [ ],
        "twoDimensionalPrepaymentModelData" : [ ],
        "twoDimensionalCreditLossModelData" : [ ],
        "twoDimensionalDepositTrxModelData" : [{{
            "riskFactorId" : "DEPOSIT_TRXS",
            "depositTrxEventTimes" : [ {deposit_times} ],
            "labelSurface" : {{
            "interpolationMethod" : "NA",
            "extrapolationMethod":  "NA",
            "labelMargins"  :  [
                {{ "dimension" : 1 , "values" : [ "{address}" ]}},
                {{ "dimension" : 2, "values" : [{deposit_times}]}}],
            "data" : [[ {deposit_amounts} ]]
            }}
        }}]
        }}
    """
  

    #print(f"scenario: {json.dumps(scenario_json, indent=4)}")
    # for debug: save to json file 
    #file_path = 'scenrio.json'
    # Write the JSON data to a file
    #with open(file_path, 'w') as file:
    #    json.dump(scenario_json, file, indent=4)
    
    # create the json for the contract
    if actus_contract == 'UMP':
        contract_json = f"""{{
            "scenarioId": "{scenario_id}",
            "simulateTo": "{enddate}",
            "monitoringTimes": [],
            "contracts":[{{
                "calendar":"WEEKDAY",
                "businessDayConvention":"SCF",
                "contractType":"UMP",
                "statusDate":"{startdate}",
                "contractRole":"RPA",
                "contractID":"{address}",
                "cycleAnchorDateOfInterestPayment":"{startdate}",
                "cycleOfInterestPayment":"P6ML0",
                "nominalInterestRate":0.00,
                "dayCountConvention":"30E360",
                "currency":"{symbol}",
                "contractDealDate":"{startdate}",
                "initialExchangeDate":"{startdate}",
                "maturityDate":"{enddate}",
                "notionalPrincipal":{initial_balance_full},
                "premiumDiscountAtIED":0,
                "objectCodeOfCashBalanceModel": "DEPOSIT_TRXS"
            }}]
            }}
        """
        
    elif actus_contract == 'STK':
        contract_json = f""" {{
            "scenarioId": "{scenario_id}",
            "simulateTo": "{enddate}",
            "monitoringTimes": [],
            "contracts":[{{
                "contractType": "STK",
                "contractID": "{address}",
                "contractRole": "RPA",
                "contractDealDate": "{startdate}",
                "statusDate": "{startdate}",
                "notionalPrincipal": "1000",
                "currency": "{symbol}",
                "purchaseDate": "{startdate}",
                "priceAtPurchaseDate": "1100",
                "endOfMonthConvention": "EOM"
            }}]
        }}
        """
    else:
        contract_json = ""



    #print(f"\n\ncontract: {json.dumps(contract_json, indent=4)}")
    
    # For debug: save the contract json
    # File path where you want to save the JSON data
    #file_path = 'contract.json'
    # Write the JSON data to a file
    #with open(file_path, 'w') as file:
    #    json.dump(contract_json, file, indent=4)
    
    # define headers for post call
    headers = {
        "Content-Type": "application/json",
    }

    print(ACTUS_SERVER + "/scenarios/saveScenario")

    '''
    response_scenario = requests.post("http://localhost:8080/scenarios/saveScenario", data=scenario_json, headers=headers)

    if response_scenario.status_code == 200:
        print("/n Hurra1")
        print(response_scenario.json())
    else:
        print(f"Request failed with status code {response_scenario.status_code}")

    response_contract = requests.post("http://localhost:8080/simulations/runScenario", data=contract_json, headers=headers)

    if response_contract.status_code == 200:
        print("/n Hurra2")
        print(response_contract.json())
        actus_data = response_contract.json()
    else:
        print(f"Request failed with status code {response_contract.status_code}")

    '''    
    # first send the secenario json and if all good the contract json to the actus server
    response_scenario = requests.post(ACTUS_SERVER + "/scenarios/saveScenario", data=scenario_json, headers=headers)
    if response_scenario.status_code == 200:
        print("/n Hurra1")
        print(response_scenario.json())
        response_contract = requests.post(ACTUS_SERVER + "/simulations/runScenario", data=contract_json, headers=headers)
        if response_contract.status_code == 200:
            print("/n Hurra2")
            print(response_contract.json())
            actus_data = response_contract.json()
            # Extract the events for the scenario
            events = actus_data[0]['events']

            # Create a DataFrame
            actus_df = pd.DataFrame(events)

            # Display the table
            print("ACTUS response: \n")
            print(actus_df.to_string())
            return actus_df
        else:
            print(f"Contract request failed with status code {response_contract.status_code}")
    else:
        print(f"Scenario request failed with status code {response_scenario.status_code}")
    
    return pd.DataFrame() # return empty dataframe


def plot_balance(initial_balance_full, deposit_data, decimals):
    """
    Plot function for the loaded data 
    """

    # Extract dates and amounts from deposit and withdrawal events
    deposit_dates = [event[0] for event in deposit_data if event[1] > 0]
    deposit_amounts = [event[1]/(10**decimals) for event in deposit_data if event[1] > 0]

    withdrawal_dates = [event[0] for event in deposit_data if event[1] < 0]
    withdrawal_amounts = [event[1]/(10**decimals) for event in deposit_data if event[1] < 0]

    # Convert date strings to datetime objects
    deposit_dates = [datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S') for date_str in deposit_dates]
    withdrawal_dates = [datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S') for date_str in withdrawal_dates]

    # Create a sorted list of all events with datetime objects
    all_events = sorted(deposit_data, key=lambda x: x[0])
    all_dates = [datetime.strptime(event[0], '%Y-%m-%dT%H:%M:%S') for event in all_events]
    all_amounts = [event[1]/(10**decimals) for event in all_events]

    # Calculate the actual balance over time
    balance_over_time = [initial_balance_full]
    for amount in all_amounts:
        balance_over_time.append(balance_over_time[-1] + amount)

    # Plot deposits, withdrawals, and actual balance over time
    fig, ax = plt.subplots()

    ax.plot(deposit_dates, deposit_amounts, 'go', label='Deposits', markersize=8)
    ax.plot(withdrawal_dates, withdrawal_amounts, 'ro', label='Withdrawals', markersize=8)
    ax.plot(all_dates, balance_over_time[:-1], 'b-', label='Actual Balance', linewidth=2)

    ax.set_xlabel('Date')
    ax.set_ylabel('Amount')
    ax.set_title('Deposits, Withdrawals, and Actual Balance')

    # Format the date axis
    date_fmt = mdates.DateFormatter('%Y-%m-%d')
    ax.xaxis.set_major_formatter(date_fmt)
    fig.autofmt_xdate()

    # Add a legend
    ax.legend()
    #plt.show()

    return fig, ax


def plot_actus (actus_df):
    """
    Plot function for the results from the ACTUS calculation
    """
    # Convert time column to datetime
    actus_df['time'] = pd.to_datetime(actus_df['time'])
    # Sort DataFrame based on 'time'
    actus_df = actus_df.sort_values(by='time')
    # Plot
    fig, ax1 = plt.subplots()

    # Set the 'time' as index for plotting
    #df.set_index('time', inplace=True)

    # Plot 'nominalValue' as a blue line
    #ax1.plot(df.index, df['nominalValue'], color='blue', label='Nominal Value')
    # Plotting the nominal value as a curve
    ax1.plot(actus_df['time'], actus_df['nominalValue'], color='blue', label='Nominal Value')

    # Plot 'payoff' as red spikes
    #ax1.plot(df['time'], df['payoff'], color='red', linestyle='none', marker='o', label='Payoff')

    # Separate payoffs into positive and negative for different colors
    positive_payoffs = actus_df['payoff'] > 0
    negative_payoffs = actus_df['payoff'] < 0

    # Plot positive payoffs in green
    ax1.plot(actus_df['time'][positive_payoffs], actus_df['payoff'][positive_payoffs], color='green', linestyle='none', marker='o', label='Positive Payoff')

    # Plot negative payoffs in red
    ax1.plot(actus_df['time'][negative_payoffs], actus_df['payoff'][negative_payoffs], color='red', linestyle='none', marker='o', label='Negative Payoff')

    ax1.set_xlabel('Time')
    ax1.set_ylabel('Nominal Value', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')
    # Rotate the x-axis labels by 90 degrees
    ax1.tick_params(axis='x', rotation=90)

    # Formatting the x-axis to show the date clearly
    #ax1.xaxis.set_major_locator(mdates.MonthLocator())
    #ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    ax1.xaxis.set_major_locator(mdates.DayLocator(interval=4))  # Every 5 days
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

    # Adding a legend
    #ax1.figure.legend(loc="upper right", bbox_to_anchor=(0.1,0.9))
    ax1.legend()
    plt.title('Nominal Value and Events Over Time')
    #plt.show()

    return fig, ax1


    """
    Backup: Possibility to read INFURA id from param.json

    # Path to your JSON file
    file_path = 'param.json'
    
    # Opening JSON file and loading the data
    with open(file_path, 'r') as file:
        param = json.load(file)
    INFURA_PROJECT_ID = param['INFURA']
    """
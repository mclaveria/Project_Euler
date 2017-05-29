#Michael Claveria
#Problem 31: Coin sum

'''
With eight coin types: 1p, 2p, 5p, 10p, 20p, 50p, 100p, 200p
Find the number of ways of making 200p using any number of coins

'''

coin_type = [1, 2, 5, 10, 20, 50, 100, 200]

def numWaysSum(coinList, amt):
    res = [1] + amt * [0]
    for coin in coinList:
        for i in range(coin, amt + 1):
            res[i] += res[i - coin]
    print('Number of ways to make', amt, 'is', res[amt] )   
     
numWaysSum(coin_type, 200)    
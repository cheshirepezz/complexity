'''
At each turn you pick a coin from each pile and move it in a randomly selected pile (it can be any of the piles).
You can repeat the process an arbitrary amount of times. If a pile becomes empty, you cannot move a coin back to it. 
Therefore if there is only one pile left the game is over.

Can you guess the number of piles that will remain if you are allowed to play an infinite amount of turns?
'''
import numpy as np
import random

numberOfPiles = 10
maxIter = 100

piles = np.empty(numberOfPiles)
piles.fill(numberOfPiles)
totPiles = np.sum(piles)
numPiles = numberOfPiles
x = 0

while (x < maxIter and piles.size >= 1):
    piles = piles[np.nonzero(piles)]
    for i in np.arange(piles.size):
        piles[i] -= 1
        num = np.random.randint(piles.size)
        piles[num] += 1
    numPiles = piles.size
    x += 1

print("The number of piles remaining are: ", numPiles)

# Head & Tail
import random

test_seed = int(input(" Create a seed number: "))
random.seed(test_seed)

flip = random.randint(0,1)
if flip == 0:
    print("Heads")
else:
    print("Tails")
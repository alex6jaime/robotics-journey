import random

def coin_toss(num_tosses):
    count_heads = 0
    count_tails = 0
    for i in range(num_tosses):
        if random.randint(0, 1) == 0:
            count_heads += 1
            print("H")
        else:
            count_tails += 1
            print("T")
    return count_heads, count_tails

heads, tails =coin_toss(10)
print(f"Heads: {heads}, Tails: {tails}")
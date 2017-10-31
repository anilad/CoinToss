import random

#Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.

def cointoss():
    head=0
    tail=0
    for i in range(1,5001):
        num = random.random()
        num_rounded = round(num)
        if num_rounded == 1:
            head+=1
            print "Attempt #{}: Throwing a coin... It's a head! ... Got {} head(s) so far and {} tail(s) so far".format(i, head, tail)
        else:
            tail+=1
            print "Attempt #{}: Throwing a coin... It's a tail! ... Got {} head(s) so far and {} tail(s) so far".format(i, head, tail)

cointoss()
import math

def mce(dist):
    n = sum(dist)
    entropy = 0
    for i in dist:
        if i == 0:
            entropy -= 0
        else:
            # base-2 log
            entropy -= i/n * math.log(i/n, 2)
    return entropy 

def ae(dist):
    eset = []
    n = 0
    for i in dist:
        n += sum(i)
    for i in dist:
        a = mce(i)
        eset.append(a*sum(i)/n)
    return sum(eset)

#greater entropy = greater information


# parent entropy
dist = [3,7]
entropy = mce(dist)
print(entropy)


# child entropy (less than 2 years at job)
dist = [[3,1],[2,4]]
years = ae(dist)
print(child_entropy)

# child entropy - missed payments
dist = [[2,1],[1,6]]
missed = ae(dist)

# year information gain
entropy - years

# missed information gain
entropy - missed

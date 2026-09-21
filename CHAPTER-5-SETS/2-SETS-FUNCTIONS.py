a = {1,2,3}
b = {3,4,5}
z = {1,2}
y = {1,2,3}

# UNION
c = a.union(b)
print(c)

# INTERSECTION
d = a.intersection(b)
print(d)

# DIFFERENCE
# removes common 
e = a-b
f = b-a
print(e)
print(f)

# SUBSET
g =z<=y
print(g)

# SUPERSET
h = y>=z
print(h)

# DIS JOINT
i = a.isdisjoint(b)
print(i)

# MEMBERSHIP
k = 2 in a
print(k)

# NOT MEMBERSHIP
l = 5 not in b
print(l)
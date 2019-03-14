def num_weight(num): 
    li = list(map(int, num))
    return sum(li)

def order_weight(strng):
    weights = strng.split()
    weights.sort()
    weights.sort(key=num_weight)
    return " ".join(w)

def divisor(n):
    divs = {1, n}
    for div in range(2, int(n**0.5)+1):
        quot, rem = divmod(n, div)
        if rem == 0:
            divs |= {div, quot}
    return divs 


def div_sqr_sum(n):
    divs = {1, n}
    for div in range(2, int(n**0.5)+1):
        quot, rem = divmod(n, div)
        if rem == 0:
            divs |= {div, quot}
    return sum(x*x for x in divs)
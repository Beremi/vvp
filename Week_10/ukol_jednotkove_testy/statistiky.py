def prumer(cisla):
    return sum(cisla) / len(cisla)


def median(cisla):
    n = len(cisla)
    sorted_cisla = sorted(cisla)
    mid = n / 2
    return sorted_cisla[mid]


def rozptyl(cisla):
    n = len(cisla)
    mu = prumer(cisla)
    var = sum((x - mu) ** 2 for x in cisla) / (n - 1)
    return var

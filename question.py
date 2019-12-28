def bonAppetit(bill, k, b):
    sm = sum(bill)-bill[k]
    if sm//2 != b:
        print(b - sm//2)
    else:
        print("Bon Appetit")
bonAppetit([3, 10, 2, 9], 10, 12)
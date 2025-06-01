def knapsack(items, W):
    return knapsack_rec(items, W, len(items)-1, {})
        
def knapsack_rec(items, W, i, table):
    if(i < 0):
        return 0

    if (i, W) in table:
        return table[(i, W)]

    (v, w) = items[i]

    if w > W:
        res = knapsack_rec(items, W, i-1, table)           # do not insert item
    else:
        res = max(
            knapsack_rec(items, W, i-1, table),            # do not insert item
            knapsack_rec(items, W-w, i-1, table) + v       # insert item
        )

    table[(i, W)] = res
    return res

items = [(60, 10), (100, 20), (120, 30), (90, 25), (75, 15), (40, 5), (30, 8)]    


print(knapsack(items, 50))

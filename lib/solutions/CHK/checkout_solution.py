

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
    offers = {'A': (3, 130), 'B': (2, 45)}

    if not all(item in prices for item in skus):
        return -1

    total_cost = 0
    item_counts = {}
    for item in skus:
        item_counts[item] = item_counts.get(item, 0) + 1

    

    raise NotImplementedError()



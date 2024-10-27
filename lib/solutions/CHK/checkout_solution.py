

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
    offers = {'A': (3, 130), 'B': (2, 45)}

    # Validates the input
    if not all(item in prices for item in skus):
        return -1

    # Counts the items
    item_counts = {}
    for item in skus:
        item_counts[item] = item_counts.get(item, 0) + 1

    # Calculates total cost
    total_cost = 0
    for item, count in item_counts.items():
        if item in offers:
            offer_qty, offer_price = offers[item]
            offer_times_used = count // offer_qty
            regular_price_qty = count % offer_qty
            total_cost += offer_times_used * offer_price + regular_price_qty * prices[item]
        else:
            total_cost += count * prices[item]

    return total_cost
    # raise NotImplementedError()

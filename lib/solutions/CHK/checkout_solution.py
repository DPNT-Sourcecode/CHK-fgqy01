

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10}
    offers = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)],
    }
    free_offers = {'E': (2, 'B'), 'F': (3, 'F')}

    # Validates the input
    if not all(item in prices for item in skus):
        return -1

    # Counts the items
    item_counts = {}
    for item in skus:
        item_counts[item] = item_counts.get(item, 0) + 1

    # Applies free offers
    for item, (required_qty, free_item) in free_offers.items():
        if item in item_counts and item_counts[item] >= required_qty:
            free_items = item_counts[item] // required_qty
            if free_item == item:
                item_counts[item] -= 1
            else:
                if free_item in item_counts:
                    item_counts[free_item] = max(0, item_counts[free_item] - free_items)

    # Calculates total cost
    total_cost = 0
    for item, count in item_counts.items():
        if item in offers:
            for offer in offers[item]:
                offer_qty, offer_price = offer
                offer_times_used = count // offer_qty
                total_cost += offer_times_used * offer_price
                count %= offer_qty
            total_cost += count * prices[item]
        else:
            total_cost += count * prices[item]

    return total_cost
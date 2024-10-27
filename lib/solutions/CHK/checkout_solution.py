

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    prices = {
        'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10,
        'G': 20, 'H': 10, 'I': 35, 'J': 60, 'K': 80, 'L': 90,
        'M': 15, 'N': 40, 'O': 10, 'P': 50, 'Q': 30, 'R': 50,
        'S': 30, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 90,
        'Y': 10, 'Z': 50
    }

    offers = {
        'A': [(3, 130), (5, 200)],
        'B': [(2, 45)],
        # 'E': [(2, 'B')],
        # 'F': [(2, 'F')],
        'H': [(5, 45), (10, 80)],
        'K': [(2, 150)],
        # 'N': [(3, 'M')],
        'P': [(5, 200)],
        'Q': [(3, 80)],
        # 'R': [(3, 'Q')],
        # 'U': [(3, 'U')],
        'V': [(2, 90), (3, 130)]
    }

    free_offers = {
        'E': (2, 'B'),
        'F': (3, 'F'),
        'N': (3, 'M'),
        'R': (3, 'Q'),
        'U': (4, 'U')
    }

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
                item_counts[item] -= free_items
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



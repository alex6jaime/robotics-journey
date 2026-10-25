inventory = {
    "rope": 1,
    "torch": 6,
    "gold coin": 42,
    "dagger": 1,
    "arrow": 12
}

def display_inventory(items):
    total = 0
    print("Inventory:")
    for item, count in items.items():
        print(f"{count} {item}")
        total += count

    print(f"Total number of items: {total}")

display_inventory(inventory)
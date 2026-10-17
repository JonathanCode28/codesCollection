items = [1, 2, 4, 3, 5, 6, 8, 7]

for item in items:
    print(f"checking {item}, list: {items}")
    if item % 2 == 0:
        print(f"removing {item}")
        items.remove(item)
print("final list: ", items)
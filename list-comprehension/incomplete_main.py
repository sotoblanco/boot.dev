def find_powerful_sword(inventory):
    powerful_swords = []
    for item in inventory:
        if item > 4:
            powerful_swords.append(item)
    return powerful_swords

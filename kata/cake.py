def cakes(recipe, available):
    completed = 0
    baking = True
    recipe_items = recipe.keys()

    for item in recipe_items:
        if not available.get(item):
            return 0

    while baking:
        for item in recipe_items:
            available[item] = available[item] - recipe[item]
            if available[item] <= 0:
                baking = False
        if baking:
            completed += 1

    return completed


print(cakes(recipe, available))
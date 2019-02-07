def cakes(recipe, available):
    completed = 0
    baking = True
    recipe_ings = recipe.keys()

    for ing in recipe_keys:
        if not available.get(ing):
            return 0

    while baking:
        for ing in recipe_ings:
            available[ing] = available[ing] - recipe[ing]
            if available[ing] <= 0:
                baking = False
        if baking:
            completed += 1

    return completed


print([min(available[ing]/recipe[ing] if ing in available else 0 for ing in recipe)])

print(cakes(recipe, available))
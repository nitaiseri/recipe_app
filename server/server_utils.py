from recipe import Recipe
from data_base.db_maneger import db_manager

class SensitivityNotExist(Exception):
    pass

sensitivities = {"gluten": "gluten_ingredient", 
                "dairy": "dairy_ingredient"}

def parse_recipes_data(raw_recipies_list):
    return [Recipe(raw_recipe) for raw_recipe in raw_recipies_list]

def filter_by_sensitivity(recipes, sensitivity):
    if sensitivity not in sensitivities.keys():
        raise SensitivityNotExist
    table_name = sensitivities[sensitivity]
    forbidden_ingredients = [ingredient["name"] for ingredient in db_manager.get_ingredients(table_name)]
    return list(filter(lambda recipe: not recipe.contain_any(forbidden_ingredients), recipes))
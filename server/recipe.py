
class Recipe:
    def __init__(self, recipe_raw_object) -> None:
        self.ingredients = recipe_raw_object["ingredients"]
        self.title = recipe_raw_object["title"]
        self.href = recipe_raw_object["href"]
        self.thumbnail = recipe_raw_object["thumbnail"]

    def get_ingredients(self):
        return self.ingredients
    
    def contain_any(self, ingredients_list) -> bool:
        return not set(ingredients_list).isdisjoint(self.ingredients)
        
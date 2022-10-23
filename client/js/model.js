class Model {

    constructor() {
        this.recipes = [];
    }

    async findRecipes(ingrediend, glutenFree, diaryFree) {
        let url = `http://localhost:8000/recipes/${ingrediend}`
        if (glutenFree) {
            url += `?sensitivity=gluten`
        }
        else if (diaryFree) {
            url += `?sensitivity=diary`
        }

        let recipes = await $.get(url);
        this.recipes = recipes;
    }

    getRecipes() {
        return this.recipes;
    }
}
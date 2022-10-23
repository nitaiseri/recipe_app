const model = new Model();
const renderer = Renderer();

$('#search-btn').on('click', function () {
    const word = $("#input").val();
    $("#input").val("");
    const glutenFree = $("#gluten").prop("checked");
    const diaryFree = $("#diary").prop("checked");
    $("#gluten").prop("checked", false);
    $("#diary").prop("checked", false);

    model.findRecipes(word, glutenFree, diaryFree).then((result) => {
        recipes = { recipes: model.getRecipes() }
        renderer.render(recipes);
    })
})

$("#recipes-container").on('click', "img", function () {
    alert($(this).closest(".recipe").find("#ingredients").text())
    alert("I know it's not the first");
    alert("Perdon");
})


const Renderer = function() {

    function render(recipes) {
        $("#recipes-container").empty();
        let source = $('#recipe-template').html();
        const template = Handlebars.compile(source);
        const newHTML = template(recipes);
        // append our new html to the page
        $("#recipes-container").append(newHTML);
    }

    // function renderHeader(userName){
    //     let header = $("#header");
    //     let head = document.createElement("h1");
    //     let text = document.createTextNode(`Hello - ${userName}`);
    //     head.appendChild(text);
    //     header.empty();
    //     header[0].appendChild(head);
    // }

    return {
        render
    }
}
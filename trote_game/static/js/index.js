$(document).ready(function(){
    $(document).on('click', ".continuar", function(){
        var proximo = parseInt($(this).data("next"));
        $(".fala").addClass("hidden");
        $(".opcoes").addClass("hidden");
        $("." + proximo).removeClass("hidden");
    });
});

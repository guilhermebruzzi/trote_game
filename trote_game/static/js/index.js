$(document).ready(function(){
    $(document).on('click', ".continuar", function(){
        var proximo = parseInt($(this).data("next"));
        $(".fala").addClass("hidden");
        $(".fala-" + proximo).removeClass("hidden");
    });
});

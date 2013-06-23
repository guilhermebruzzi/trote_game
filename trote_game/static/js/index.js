if (typeof String.prototype.startsWith != 'function') {
    // see below for better implementation!
    String.prototype.startsWith = function (str){
        return this.indexOf(str) == 0;
    };
}
if (typeof String.prototype.endsWith != 'function') {
    String.prototype.endsWith = function (str){
        return this.slice(-str.length) == str;
    };
}

function exibeResultados(elm, proximo){
    var sala = $(elm).parent().parent().parent();
    var salaId = sala.data("sala");
    sala.addClass("hidden");
    var resultados = sala.parent().find("." + proximo);
    resultados.removeClass("hidden");
    var resultadoId = "";
    $(".opcao-sala-" + salaId).each(function(){
        if($(this).is(":checked")){
            resultadoId = $(this).val();
        }
    });
    $("#resultados-" + salaId + "-" + resultadoId).removeClass("hidden");
}

$(document).ready(function(){
    $(document).on('click', ".continuar", function(event){
        var proximo = $(this).data("next");
        $(".fala").addClass("hidden");
        if (proximo.startsWith("resultados-")){
            exibeResultados(this, proximo);
        }
        else{
            $("." + proximo).removeClass("hidden");
        }
        event.preventDefault();
    });
});

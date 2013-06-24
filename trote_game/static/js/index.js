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
    var resultadoId = "";
    $(".opcao-sala-" + salaId).each(function(){
        if($(this).is(":checked")){
            resultadoId = $(this).val();
        }
    });
    var resultados = $("#resultados-" + salaId + "-" + resultadoId);
    resultados.removeClass("hidden");
    resultados.find(".resultado-" + salaId + "-0").removeClass("hidden");
}

function exibeSala(elm, proximo){
    var resultados = $(elm).parent().parent().parent();
    resultados.addClass("hidden");
    $(".sala").addClass("hidden");
    var sala = $("#" + proximo);
    sala.removeClass("hidden");
    sala.find(".fala-0").removeClass("hidden");
}

$(document).ready(function(){
    $(document).on('click', ".continuar", function(event){
        var proximo = $(this).data("next");
        $(".fala").addClass("hidden");
        if (proximo.startsWith("resultados-")){
            exibeResultados(this, proximo);
        }
        else if(proximo.startsWith("sala-")){
            exibeSala(this, proximo)
        }
        else if(proximo == "perdeu" || proximo == "venceu"){
            return true;
        }
        else{
            $("." + proximo).removeClass("hidden");
        }
        event.preventDefault();
    });
});

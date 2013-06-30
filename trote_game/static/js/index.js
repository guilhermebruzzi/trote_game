if (typeof String.prototype.startsWith != 'function') {
    String.prototype.startsWith = function (str){
        return this.slice(0, str.length) == str;
    };
}

if (typeof String.prototype.endsWith != 'function') {
    String.prototype.endsWith = function (str){
        return this.slice(-str.length) == str;
    };
}

var jaPassouPelaSala6 = false; // Necessário para ganhar o jogo

function limpaOpcoes(sala){
    var salaId = sala.data("sala");
    sala.find(".opcao-sala-" + salaId).each(function(){
        $(this).prop('checked', false);
    });
}

function exibeResultados(elm, proximo){
    var sala = $(elm).parent().parent().parent();
    var salaId = sala.data("sala");
    var resultadoId = "";
    $(".opcao-sala-" + salaId).each(function(){
        if($(this).is(":checked")){
            resultadoId = $(this).val();
        }
    });
    if(resultadoId == ""){
        alert("Escolha uma opcao!");
        return;
    }
    $(".fala").addClass("hidden");
    sala.addClass("hidden");
    var resultados = $("#resultados-" + salaId + "-" + resultadoId);
    resultados.removeClass("hidden");
    resultados.find(".resultado-" + salaId + "-0").removeClass("hidden");
}

function mostraSalaDaVez(sala){
    $(".sala").addClass("hidden");
    sala.removeClass("hidden");
    $(".fala").addClass("hidden");
    sala.find(".fala-0").removeClass("hidden");
    limpaOpcoes(sala);
}

function exibeSala(elm, proximo){
    var resultados = $(elm).parent().parent().parent();
    resultados.addClass("hidden");

    var sala = $("#" + proximo);
    var salaId = sala.data("sala");
    if(salaId == 6){
        jaPassouPelaSala6 = true;
    }
    if(jaPassouPelaSala6 && salaId == 4){
        sala = $("#sala-7"); // Última sala
        mostraSalaDaVez(sala);
    }
    else{
        mostraSalaDaVez(sala);
    }
}

$(document).ready(function(){
    $(".sala").each(function(){
        limpaOpcoes($(this));
    });

    $(document).on('click', "#botao-entrar", function(event){
        $("#capa-do-jogo").addClass("hidden");
        $("#cenario").removeClass("hidden");
        event.preventDefault();
    });

    $(document).on('click', ".continuar", function(event){
        var proximo = $(this).data("next");
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
            $(".fala").addClass("hidden");
            $("." + proximo).removeClass("hidden");
        }
        event.preventDefault();
    });
});

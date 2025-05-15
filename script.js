function validarNumero(){
    let numero = document.getElementById("numero").value;

    let mensagem = document.getElementById("mensagem");

    if(numero === ""){
        mensagem.textContent = "Insira algum valor.";
        mensagem.style.color = "red";
    } else {
        numero = parseInt(numero)
        
        if (numero>10){
            mensagem.textContent = "O número é maior que 10.";
            mensagem.style.color = "green";
        } else {

            if (numero > 5){
                mensagem.textContent = "O número é maior que 5, mas menor ou igual a 10."
                mensagem.style.color = "orange"
            } else {
                mensagem.textContent = "O número é menor ou igual a 5.";
                mensagem.style.color = "blue";
            }
        }
    }
}
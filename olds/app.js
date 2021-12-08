function number() {
    var nombre1 = document.getElementById("TextInput").value;
    var nombre2 = document.getElementById("TextInput2").value;
    nombre_random_1 = Math.floor((Math.random() * nombre2) + nombre1);
    nombre_random_2 = Math.floor((Math.random() * nombre2) + nombre1);

    console.log(nombre_random_1, nombre_random_2);
    if (nombre_random_1 >= 0 && nombre_random_2 >= 0){
        document.getElementById("calcul").innerHTML = "What the result of: " + nombre_random_1 + " mutiplied by: " + nombre_random_2
    }else{
        document.getElementById("calcul").innerHTML = "First or second number must be greater or equal to 0."
    }

    
    
    var x = document.getElementById("resultDiv");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
};
var playerInp = document.getElementById("player");
var playerInp2 = document.getElementById("player1");

playerInp.addEventListener("input", ()=> {
    playerInp2.value = playerInp.value;
})
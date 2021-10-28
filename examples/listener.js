const buttonElement = document.getElementById("ani-button")
buttonElement.addEventListener('click', function(event){
    console.log(event)
    this.innerText = "Minam is jeff" 
})


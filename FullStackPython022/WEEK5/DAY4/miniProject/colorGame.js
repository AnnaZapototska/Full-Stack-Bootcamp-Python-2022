

generateCollors()
listenToMain()
let currentColor
let isMousePressed = false
let chosenColor
let but1 = document.querySelector(".clear button")
but1.addEventListener("click", clearCanvas)

function generateCollors(){
    let colorDivs = document.querySelectorAll(".color")
    let color = generateRandomColor()
    for(let colorDiv of colorDivs){
        let color = generateRandomColor()
        colorDiv.style.backgroundColor = color
        colorDiv.addEventListener("click", setCurrentColor)
        colorDiv.dataset.color = color
    }
}

function generateRandomColor(){
    let hex = Math.floor(Math.random() * 16777215).toString(16)
    return "#" + hex
}

function setCurrentColor(e){
 currentColor = e.target.dataset.color
 chosenColor = currentColor
 let but = document.querySelector(".clear button")
 but.style.backgroundColor = chosenColor
}

function listenToMain(){
    let main = document.getElementById("main")
    main.addEventListener("mousedown", handleClick)
    main.addEventListener("mousemove", handleMove)
    document.body.addEventListener("mouseup", handleUp)
}


function handleClick(){
if(currentColor == null) return
console.log(currentColor);
isMousePressed = true
}

function handleMove(e){
if(!isMousePressed) return
console.log("cordinates: ", e.x, e.y);
let currentDiv = document.elementFromPoint(e.x, e.y)
currentDiv.style.backgroundColor = currentColor
}
function handleUp(){
    isMousePressed = false
}

function clearCanvas(){
    currentColor = null
    let squares = document.querySelectorAll("#main > div")
    for(let square of squares){
        square.style.backgroundColor = 'white'
    }
}
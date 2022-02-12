const grid = document.querySelector(".gridContainer");
const userInput = document.getElementById("quantity");
const resetButton = document.querySelector(".reset");

const grid1 = document.querySelector(".gridContainer1");

createGrid1 = () => {
  for (let i = 0; i < 25; i++) {
    const div = document.createElement("div");
    div.classList.add("square");
    grid1.appendChild(div);
   }
};

createGrid = () => {
  for (let i = 0; i < 25; i++) {
    const div = document.createElement("div");
    div.classList.add("square");
    grid.appendChild(div);
  }
};

updateGrid = () => {
  grid.innerHTML = "";
  grid.style.setProperty(
    "grid-template-columns",
  );
  grid.style.setProperty(
    "grid-template-rows",
  );
};

const square = document.querySelector("div");
square.addEventListener("click", function(event) {
  if(event.target.classList[0] == "square"){
    event.target.classList.replace("square", "color");
  }else{
    event.target.classList.replace("color", "square");
  }
  console.log(event.target.classList);
});

userInput.addEventListener("change", updateGrid);

resetButton.addEventListener("click", function() {
  grid.innerHTML = "";
  grid.style.setProperty("grid-template-columns", `repeat(5, 2fr)`);
  grid.style.setProperty("grid-template-rows", `repeat(5, 2fr)`);
  createGrid();
});

createGrid();
createGrid1();

botonAnalizar = () => {
  document.getElementById('boton1').style.display = 'inline';
  document.getElementById('boton2').style.display = 'none';
  document.getElementById('navAnalizar').className = 'nav-link active';
  document.getElementById('navCargar').className = 'nav-link';
  document.getElementById('ocultarGrid1').style.display = 'inline';
};

botonCargar = () => {
  document.getElementById('boton1').style.display = 'none';
  document.getElementById('boton2').style.display = 'inline';
  document.getElementById('navAnalizar').className = 'nav-link';
  document.getElementById('navCargar').className = 'nav-link active';
  document.getElementById('ocultarGrid1').style.display = 'none';
};
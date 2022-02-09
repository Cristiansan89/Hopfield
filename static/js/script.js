const grid = document.querySelector(".gridContainer");
const userInput = document.getElementById("quantity");
const resetButton = document.querySelector(".reset");

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
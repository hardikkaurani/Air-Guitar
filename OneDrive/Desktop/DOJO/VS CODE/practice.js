// if(score >= 90){
//   console.log("Excellent");
// } else if(score >= 80){
//   console.log("Very good");
// } else if(score >= 70){
//   console.log("Good");
// } else {
//   console.log("Improve");
// }




// function greet() {
//   console.log("Hello, Kalvian!");
// }

// greet();   // calling the function


// function greet() {
//     console.log("Hello Kalvium");
// }

// greet();


// function add(a, b) {
//   return a + b;
// }





const title = document.getElementById('title');
const desc = document.querySelector('.desc');
const button = document.getElementById('change');

button.addEventListener('click', () => {
  title.textContent = "DOM Manipulation in Action!";
  desc.style.color = "blue";
});


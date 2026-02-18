/*
 * JavaScript Basics Tutorial
 * ==========================
 * 
 * JavaScript makes web pages interactive and dynamic.
 * It can respond to user actions, modify page content, and much more.
 * 
 * To use this file in HTML:
 * <script src="javascript_basics.js"></script>
 * 
 * Or put JavaScript directly in HTML using <script> tags.
 */

// ====================
// CONSOLE OUTPUT
// ====================

console.log("Hello, JavaScript!");
console.log("Check the browser console (F12) to see this output");

// ====================
// VARIABLES
// ====================

// Modern JavaScript uses let and const
let name = "Alice";
let age = 25;
const PI = 3.14159; // const cannot be changed

console.log("Name:", name);
console.log("Age:", age);

// ====================
// DATA TYPES
// ====================

let text = "Hello";           // String
let number = 42;              // Number
let decimal = 3.14;           // Number (no separate float type)
let isTrue = true;            // Boolean
let nothing = null;           // Null
let notDefined;               // Undefined
let array = [1, 2, 3];       // Array
let object = { key: "value" }; // Object

console.log("Type of text:", typeof text);
console.log("Type of number:", typeof number);

// ====================
// OPERATORS
// ====================

let x = 10;
let y = 5;

console.log("x + y =", x + y);   // Addition
console.log("x - y =", x - y);   // Subtraction
console.log("x * y =", x * y);   // Multiplication
console.log("x / y =", x / y);   // Division
console.log("x % y =", x % y);   // Modulo (remainder)

// String concatenation
let greeting = "Hello" + " " + "World";
console.log(greeting);

// Template literals (modern way)
let message = `My name is ${name} and I'm ${age} years old`;
console.log(message);

// ====================
// CONDITIONALS
// ====================

let score = 85;

if (score >= 90) {
    console.log("Grade: A");
} else if (score >= 80) {
    console.log("Grade: B");
} else if (score >= 70) {
    console.log("Grade: C");
} else {
    console.log("Grade: F");
}

// Ternary operator (shorthand if/else)
let status = age >= 18 ? "Adult" : "Minor";
console.log("Status:", status);

// ====================
// LOOPS
// ====================

// For loop
console.log("\nCounting with for loop:");
for (let i = 1; i <= 5; i++) {
    console.log(i);
}

// While loop
console.log("\nCounting with while loop:");
let count = 0;
while (count < 3) {
    console.log("Count:", count);
    count++;
}

// Loop through array
let fruits = ["apple", "banana", "cherry"];
console.log("\nFruits:");
for (let fruit of fruits) {
    console.log("-", fruit);
}

// ====================
// FUNCTIONS
// ====================

// Function declaration
function greet(personName) {
    return `Hello, ${personName}!`;
}

console.log(greet("Alice"));

// Function expression
const add = function(a, b) {
    return a + b;
};

console.log("5 + 3 =", add(5, 3));

// Arrow function (modern syntax)
const multiply = (a, b) => a * b;
console.log("4 * 7 =", multiply(4, 7));

// Function with default parameter
const greetWithTitle = (personName, title = "Friend") => {
    return `Hello, ${title} ${personName}!`;
};

console.log(greetWithTitle("Bob"));
console.log(greetWithTitle("Charlie", "Dr."));

// ====================
// ARRAYS
// ====================

let numbers = [10, 20, 30, 40, 50];

// Array methods
console.log("\nArray operations:");
console.log("Length:", numbers.length);
console.log("First element:", numbers[0]);
console.log("Last element:", numbers[numbers.length - 1]);

numbers.push(60);  // Add to end
console.log("After push:", numbers);

numbers.pop();     // Remove from end
console.log("After pop:", numbers);

// Array iteration methods
numbers.forEach(num => {
    console.log("Number:", num);
});

// Map: transform each element
let doubled = numbers.map(num => num * 2);
console.log("Doubled:", doubled);

// Filter: keep elements that match condition
let bigNumbers = numbers.filter(num => num > 25);
console.log("Numbers > 25:", bigNumbers);

// ====================
// OBJECTS
// ====================

let person = {
    firstName: "John",
    lastName: "Doe",
    age: 30,
    email: "john@email.com",
    greet: function() {
        return `Hi, I'm ${this.firstName}`;
    }
};

console.log("\nPerson object:");
console.log("Name:", person.firstName, person.lastName);
console.log("Age:", person.age);
console.log(person.greet());

// Accessing properties
console.log(person.email);
console.log(person["email"]); // Alternative syntax

// Adding properties
person.phone = "555-1234";
console.log("Phone:", person.phone);

// ====================
// DOM MANIPULATION
// ====================

// These examples work when included in an HTML page

// Select element by ID
// let element = document.getElementById("myElement");

// Select elements by class
// let elements = document.getElementsByClassName("myClass");

// Select with CSS selector
// let element = document.querySelector(".myClass");
// let elements = document.querySelectorAll(".myClass");

// Modify content
// element.textContent = "New text";
// element.innerHTML = "<strong>Bold text</strong>";

// Modify styles
// element.style.color = "red";
// element.style.fontSize = "20px";

// Add/remove classes
// element.classList.add("active");
// element.classList.remove("active");
// element.classList.toggle("active");

// ====================
// EVENT HANDLING
// ====================

// Add event listener
// button.addEventListener("click", function() {
//     console.log("Button clicked!");
// });

// Common events:
// - click
// - mouseover
// - mouseout
// - keydown
// - keyup
// - submit
// - load

// ====================
// PRACTICAL EXAMPLES
// ====================

// Example 1: Calculate total price
function calculateTotal(prices) {
    let total = 0;
    for (let price of prices) {
        total += price;
    }
    return total;
}

let cart = [10.99, 5.50, 3.25];
console.log("\nCart total:", calculateTotal(cart));

// Example 2: Filter array
function getEvenNumbers(numbers) {
    return numbers.filter(num => num % 2 === 0);
}

console.log("Even numbers:", getEvenNumbers([1, 2, 3, 4, 5, 6]));

// Example 3: String manipulation
function capitalize(str) {
    return str.charAt(0).toUpperCase() + str.slice(1);
}

console.log("Capitalized:", capitalize("hello"));

// ====================
// EXERCISES
// ====================

/*
Try these exercises:

1. Create a function that checks if a number is even or odd
2. Create a function that reverses a string
3. Create a function that finds the largest number in an array
4. Create an object representing a car with properties and methods
5. Create a function that counts vowels in a string
*/

// Your code here:

function isEven(num) {
    return num % 2 === 0;
}

function reverseString(str) {
    return str.split("").reverse().join("");
}

function findMax(numbers) {
    return Math.max(...numbers);
}

console.log("\nExercise results:");
console.log("Is 4 even?", isEven(4));
console.log("Reverse 'hello':", reverseString("hello"));
console.log("Max of [3,7,2,9,1]:", findMax([3,7,2,9,1]));

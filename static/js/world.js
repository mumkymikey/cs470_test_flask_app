"use strict";

// Collect all the 'path' tags from world.html and store it in a NodeList (similar to an array)
const country_selectables = document.querySelectorAll("path");

// Create an empty array that will hold all country names
let country_names = [];

//console.log(country_selectables);

// Extract the country's name from each 'path' tag in world.html
country_selectables.forEach((country) => {
  let name;
  if (country.classList.value) {
    name = country.classList.value;
  } else {
    name = country.attributes.name.value;
  }

  // Unique entries only
  if (country_names.indexOf(name) === -1) {
    country_names.push(name);
  }
});

// printName: receives a 'path' tag as a parameter and outputs the country's name to the console
function printName(item) {
  if (item.classList.value) {
    console.log(item.classList.value);
    $.post( "/countrymethod", {
      country_data: item.classList.value
    });
  } else {
    console.log(item.attributes.name.value);
    $.post( "/countrymethod", {
      country_data: item.attributes.name.value
    });
  }
}

// ***** EVENT LISTENERS *****
// Listens for actions on the world map
country_selectables.forEach((country) => {
  country.addEventListener(
    "click",
    () => {
      printName(country);
    },
    false
  );
});

//console.log(country_names);
const svg_map = document.querySelector("svg");

"use strict";
  
console.log("Loading js");
const addBtn = document.querySelector("#addBtn");


addBtn.addEventListener('click', (event)=>{
  console.log(`${event.target} was clicked`)
})

document.getElementsByClassName('card__product').addEventListener('click', function(event) {
  console.log(`clicked on ${event.target.id} \n`)
  if (event.target.id === 'buyBtn') {
    alert('Fonctionnalité non disponible :(');
  }
  if (event.target.id === 'infoBtn') {
    alert('Fonctionnalité non disponible :(');
  }
})

document.querySelectorAll('.infoBtn').forEach((infoBtn) => {
  infoBtn.addEventListener('click', (e) => {
    alert('Fonctionnalité non disponible :(');
  });
});
const buyBtn = document.getElementById('buyBtn');
buyBtn.addEventListener('click', (e) => {
  alert('Fonctionnalité non disponible :(');
})
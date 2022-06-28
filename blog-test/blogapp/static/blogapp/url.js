
let header = document.querySelector('header');
let main = document.querySelector('main');
main.style.paddingTop = header.offsetHeight + 'px';
let link = document.querySelector('.links');

function menu(){
  link.classList.toggle('active');
}
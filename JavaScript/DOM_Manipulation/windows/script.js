'use strict';

const modal = document.querySelector('.modal');
const overlay = document.querySelector('.overlay');
const btnCloseModal = document.querySelector('.close-modal');
// NodeList getElementsByClass HTML collection
const btnsOpenModal = document.querySelectorAll('.show-modal');

const openModal = function() {
    modal.classList.remove('hidden')
    overlay.classList.remove('hidden')
};

const closeModal = function() {
    modal.classList.add('hidden')
    overlay.classList.add('hidden')
};

for(let i=0; i<btnsOpenModal.length; i++) {
    btnsOpenModal[i].addEventListener('click', openModal)
};

btnCloseModal.addEventListener('click', closeModal)
overlay.addEventListener('click', closeModal)
document.addEventListener('keydown', (e) => {
    if(e.keyCode == 27) {
        closeModal()
    }
})
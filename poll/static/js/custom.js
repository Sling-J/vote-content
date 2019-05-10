// Slider Effect

const changePersonBtn = document.querySelectorAll('.person-is-voted');
const personListBox = document.querySelector('.person-list-box');

if (personListBox) { 
   var currentWrap = personListBox.firstElementChild
   currentWrap.classList.add('active');
};

changePersonBtn.forEach(item => {
   item.addEventListener('click', () => {
      const activeWrap = currentWrap.nextElementSibling;

      currentWrap.classList.remove('active');
      activeWrap.classList.add('active');
      currentWrap = activeWrap;

      if (activeWrap.nextElementSibling === null) {
         activeWrap.classList.remove('active');
         return;
      };

      if (!activeWrap) return;
   });
});
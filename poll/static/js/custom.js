const changePersonBtn = document.querySelectorAll('.checkbox');
const wrapBox = document.querySelector('.wrap-box');

if (wrapBox) { 
   var currentWrap = wrapBox.firstElementChild
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
function toggleSubMenu(element) {
    const submenu = element.nextElementSibling;
    const chevron = element.querySelector('.fas.fa-chevron-down');

    element.classList.toggle('active');
    submenu.classList.toggle('active');

    if (submenu.classList.contains('active')) {
        chevron.style.transform = 'rotate(180deg)';
    } else {
        chevron.style.transform = 'rotate(0deg)';
    }
}

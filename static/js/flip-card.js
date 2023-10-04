document.addEventListener('DOMContentLoaded', function () {
    const flipButtons = document.querySelectorAll('.flip');

    flipButtons.forEach(button => {
        button.addEventListener('click', function () {
            const card = button.closest('.relative');
            const frontSide = card.querySelector('.front');
            const backSide = card.querySelector('.back');
            
            frontSide.classList.toggle('opacity-0');
            backSide.classList.toggle('opacity-0');
        });
    });
});

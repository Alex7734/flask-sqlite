document.addEventListener('DOMContentLoaded', function () {
    const problemItems = document.querySelectorAll('.problem-item');

    problemItems.forEach(item => {
        item.addEventListener('click', function () {
            const details = this.querySelector('.problem-details');
            const solve = this.querySelector('.problem-details-solve');
            details.classList.toggle('visible');
            solve.classList.toggle('visible');
        });
    });
});


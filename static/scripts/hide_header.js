// This short script allows the user to hide the header on Clue.html, giving them more space for notes
//          (Maybe we can add it to other pages too?) 


document.getElementById('toggle-header').addEventListener('click', function () {
    const header = document.getElementById('page-header');
    header.classList.toggle('collapsed');
});
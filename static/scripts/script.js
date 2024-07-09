document.addEventListener('click', function(event) {
    var dropbtn = document.querySelector('.dropbtn');
    var dropContent = document.querySelector('.drop-content');

    if (dropbtn.contains(event.target)) {
        dropContent.style.display = dropContent.style.display === 'block' ? 'none' : 'block';
    }else {
        dropContent.style.display = 'none';
    }
});
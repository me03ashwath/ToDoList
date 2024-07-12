document.addEventListener('click', function(event) {
    var dropbtn = document.querySelector('.dropbtn');
    var dropContent = document.querySelector('.drop-content');

    if (dropbtn.contains(event.target)) {
        dropContent.style.display = dropContent.style.display === 'block' ? 'none' : 'block';
    }else {
        dropContent.style.display = 'none';
    }
});

function clearDefaultValue(element) {
    if (element.value == 'new topic') {
        element.value = '';
        element.style.color = 'rgba(0,0,0,1)';
    }
}

function restoreDefaultValue(element, defaultvalue) {
    if (element.value == '') {
            element.value = defaultvalue;
            element.style.color = 'rgba(0,0,0,.5)';
    }
}
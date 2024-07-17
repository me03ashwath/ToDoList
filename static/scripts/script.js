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

function redirectToTopic(topicId) {
    window.location.href = `/topic/${topicId}`;
}

function hoverDim(element) {
    const dimElement = element.querySelector('.dim');
    if (dimElement.style.opacity != '.8') {
        dimElement.style.opacity = '.8';
    }
}

function resetDim(element) {
    const dimElement = element.querySelector('.dim');
    if (dimElement.style.opacity != '1') {
        dimElement.style.opacity = '1';
    }
}

function deleteTopic(topicId, event) {
    event.stopPropagation();
    if (confirm("Are you sure you want to delete this?")) {
        window.location.href = `/delete-topic/${topicId}/`;
    }
}


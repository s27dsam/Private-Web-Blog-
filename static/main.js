function toggleComment(formIndex) {
    // Parse the index to an integer if necessary
    var index = parseInt(formIndex, 10);
    toggleCommentForm(index);
}

function toggleCommentForm(index) {
    var form = document.getElementById('comment-form-' + index);
    form.style.display = form.style.display === 'none' ? 'block' : 'none';
}


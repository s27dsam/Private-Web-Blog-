function toggleComment(formIndex) {
    // Parse the index to an integer if necessary
    var index = parseInt(formIndex, 10);
    toggleCommentForm(index);
}

function toggleCommentForm(index) {
    var form = document.getElementById('comment-form-' + index);
    form.style.display = form.style.display === 'none' ? 'block' : 'none';
}

function openEmailClient() {
        var subject = "New Signup Request";
        var body = "Hello, I'm interested in signing up. Please send me more information.";
        var mailtoLink = "mailto:s2711dsam@gmail.com?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);


        window.location.href = mailtoLink;
    }

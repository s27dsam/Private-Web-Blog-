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
        var body = "Make your case below as to why you should be allowed to join the form.";
        var mailtoLink = "mailto:s2711dsam@gmail.com?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);


        window.location.href = mailtoLink;
    }

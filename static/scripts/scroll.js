// This bit of code allows the user to stay at the same point on the page upon form submission

document.addEventListener('DOMContentLoaded', function () {
    const leftPane = document.querySelector('.left-pane');

    // Save both window and left pane scroll positions in localStorage on form submission
    document.querySelectorAll('.ajax-form').forEach(form => {
        form.addEventListener('submit', function () {
            localStorage.setItem('windowScrollPosition', window.scrollY);
            if (leftPane) {
                localStorage.setItem('leftPaneScrollPosition', leftPane.scrollTop);
            }
        });
    });

    // Restore both window and left pane scroll positions when the page loads
    const savedWindowPosition = localStorage.getItem('windowScrollPosition');
    const savedLeftPanePosition = localStorage.getItem('leftPaneScrollPosition');

    if (savedWindowPosition !== null) {
        window.scrollTo(0, parseInt(savedWindowPosition));
        localStorage.removeItem('windowScrollPosition'); // Clean up storage
    }

    if (savedLeftPanePosition !== null && leftPane) {
        leftPane.scrollTop = parseInt(savedLeftPanePosition);
        localStorage.removeItem('leftPaneScrollPosition'); // Clean up storage
    }
});

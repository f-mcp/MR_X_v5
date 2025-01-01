// JavaScript for dragging the resizer and resizing the left and right panes
$(document).ready(function () {
    const resizer = $('#resizer');
    const leftPane = $('.left-pane');
    const rightPane = $('.right-pane');
    const container = $('.flex-container');
    let isResizing = false;

    // Load saved resizer position from localStorage
    const loadResizerPosition = () => {
        const savedPosition = localStorage.getItem('resizerPosition');
        if (savedPosition) {
            const resizerState = JSON.parse(savedPosition);
            const containerWidth = container.width();
            if (resizerState.leftPaneWidth) {
                const leftWidth = parseFloat(resizerState.leftPaneWidth);
                if (leftWidth > 50 && leftWidth < containerWidth - 50) { // Ensure valid range
                    leftPane.css('width', `${leftWidth}px`);
                    rightPane.css('width', `${containerWidth - leftWidth}px`);
                }
            }
        }
    };

    // Save resizer position to localStorage
    const saveResizerPosition = () => {
        const leftWidth = leftPane.width(); // Current width of the left pane
        const resizerState = {
            leftPaneWidth: leftWidth
        };
        localStorage.setItem('resizerPosition', JSON.stringify(resizerState));
    };

    // Initialize resizer position
    loadResizerPosition();

    // Handle mousedown on resizer
    resizer.on('mousedown', function (e) {
        isResizing = true;
        $('body').addClass('resizing');
    });

    // Handle mousemove to resize panes
    $(document).on('mousemove', function (e) {
        if (!isResizing) return;
        const containerOffset = container.offset().left;
        const newLeftWidth = e.pageX - containerOffset;
        const containerWidth = container.width();
        const minPaneWidth = 50; // Minimum width in pixels

        // Prevent panes from becoming too small
        if (newLeftWidth < minPaneWidth || newLeftWidth > containerWidth - minPaneWidth) return;

        // Resize the panes
        leftPane.css('width', `${newLeftWidth}px`);
        rightPane.css('width', `${containerWidth - newLeftWidth}px`);

        // Save position dynamically while resizing
        saveResizerPosition();
    });

    // Handle mouseup to stop resizing
    $(document).on('mouseup', function () {
        if (isResizing) {
            isResizing = false;
            $('body').removeClass('resizing');
            saveResizerPosition(); // Ensure position is saved after resizing stops
        }
    });
});

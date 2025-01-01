// This script (should) enable the user to take notes on the right pane of Clue.html


let paths = []; // To store drawing actions
let currentPath = null;


document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('drawing-canvas');
    const ctx = canvas.getContext('2d');
    const drawingPad = document.getElementById('drawing-pad');

    // Ensure canvas dimensions match the container
    function resizeCanvas() {
        canvas.width = drawingPad.offsetWidth;
        canvas.height = drawingPad.offsetHeight;
    }
    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);

    // Freehand Drawing
    let isDrawing = false;
    let startX = 0, startY = 0;

    canvas.addEventListener('mousedown', (e) => {
        if (e.button === 0) { // Left mouse button
            isDrawing = true;

            // Get scaling factors
            const rect = canvas.getBoundingClientRect();
            const scaleX = canvas.width / rect.width;
            const scaleY = canvas.height / rect.height;

            // Adjust coordinates for scaling
            startX = (e.clientX - rect.left) * scaleX;
            startY = (e.clientY - rect.top) * scaleY;
        }
    });

    canvas.addEventListener('mousemove', (e) => {
        if (isDrawing) {
            // Get scaling factors
            const rect = canvas.getBoundingClientRect();
            const scaleX = canvas.width / rect.width;
            const scaleY = canvas.height / rect.height;

            // Adjust coordinates for scaling
            const currentX = (e.clientX - rect.left) * scaleX;
            const currentY = (e.clientY - rect.top) * scaleY;

            ctx.beginPath();
            ctx.moveTo(startX, startY);
            ctx.lineTo(currentX, currentY);
            ctx.strokeStyle = 'black';
            ctx.lineWidth = 2;
            ctx.stroke();
            ctx.closePath();

            startX = currentX;
            startY = currentY;
        }
    });


    canvas.addEventListener('mouseup', () => isDrawing = false);
    canvas.addEventListener('mouseleave', () => isDrawing = false);

    // Right-Click to Add Text Box
    canvas.addEventListener('contextmenu', (e) => {
        e.preventDefault();
        const input = document.createElement('textarea');
        input.style.position = 'absolute';
        input.style.top = `${e.offsetY}px`;
        input.style.left = `${e.offsetX}px`;
        input.style.resize = 'none';
        input.style.border = '1px solid #333';
        input.style.background = 'white';
        input.style.padding = '5px';
        drawingPad.appendChild(input);

        input.focus();
        input.addEventListener('blur', () => {
            input.style.pointerEvents = 'none'; // Prevent accidental editing
        });
    });

    // Scroll Click and Drag to Move Around
    let isPanning = false;
    let startPanX = 0, startPanY = 0;

    drawingPad.addEventListener('mousedown', (e) => {
        if (e.button === 1) { // Middle mouse button
            isPanning = true;
            startPanX = e.clientX;
            startPanY = e.clientY;
            drawingPad.style.cursor = 'grab';
        }
    });

    window.addEventListener('mousemove', (e) => {
        if (isPanning) {
            const dx = e.clientX - startPanX;
            const dy = e.clientY - startPanY;
            drawingPad.scrollBy(-dx, -dy);
            startPanX = e.clientX;
            startPanY = e.clientY;
        }
    });

    window.addEventListener('mouseup', () => {
        isPanning = false;
        drawingPad.style.cursor = 'crosshair';
    });
});

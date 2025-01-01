// This script enables the user to take notes on the right pane of Clue.html

// CURRENTLY IS CLEARED ON ANDWER SUBMISSION



let paths = []; // To store drawing actions
let textBoxes = []; // To store added text boxes
let undoStack = []; // Stack to track actions for undo
let redoStack = []; // Stack to track actions for redo
let currentPath = null;
let isErasing = false; // Track whether eraser is active
let drawingColor = 'black'; // Default drawing color

document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('drawing-canvas');
    const ctx = canvas.getContext('2d');
    const drawingPad = document.getElementById('drawing-pad');
    const colorPicker = document.getElementById('color-picker'); // Get the color picker input

    // Ensure canvas dimensions match the container
    function resizeCanvas() {
        canvas.width = drawingPad.clientWidth;
        canvas.height = drawingPad.clientHeight;
        ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear the canvas
        redrawPaths(); // Redraw saved paths
        redrawTextBoxes(); // Redraw saved text boxes
    }

    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);

    // Freehand Drawing
    let isDrawing = false;
    let startX = 0, startY = 0;

    canvas.addEventListener('mousedown', (e) => {
        if (isErasing) {
            eraseContent(e);
        } else if (e.button === 0) { // Left mouse button for drawing
            isDrawing = true;

            // Get scaling factors
            const rect = canvas.getBoundingClientRect();
            const scaleX = canvas.width / rect.width;
            const scaleY = canvas.height / rect.height;

            // Adjust coordinates for scaling
            startX = (e.clientX - rect.left) * scaleX;
            startY = (e.clientY - rect.top) * scaleY;

            // Start a new path and add the starting point
            currentPath = [{ x: startX, y: startY }];
            paths.push(currentPath); // Add the new path to the `paths` array
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

            // Draw on the canvas
            ctx.beginPath();
            ctx.moveTo(startX, startY);
            ctx.lineTo(currentX, currentY);
            ctx.strokeStyle = drawingColor; // Use the selected drawing color
            ctx.lineWidth = 2;
            ctx.stroke();
            ctx.closePath();

            // Update the current path
            currentPath.push({ x: currentX, y: currentY });

            startX = currentX;
            startY = currentY;
        }
    });

    canvas.addEventListener('mouseup', () => isDrawing = false);
    canvas.addEventListener('mouseleave', () => isDrawing = false);

    // Function to redraw saved paths
    function redrawPaths() {
        ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear the canvas

        for (const path of paths) {
            ctx.beginPath();
            for (let i = 0; i < path.length - 1; i++) {
                ctx.moveTo(path[i].x, path[i].y);
                ctx.lineTo(path[i + 1].x, path[i + 1].y);
            }
            ctx.strokeStyle = drawingColor; // Use the current drawing color
            ctx.lineWidth = 2;
            ctx.stroke();
            ctx.closePath();
        }
    }

    // Function to redraw saved text boxes
    function redrawTextBoxes() {
        textBoxes.forEach((box) => {
            const input = document.createElement('textarea');
            input.style.position = 'absolute';
            input.style.top = `${box.y}px`;
            input.style.left = `${box.x}px`;
            input.style.resize = 'none';
            input.style.border = '1px solid #333';
            input.style.background = 'white';
            input.style.padding = '5px';
            input.value = box.text;

            drawingPad.appendChild(input);

            // Handle blur event for textboxes
            input.addEventListener('blur', () => {
                input.style.pointerEvents = 'none'; // Prevent accidental editing
            });
        });
    }

    // Right-Click to Add Text Box
    canvas.addEventListener('contextmenu', (e) => {
        e.preventDefault();
        if (!isErasing) { // Only add text boxes when not erasing
            const input = document.createElement('textarea');
            input.style.position = 'absolute';
            input.style.top = `${e.offsetY}px`;
            input.style.left = `${e.offsetX}px`;
            input.style.resize = 'none';
            input.style.border = '1px solid #333';
            input.style.background = 'white';
            input.style.padding = '5px';
            drawingPad.appendChild(input);

            // Save the position and content of the textbox
            textBoxes.push({
                x: e.offsetX,
                y: e.offsetY,
                text: input.value
            });

            input.focus();
            input.addEventListener('blur', () => {
                input.style.pointerEvents = 'none'; // Prevent accidental editing
            });
        }
    });

    // Function to erase content (both textboxes and paths)
    function eraseContent(e) {
        const rect = canvas.getBoundingClientRect();
        const scaleX = canvas.width / rect.width;
        const scaleY = canvas.height / rect.height;

        const x = (e.clientX - rect.left) * scaleX;
        const y = (e.clientY - rect.top) * scaleY;

        // Erase drawing paths
        paths = paths.filter((path) => {
            return !path.some((point) => {
                return Math.abs(point.x - x) < 10 && Math.abs(point.y - y) < 10; // Erase nearby points
            });
        });

        // Erase text boxes
        textBoxes = textBoxes.filter((box) => {
            return !(Math.abs(box.x - x) < 10 && Math.abs(box.y - y) < 10); // Erase text boxes in range
        });

        redrawPaths();
        redrawTextBoxes();
    }

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

    // "Erase" button click handler
    const eraseButton = document.getElementById('erase-button');
    eraseButton.addEventListener('click', () => {
        isErasing = !isErasing; // Toggle erasing mode
        eraseButton.style.backgroundColor = isErasing ? '#ff0000' : ''; // Optional: change button color
    });

    // "Clear" button click handler
    const clearButton = document.getElementById('clear-button');
    clearButton.addEventListener('click', () => {
        paths = [];
        textBoxes = [];
        ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear the canvas
    });

    // "Undo" button click handler
    const undoButton = document.getElementById('undo-button');
    undoButton.addEventListener('click', () => {
        if (paths.length > 0 || textBoxes.length > 0) {
            undoStack.push({ paths: [...paths], textBoxes: [...textBoxes] }); // Save current state to undo stack
            redoStack = []; // Clear redo stack
            if (paths.length > 0) paths.pop(); // Remove last drawing path
            if (textBoxes.length > 0) textBoxes.pop(); // Remove last text box
            redrawPaths();
            redrawTextBoxes();
        }
    });

    // "Redo" button click handler
    const redoButton = document.getElementById('redo-button');
    redoButton.addEventListener('click', () => {
        if (redoStack.length > 0) {
            const redoState = redoStack.pop(); // Get last undone state
            undoStack.push({ paths: [...paths], textBoxes: [...textBoxes] }); // Save current state to undo stack
            paths = [...redoState.paths]; // Restore paths
            textBoxes = [...redoState.textBoxes]; // Restore text boxes
            redrawPaths();
            redrawTextBoxes();
        }
    });

    // Color Picker change handler
    colorPicker.addEventListener('input', (e) => {
        drawingColor = e.target.value; // Set the drawing color to the selected color
    });


    // Retrieve canvas and drawing pad elements

    // Helper function to save notepad data
    function saveNotepadData() {
        const data = {
            paths: paths, // Save drawn paths
            textBoxes: textBoxes, // Save text boxes
            resizerPosition: {
                width: drawingPad.style.width || '100%', // Save resizer width
                height: drawingPad.style.height || '100%' // Save resizer height
            }
        };
        localStorage.setItem('notepadData', JSON.stringify(data));
    }

    // Helper function to load notepad data
    function loadNotepadData() {
        const data = localStorage.getItem('notepadData');
        if (data) {
            const parsedData = JSON.parse(data);

            // Restore paths
            if (parsedData.paths) {
                paths = parsedData.paths;
                redrawPaths();
            }

            // Restore text boxes
            if (parsedData.textBoxes) {
                textBoxes = parsedData.textBoxes;
                redrawTextBoxes();
            }

            // Restore resizer position
            if (parsedData.resizerPosition) {
                drawingPad.style.width = parsedData.resizerPosition.width;
                drawingPad.style.height = parsedData.resizerPosition.height;
            }
        }
    }

    // Save data on form submission
    const form = document.querySelector('form'); // Adjust selector to match your form
    if (form) {
        form.addEventListener('submit', () => {
            saveNotepadData(); // Save notepad data before form submission
        });
    }

    // Load data on page load
    loadNotepadData();

    // Save data on navigation
    window.addEventListener('beforeunload', () => {
        saveNotepadData(); // Save notepad data before navigating away
    });

    // Existing event listeners for drawing, text boxes, undo, redo, etc.
    // No changes needed, they will work seamlessly with the data restoration
});

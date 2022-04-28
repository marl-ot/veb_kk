// var img = new Image();
// img.src = "/static/main/img/map-1.png";
// console.log(ctx.drawImage(img, 10, 10, 80, 150));

var isMouseDown = false;
var canvas = document.createElement('canvas');
var body = document.getElementsByTagName("main")[0];
var ctx = canvas.getContext('2d');
var linesArray = [];
currentSize = 1;
var currentColor = "rgb(0,0,0)";
let cameraOffset = { x: window.innerWidth / 2, y: window.innerHeight / 2 }
let cameraZoom = 1
let MAX_ZOOM = 5
let MIN_ZOOM = 0.1
let SCROLL_SENSITIVITY = 0.0005
ctx.translate(window.innerWidth / 2, window.innerHeight / 2)
ctx.scale(cameraZoom, cameraZoom)
ctx.translate(-window.innerWidth / 2 + cameraOffset.x, -window.innerHeight / 2 + cameraOffset.y)
ctx.clearRect(0, 0, window.innerWidth, window.innerHeight)

//ZOOM

function getEventLocation(e) {
    if (e.touches && e.touches.length == 1) {
        return { x: e.touches[0].clientX, y: e.touches[0].clientY }
    } else if (e.clientX && e.clientY) {
        return { x: e.clientX, y: e.clientY }
    }
}


let isDragging = false
let dragStart = { x: 0, y: 0 }

function onPointerDown(e) {
    isDragging = true
    dragStart.x = getEventLocation(e).x / cameraZoom - cameraOffset.x
    dragStart.y = getEventLocation(e).y / cameraZoom - cameraOffset.y
}

function onPointerUp(e) {
    isDragging = false
    initialPinchDistance = null
    lastZoom = cameraZoom
}

function onPointerMove(e) {
    if (isDragging) {
        cameraOffset.x = getEventLocation(e).x / cameraZoom - dragStart.x
        cameraOffset.y = getEventLocation(e).y / cameraZoom - dragStart.y
    }
}

function handleTouch(e, singleTouchHandler) {
    if (e.touches.length == 1) {
        singleTouchHandler(e)
    } else if (e.type == "touchmove" && e.touches.length == 2) {
        isDragging = false
        handlePinch(e)
    }
}

let initialPinchDistance = null
let lastZoom = cameraZoom

function handlePinch(e) {
    e.preventDefault()

    let touch1 = { x: e.touches[0].clientX, y: e.touches[0].clientY }
    let touch2 = { x: e.touches[1].clientX, y: e.touches[1].clientY }

    // This is distance squared, but no need for an expensive sqrt as it's only used in ratio
    let currentDistance = (touch1.x - touch2.x) ** 2 + (touch1.y - touch2.y) ** 2

    if (initialPinchDistance == null) {
        initialPinchDistance = currentDistance
    } else {
        adjustZoom(null, currentDistance / initialPinchDistance)
    }
}

function adjustZoom(zoomAmount, zoomFactor) {
    if (!isDragging) {
        if (zoomAmount) {
            cameraZoom += zoomAmount
        } else if (zoomFactor) {
            console.log(zoomFactor)
            cameraZoom = zoomFactor * lastZoom
        }

        cameraZoom = Math.min(cameraZoom, MAX_ZOOM)
        cameraZoom = Math.max(cameraZoom, MIN_ZOOM)

        console.log(zoomAmount)
    }
}

canvas.addEventListener('mousedown', onPointerDown)
canvas.addEventListener('touchstart', (e) => handleTouch(e, onPointerDown))
canvas.addEventListener('mouseup', onPointerUp)
canvas.addEventListener('touchend', (e) => handleTouch(e, onPointerUp))
canvas.addEventListener('mousemove', onPointerMove)
canvas.addEventListener('touchmove', (e) => handleTouch(e, onPointerMove))
canvas.addEventListener('wheel', (e) => adjustZoom(e.deltaY * SCROLL_SENSITIVITY))

// INITIAL LAUNCH

createCanvas();

// BUTTON EVENT HANDLERS

document.getElementById('canvasUpdate').addEventListener('click', function() {
    createCanvas();
    redraw();
});
document.getElementById('colorpicker').addEventListener('change', function() {
    currentColor = this.value;
});
// document.getElementById('bgcolorpicker').addEventListener('change', function() {
//     ctx.fillStyle = this.value;
//     ctx.fillRect(0, 0, canvas.width, canvas.height);
//     redraw();
//     currentBg = ctx.fillStyle;
// });


document.getElementById('controlSize').addEventListener('change', function() {
    currentSize = this.value;
    document.getElementById("showSize").innerHTML = this.value;
});
document.getElementById('saveToImage').addEventListener('click', function() {
    downloadCanvas(this, 'canvas', 'masterpiece.png');
}, false);
document.getElementById('eraser').addEventListener('click', eraser);
document.getElementById('clear').addEventListener('click', createCanvas);
document.getElementById('save').addEventListener('click', save);
document.getElementById('load').addEventListener('click', load);
document.getElementById('clearCache').addEventListener('click', function() {
    localStorage.removeItem("savedCanvas");
    linesArray = [];
    console.log("Cache cleared!");
});

// REDRAW

function redraw() {
    for (var i = 1; i < linesArray.length; i++) {
        ctx.beginPath();
        ctx.moveTo(linesArray[i - 1].x, linesArray[i - 1].y);
        ctx.lineWidth = linesArray[i].size;
        ctx.lineCap = "round";
        ctx.strokeStyle = linesArray[i].color;
        ctx.lineTo(linesArray[i].x, linesArray[i].y);
        ctx.stroke();
    }
}

// DRAWING EVENT HANDLERS

canvas.addEventListener('mousedown', function() { mousedown(canvas, event); });
canvas.addEventListener('mousemove', function() { mousemove(canvas, event); });
canvas.addEventListener('mouseup', mouseup);

// CREATE CANVAS

function createCanvas() {
    var img = new Image();
    img.src = '/static/main/img/test-map-1.png';
    canvas.id = "canvas";
    canvas.width = img.width;
    canvas.height = img.height;
    canvas.style.zIndex = 8;
    canvas.style.position = "absolute";
    canvas.style.border = "1px solid";
    img.onload = function() {
        ctx.drawImage(img, 0, 0);
    }
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    body.appendChild(canvas);
}

// DOWNLOAD CANVAS

function downloadCanvas(link, canvas, filename) {
    link.href = document.getElementById(canvas).toDataURL();
    link.download = filename;
}

// SAVE FUNCTION

function save() {
    localStorage.removeItem("savedCanvas");
    localStorage.setItem("savedCanvas", JSON.stringify(linesArray));
    alert("Saved canvas!");
}

// LOAD FUNCTION

function load() {
    if (localStorage.getItem("savedCanvas") != null) {
        linesArray = JSON.parse(localStorage.savedCanvas);
        var lines = JSON.parse(localStorage.getItem("savedCanvas"));
        for (var i = 1; i < lines.length; i++) {
            ctx.beginPath();
            ctx.moveTo(linesArray[i - 1].x, linesArray[i - 1].y);
            ctx.lineWidth = linesArray[i].size;
            ctx.lineCap = "round";
            ctx.strokeStyle = linesArray[i].color;
            ctx.lineTo(linesArray[i].x, linesArray[i].y);
            ctx.stroke();
        }
        console.log("Canvas loaded.");
    } else {
        console.log("No canvas in memory!");
    }
}

// ERASER HANDLING

function eraser() {
    currentSize = 50;
    currentColor = ctx.fillStyle
}

// GET MOUSE POSITION

function getMousePos(canvas, evt) {
    var rect = canvas.getBoundingClientRect();
    return {
        x: evt.clientX - rect.left,
        y: evt.clientY - rect.top
    };
}

// ON MOUSE DOWN

function mousedown(canvas, evt) {
    var mousePos = getMousePos(canvas, evt);
    isMouseDown = true
    var currentPosition = getMousePos(canvas, evt);
    ctx.moveTo(currentPosition.x, currentPosition.y)
    ctx.beginPath();
    ctx.lineWidth = currentSize;
    ctx.lineCap = "round";
    ctx.strokeStyle = currentColor;

}

// ON MOUSE MOVE

function mousemove(canvas, evt) {

    if (isMouseDown) {
        var currentPosition = getMousePos(canvas, evt);
        ctx.lineTo(currentPosition.x, currentPosition.y)
        ctx.stroke();
        store(currentPosition.x, currentPosition.y, currentSize, currentColor);
    }
}

// STORE DATA

function store(x, y, s, c) {
    var line = {
        "x": x,
        "y": y,
        "size": s,
        "color": c
    }
    linesArray.push(line);
}

// ON MOUSE UP

function mouseup() {
    isMouseDown = false
    store()
}
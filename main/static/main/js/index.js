// const canvas = document.getElementById('drawing-board');
// const toolbar = document.getElementById('toolbar');
// const ctx = canvas.getContext('2d');

// const canvasOffsetX = canvas.offsetLeft;
// const canvasOffsetY = canvas.offsetTop;

// canvas.width = window.innerWidth - canvasOffsetX;
// canvas.height = window.innerHeight - canvasOffsetY;

// let isPainting = false;
// let lineWidth = 5;
// let drawing = false
// var mouse = { x: 0, y: 0, color: 0 };
// var previous = { x: 0, y: 0, color: 0 };
// let points = [];
// let pathsry = [];
// let colorsry = "#000000";
// ctx.strokeStyle = "#000000";
// let draw_list = [];
// let planexy = { x: 0, y: 0 };

// var img = new Image();
// img.src = 'test-map.png';
// img.onload = function() {

//     var pattern = context.createPattern(img, "repeat");
//     context.fillStyle = pattern;
//     context.fillRect(10, 10, 150, 150);
//     context.strokeRect(10, 10, 150, 150);
// };

// toolbar.addEventListener('click', e => {
//     if (e.target.id === 'clear') {
//         ctx.clearRect(0, 0, canvas.width, canvas.height);
//     }
// });


// toolbar.addEventListener('click', e => {
//     if (e.target.id === 'plane') {
//         canvas.addEventListener('click', function(e) {
//             drawing = false;
//             mouse = oMousePos(canvas, e);
//             planexy = { x: mouse.x, y: mouse.y };
//             var img = new Image();
//             img.src = 'plane-icon.svg';
//             ctx.drawImage(img, planexy.x, planexy.y);
//             canvas.removeEventListener('click');

//         })


//     }
// });



// toolbar.addEventListener('change', e => {
//     if (e.target.id === 'stroke') {
//         ctx.strokeStyle = e.target.value;
//         colorsry = e.target.value;
//     }

//     if (e.target.id === 'lineWidth') {
//         lineWidth = e.target.value;
//     }

// });
// canvas.addEventListener('mousedown', function(e) {
//     drawing = true;
//     previous = { x: mouse.x, y: mouse.y };
//     mouse = oMousePos(canvas, e);
//     points = [];
//     points.push({ x: mouse.x, y: mouse.y })
// });

// canvas.addEventListener('mousemove', function(e) {
//     if (drawing) {
//         ctx.lineWidth = lineWidth;
//         ctx.lineCap = 'round';
//         previous = { x: mouse.x, y: mouse.y };
//         mouse = oMousePos(canvas, e);
//         points.push({ x: mouse.x, y: mouse.y, color: colorsry })
//         ctx.beginPath();
//         ctx.moveTo(previous.x, previous.y);
//         ctx.lineTo(mouse.x, mouse.y);
//         ctx.stroke();
//     }
// }, false);


// canvas.addEventListener('mouseup', function() {
//     drawing = false;
//     pathsry.push(points);

// }, false);


// undo.addEventListener("click", Undo);

// function drawPaths() {
//     ctx.clearRect(0, 0, canvas.width, canvas.height);
//     pathsry.forEach(path => {
//         ctx.beginPath();
//         ctx.moveTo(path[0].x, path[0].y);
//         for (let i = 1; i < path.length; i++) {
//             ctx.strokeStyle = path[i].color;
//             ctx.lineTo(path[i].x, path[i].y);


//         }
//         ctx.stroke();
//     })
// }

// function Undo() {
//     pathsry.splice(-1, 1);
//     drawPaths();
// }


// function oMousePos(canvas, evt) {
//     var ClientRect = canvas.getBoundingClientRect();
//     return {
//         x: Math.round(evt.clientX - ClientRect.left),
//         y: Math.round(evt.clientY - ClientRect.top)
//     }
// }
// console.log(planexy)
var img = new Image();
img.src = "main/static/main/img/test-map.png";

var isMouseDown = false;
var canvas = document.createElement('canvas');
var body = document.getElementsByTagName("main")[0];
var ctx = canvas.getContext('2d');
var linesArray = [];
currentSize = 1;
var currentColor = "rgb(200,20,100)";
var currentBg = img;

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
    canvas.id = "canvas";
    canvas.width = parseInt(document.getElementById("sizeX").value);
    canvas.height = parseInt(document.getElementById("sizeY").value);
    canvas.style.zIndex = 8;
    canvas.style.position = "absolute";
    canvas.style.border = "1px solid";
    ctx.fillStyle = currentBg;
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
    console.log("Saved canvas!");
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
const canvas = document.getElementById('drawing-board');
const toolbar = document.getElementById('toolbar');
const ctx = canvas.getContext('2d');

const canvasOffsetX = canvas.offsetLeft;
const canvasOffsetY = canvas.offsetTop;

canvas.width = window.innerWidth - canvasOffsetX;
canvas.height = window.innerHeight - canvasOffsetY;

let isPainting = false;
let lineWidth = 5;
let drawing = false
var mouse ={x:0, y:0, color:0};
var previous = {x:0, y:0, color:0};
let points = [];
let pathsry = [];
let colorsry = "#000000";
ctx.strokeStyle = "#000000";
let draw_list = [];
let planexy = {x:0, y:0};

toolbar.addEventListener('click', e => {
    if (e.target.id === 'clear') {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
    }
});


toolbar.addEventListener('click', e => {
  if (e.target.id === 'plane') {
      canvas.addEventListener('click', function(e){
        drawing = false;
        mouse = oMousePos(canvas,e);
        planexy = {x:mouse.x,y:mouse.y};
        var img = new Image();
        img.src = 'plane-icon.svg';
        ctx.drawImage(img, planexy.x, planexy.y);
      canvas.removeEventListener('click');
        
      }
      )
      

  }
});



toolbar.addEventListener('change', e => {
    if(e.target.id === 'stroke') {
        ctx.strokeStyle = e.target.value;
        colorsry = e.target.value;
    }

    if(e.target.id === 'lineWidth') {
        lineWidth = e.target.value;
    }
    
});
canvas.addEventListener('mousedown', function(e) {
    drawing = true; 
    previous = {x:mouse.x,y:mouse.y};
    mouse = oMousePos(canvas, e);
    points = [];
    points.push({x:mouse.x,y:mouse.y})
    });
    
    canvas.addEventListener('mousemove', function(e) {
    if(drawing){
    ctx.lineWidth = lineWidth;
    ctx.lineCap = 'round';
    previous = {x:mouse.x,y:mouse.y};
    mouse = oMousePos(canvas, e);
    points.push({x:mouse.x,y:mouse.y, color:colorsry})
    ctx.beginPath();
    ctx.moveTo(previous.x,previous.y);
    ctx.lineTo(mouse.x,mouse.y);
    ctx.stroke();
    }
    }, false);
    
    
    canvas.addEventListener('mouseup', function() {
    drawing=false;
    pathsry.push(points);
    
    }, false);
    
    
    undo.addEventListener("click",Undo);
    
    function drawPaths(){
      ctx.clearRect(0,0,canvas.width,canvas.height);
      pathsry.forEach(path=>{
      ctx.beginPath();
      ctx.moveTo(path[0].x,path[0].y);  
      for(let i = 1; i < path.length; i++){
        ctx.strokeStyle = path[i].color;
        ctx.lineTo(path[i].x,path[i].y);
        
        
      }
        ctx.stroke();
      })
    }  
    
    function Undo(){
      pathsry.splice(-1,1);
      drawPaths();
    }
    

    function oMousePos(canvas, evt) {
      var ClientRect = canvas.getBoundingClientRect();
        return { 
        x: Math.round(evt.clientX - ClientRect.left),
        y: Math.round(evt.clientY - ClientRect.top)
    }
    }
console.log(planexy)
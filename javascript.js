let canvas;
let canvasContext;
let ballX = 50;
window.onload = function() {
    canvas = document.getElementById('gameCanvas');
    canvasContext = canvas.getContext('2d');
    const framePerSecond = 30;
    setInterval(drawEverything, 1000/framePerSecond);
};
function drawEverything() {
    ballX = ballX + 10;
    console.log(ballX);
    canvasContext.fillStyle = 'black';
    canvasContext.fillRect(0, 0, canvas.width, canvas.height);
    canvasContext.fillStyle = 'white';
    canvasContext.fillRect(20, 100, 30, 150);
    canvasContext.fillStyle = 'red';
    canvasContext.fillRect(ballX, 100, 30,30);
}
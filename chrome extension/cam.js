	// Grab elements, create settings, etc.
var video = document.getElementById('video');
canvas = document.getElementById('canvas');

//response = $.get('http://localhost:80/')
//console.log(response)
// Get access to the camera!
if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    // Not adding `{ audio: true }` since we only want video now
    navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
        //video.src = window.URL.createObjectURL(stream);
        video.srcObject = stream;
        video.play();
    });
}
var context = canvas.getContext('2d');
window.setInterval(function(){  
var dataURL = canvas.toDataURL('image/jpeg', 1.0); 
dataURL = dataURL.split(',')[1]

console.log(dataURL)
$.ajax({
  type: "POST",
  url: "http://localhost:80/",
  data: dataURL
}).done(function(o) {
});
},100);

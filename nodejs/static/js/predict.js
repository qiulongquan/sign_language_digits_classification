const CLASSES = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four',5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}

//-----------------------
// start button event
//-----------------------

$("#start-button").click(function(){
	console.log("qiulongquan model load");
	loadModel();
	startWebcam();
});

//-----------------------
// load model
//-----------------------
// 注意这个地方 新版本已经更新了方法名字loadLayersModel，以前的loadModel在老版本还可以使用，新版本已经不使用了
// tf.loadLayersModel

let model;
async function loadModel() {
	console.log("model loading..");
	$("#console").html(`<li>model loading...</li>`);

	model=await tf.loadLayersModel(`http://localhost:8080/sign_language_vgg16/model.json`);
	console.log("model loaded.");
	$("#console").html(`<li>VGG16 pre trained model loaded.</li>`);
};

//-----------------------
// start webcam 
//-----------------------

var video;
function startWebcam() {
	console.log("qiulongquan video streaming start.");
	$("#console").html(`<li>video streaming start.</li>`);
	video = $('#main-stream-video').get(0);
	vendorUrl = window.URL || window.webkitURL;

	navigator.getMedia = navigator.getUserMedia ||
						 navigator.webkitGetUserMedia ||
						 navigator.mozGetUserMedia ||
						 navigator.msGetUserMedia;

	navigator.getMedia({
		video: true,
		audio: false
	}, function(stream) {
		localStream = stream;
		video.srcObject = stream;
		video.play();
	}, function(error) {
		alert("Something wrong with webcam!");
	});
}

//-----------------------
// predict button event
//-----------------------

$("#predict-button").click(function(){
	setInterval(predict, 1000/10);
});

//-----------------------
// TensorFlow.js method
// predict tensor
//-----------------------

async function predict(){
	let tensor = captureWebcam();

	// 把图片的tensorflow化后的内容传给model.predict，进行判断
	let prediction = await model.predict(tensor).data();
	let results = Array.from(prediction)
				.map(function(p,i){
	return {
		probability: p,
		className: CLASSES[i]
	};
	}).sort(function(a,b){
		return b.probability-a.probability;
	}).slice(0,5);

	// 这个清空是摄像头下面位置的内容每次清空保证只显示5个结果
	$("#console").empty();

	results.forEach(function(p){
		$("#console").append(`<li>${p.className} : ${p.probability.toFixed(6)}</li>`);
		// 这个是F12进入控制台的显示内容
		console.log("qiulongquan控制台显示内容：",p.className,p.probability.toFixed(6))
	});

};

//------------------------------
// capture streaming video 
// to a canvas object
//------------------------------

function captureWebcam() {
	var canvas    = document.createElement("canvas");
	var context   = canvas.getContext('2d');
	canvas.width  = video.width;
	canvas.height = video.height;

	context.drawImage(video, 0, 0, video.width, video.height);
	tensor_image = preprocessImage(canvas);

	return tensor_image;
}

//-----------------------
// TensorFlow.js method
// image to tensor
//-----------------------

// You are looking at the documentation for version 0.12.0.
// tf.fromPixels was deprecated in version 1.0.0, use: tf.browser.fromPixels()
// 注意 这个地方新版本tensorflowjs方法名有变化tf.browser.fromPixels()，老版本可以继续使用tf.fromPixels这个方法名

function preprocessImage(image){
	let tensor = tf.browser.fromPixels(image).resizeNearestNeighbor([100,100]).toFloat();
	let offset = tf.scalar(255);
    return tensor.div(offset).expandDims();
}

//-----------------------
// clear button event
//-----------------------

$("#clear-button").click(function clear() {
	location.reload();
});
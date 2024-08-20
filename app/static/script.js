function changeCamera() {
    const select = document.getElementById("camera-select");
    const cameraId = select.value;
    const videoFeed = document.getElementById("video-feed");
    videoFeed.src = `/video_feed/${cameraId}`;
}
import cv2
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from threading import Lock

app = FastAPI()

app.mount("/static", StaticFiles(directory="frontend/dist"), name="static")

cameras = {
    "camera_1": cv2.VideoCapture(0),
    "camera_2": cv2.VideoCapture(2)
}
camera_lock = Lock()


def generate_frames(camera):
    while True:
        with camera_lock:
            success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.get("/")
async def serve_frontend():
    return FileResponse('frontend/dist/index.html')


@app.get("/video_feed/{camera_id}")
async def video_feed(camera_id: str):
    camera = cameras.get(camera_id)
    if camera is None:
        return HTMLResponse(status_code=404, content="Camera not found")
    return StreamingResponse(generate_frames(camera), media_type="multipart/x-mixed-replace; boundary=frame")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=4567)

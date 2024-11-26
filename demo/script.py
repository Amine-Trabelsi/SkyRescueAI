import typer
import cv2
from ultralytics import YOLO

def main(
    model_name: str = "yolov11n.pt",
    device: str = "cpu",
    images: str = "images",
    conf: float = 0.25,
    iou: float = 0.6,
    window_size: tuple[int, int] = (1280, 729)
):
    model = YOLO(model_name).to(device)

    for prediction in model.predict(images, stream=True, conf=conf, iou=iou):
        if prediction:
            cv2.imshow("YOLO Inference", cv2.resize(prediction[0].plot(probs=False), window_size))
        else:
            cv2.imshow("YOLO Inference", cv2.resize(prediction.orig_img, window_size))

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    typer.run(main)

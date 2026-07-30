import cv2


def load_image(image_path):
    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(image_path)

    return image


def crop_roi(image, field_config):

    h, w = image.shape[:2]

    roi = field_config["roi"]

    margin = field_config.get("margin", 0)

    y1 = int(roi[0] * h)
    y2 = int(roi[1] * h)

    x1 = int(roi[2] * w)
    x2 = int(roi[3] * w)

    y1 = max(0, y1 - margin)
    x1 = max(0, x1 - margin)

    y2 = min(h, y2 + margin)
    x2 = min(w, x2 + margin)

    return image[y1:y2, x1:x2]
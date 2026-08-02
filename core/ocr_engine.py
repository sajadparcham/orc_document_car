from paddleocr import PaddleOCR
#ورودی
#processed_crop
#language

#خروجی
#raw_text

#confidence

#مثلاً

#text, conf = run_ocr(crop,"fa")


from paddleocr import PaddleOCR


class OCREngine:

    def __init__(self):
        self.engines = {
            "fa": PaddleOCR(
                use_angle_cls=True,
                lang="fa",
                show_log=False
            ),

            "en": PaddleOCR(
                use_angle_cls=True,
                lang="en",
                show_log=False
            )
        }

    def recognize(self, crop, field_config):

        lang = field_config["lang"]

        engine = self.engines[lang]

        result = engine.ocr(crop, cls=True)

        texts = []
        boxes = []
        confidences = []

        if result and result[0]:
            for item in result[0]:
                boxes.append(item[0])
                texts.append(item[1][0])
                confidences.append(item[1][1])

        return {
            "texts": texts,
            "boxes": boxes,
            "confidences": confidences
        }

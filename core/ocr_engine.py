from paddleocr import PaddleOCR
#ورودی
#processed_crop
#language

#خروجی
#raw_text

#confidence

#مثلاً

#text, conf = run_ocr(crop,"fa")



ocr_fa = PaddleOCR(use_angle_cls=True, lang="fa", show_log=False)
ocr_en = PaddleOCR(use_angle_cls=True, lang="en", show_log=False)
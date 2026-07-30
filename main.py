image = load_image(path)

results = {}

for field in CONFIG:

    crop = crop_roi(image)

    crop = preprocess(crop)

    text = run_ocr(crop)

    text = normalize(text)

    text = validate(field, text)

    results[field] = text

save_docx(results)
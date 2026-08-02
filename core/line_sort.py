from collections import defaultdict


def sort_lines(texts, boxes, rtl=True):

    if not texts:
        return ""

    words = []

    for text, box in zip(texts, boxes):

        xs = [p[0] for p in box]
        ys = [p[1] for p in box]

        words.append({

            "text": text,
            "x": sum(xs) / 4,
            "y": sum(ys) / 4,
            "height": max(ys) - min(ys)

        })

    # ارتفاع متوسط کلمات
    avg_height = sum(w["height"] for w in words) / len(words)

    # فاصله مجاز بین سطرها
    threshold = avg_height * 0.7

    # مرتب سازی بر اساس ارتفاع
    words.sort(key=lambda w: w["y"])

    lines = []

    for word in words:

        added = False

        for line in lines:

            if abs(line["y"] - word["y"]) <= threshold:

                line["words"].append(word)

                line["y"] = (
                    line["y"] * (len(line["words"]) - 1)
                    + word["y"]
                ) / len(line["words"])

                added = True
                break

        if not added:

            lines.append({

                "y": word["y"],
                "words": [word]

            })

    output = []

    for line in lines:

        line["words"].sort(
            key=lambda w: w["x"],
            reverse=rtl
        )

        output.append(

            " ".join(
                w["text"] for w in line["words"]
            )

        )

    return "\n".join(output)
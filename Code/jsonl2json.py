import jsonlines
import json

with jsonlines.open(r"", "r") as rfd:
    with open(r"", "w", encoding='utf-8') as wfd:
        for data in rfd:
            json.dump(data, wfd, indent=4, ensure_ascii=False)
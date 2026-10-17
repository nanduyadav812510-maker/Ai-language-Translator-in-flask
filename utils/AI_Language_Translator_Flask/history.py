import json
import os

HISTORY_FILE = "data/data.json"


def save_history(original, translated, source, target):
    history = []

    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            try:
                history = json.load(file)
            except:
                history = []

    history.append({
        "original_text": original,
        "translated_text": translated,
        "source_language": source,
        "target_language": target
    })

    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4, ensure_ascii=False)


def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return []
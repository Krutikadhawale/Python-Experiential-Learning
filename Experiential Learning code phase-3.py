

import urllib.request
import urllib.parse
import json

def translate(sentence):
    url = "https://translate.googleapis.com/translate_a/single"

    params = urllib.parse.urlencode({
        "client": "gtx",
        "sl": "en",
        "tl": "hi",
        "dt": "t",
        "q": sentence
    })

    request = urllib.request.Request(
        url + "?" + params,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    with urllib.request.urlopen(request, timeout=15) as response:
        data = json.loads(response.read().decode("utf-8"))

    hindi = "".join(
        part[0] for part in data[0] if part[0]
    )

    return hindi


print("===== English to Hindi Translator =====")

while True:
    sentence = input("\nEnter English sentence (or exit): ").strip()

    if sentence.lower() == "exit":
        print("Thank you!")
        break

    if not sentence:
        print("Please enter some text.")
        continue

    try:
        print("Hindi Translation:", translate(sentence))

    except Exception as e:
        print("Translation error:", e)
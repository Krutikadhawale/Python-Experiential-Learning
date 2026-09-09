# English to Hindi Translator - Level 2

words = {
    "hello": "नमस्ते",
    "good": "अच्छा",
    "morning": "सुबह",
    "how": "कैसे",
    "are": "हैं",
    "you": "आप",
    "i": "मैं",
    "am": "हूँ",
    "fine": "ठीक",
    "thank": "धन्यवाद",
    "friend": "दोस्त",
    "school": "विद्यालय",
    "student": "विद्यार्थी",
    "book": "किताब",
    "water": "पानी",
    "food": "भोजन",
    "home": "घर",
    "love": "प्यार",
    "happy": "खुश"
}


def translate(sentence):
    sentence = sentence.lower()

    # Remove common punctuation
    for symbol in ".,!?":
        sentence = sentence.replace(symbol, "")

    word_list = sentence.split()
    result = []

    for word in word_list:
        if word in words:
            result.append(words[word])
        else:
            result.append("[" + word + "]")

    return " ".join(result)


try:
    print("===== English to Hindi Translator =====")

    sentence = input("Enter English sentence: ")

    if sentence.strip() == "":
        print("Please enter some text.")
    else:
        hindi = translate(sentence)
        print("Hindi Translation:", hindi)

except Exception:
    print("Something went wrong.")
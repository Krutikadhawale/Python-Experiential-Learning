# English to Hindi Translator

dictionary = {
    "hello": "नमस्ते",
    "good": "अच्छा",
    "morning": "सुबह",
    "water": "पानी",
    "book": "किताब",
    "school": "विद्यालय",
    "student": "विद्यार्थी",
    "friend": "दोस्त",
    "thank": "धन्यवाद"
}

def translate(text):
    words = text.lower().split()
    result = []

    for word in words:
        if word in dictionary:
            result.append(dictionary[word])
        else:
            result.append(word)

    return " ".join(result)


text = input("Enter English sentence: ")

translation = translate(text)

print("Hindi Translation:", translation)
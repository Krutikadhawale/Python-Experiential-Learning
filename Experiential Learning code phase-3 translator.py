
from deep_translator import MyMemoryTranslator

def translate(sentence):
    # 'english' और 'hindi' पूरे नाम के साथ लिखें
    return MyMemoryTranslator(source='english', target='hindi').translate(sentence)

print("===== English to Hindi Translator =====")

while True:
    sentence = input("\nEnter English sentence (or exit): ").strip()
    
    if sentence.lower() == "exit":
        print("Thank you!")
        break
        
    if not sentence:
        print("Please enter a sentence.")
        continue
        
    try:
        print("Hindi Translation:", translate(sentence))
    except Exception as e:
        print("Error:", e)
# Text to Morse Code Converter
# A text-based Python program to convert Strings into Morse Code.
morse_dict = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    " ": "/",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}


def split(word):
    # Splits a string into a list
    return [char for char in word]


text = input("Write a text to convert to morse: ").lower()
text_split = split(text)
morse_list = []
# Change string list into morse list
[morse_list.append(morse_dict[item]) for item in text_split]
# Change morse list to morse string
morse_string = ' '.join([str(item) for item in morse_list])
print(morse_string)

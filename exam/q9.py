def four_letter_words(message):
    words = message.split()
    four_letters = [w for w in words if len(w) == 4]
    return four_letters


message = "The quick brown fox jumps over the lazy dog"
print(four_letter_words(message))
# Output: ["over", "lazy"]

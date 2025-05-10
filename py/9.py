# 10.Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary
# Input: str1 = "Python is great and Java is also great"
# Output: {'Python': 1, 'is': 2, 'great': 2, 'and': 1, 'Java': 1, 'also': 1}

from typing import Dict


def count_word_frequency(s: str) -> Dict[str, int]:
    words = s.split()
    word_freq: Dict[str, int] = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq


s = "Python is great and Java is also great"
word_freq = count_word_frequency(s)
print(word_freq)
# Output: {'Python': 1, 'is': 2, 'great': 2, 'and': 1, 'Java': 1, 'also': 1}

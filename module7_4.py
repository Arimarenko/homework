from typing import Dict, List


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
        self.all_words = self.get_all_words()

    def get_all_words(self) -> Dict[str, List[str]]:
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r') as file:
                text = file.read().lower().split()
                text = [word.strip('.,:=!?;\'\"') for word in text]
                all_words[file_name] = text
        return all_words

    def find(self, word: str) -> Dict[str, int]:
        result = {}
        for file_name, words in self.all_words.items():
            if word in words:
                index = words.index(word)
                result[file_name] = index
        return result

    def count(self, word: str) -> Dict[str, int]:
        result = {}
        for file_name, words in self.all_words.items():
            count = words.count(word)
            result[file_name] = count
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))

class Solution(object):
    def toGoatLatin(self, sentence):

        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        
        words = sentence.split()
        
        goat_latin_words = []
        for i, word in enumerate(words):
            if word[0] in vowels:
                goat_word = word + "ma"
            else:
                goat_word = word[1:] + word[0] + "ma"
            
            
            goat_word += 'a' * (i + 1)
            
            goat_latin_words.append(goat_word)
        

        return " ".join(goat_latin_words)

solution = Solution()
sentence1 = "I speak Goat Latin"
sentence2 = "The quick brown fox jumped over the lazy dog"

print(solution.toGoatLatin(sentence1))
print(solution.toGoatLatin(sentence2))


class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        words = sentence.split()
        for i, word in enumerate(words):
            for root in sorted(dictionary, key=len):
                if word.startswith(root):
                    words[i] = root
                    break
        return ' '.join(words)

        

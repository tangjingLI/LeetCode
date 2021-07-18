# @Author ltj
# @Time   2021/7/18 19:04
# @File   replaceWords.py


class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """

        dictionary = sorted(dictionary, key=lambda i: len(i), reverse=False)
        print(dictionary)
        words = sentence.split(' ')
        print(words)

        for i, word in enumerate(words):
            for root in dictionary:
                if word.startswith(root):
                    words[i] = root
                    break

        return " ".join(words)


dictionary = ["catt", "cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
print(Solution().replaceWords(dictionary, sentence))

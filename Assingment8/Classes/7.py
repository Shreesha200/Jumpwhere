class StringReverser:
    def reverse_words(self, s):
        return ' '.join(s.split()[::-1])

def is_palindrme(s):
    return s== s[:: -1]

def count_words(text):
    return len(text.split())

    def factorial(n):
        if n<0:
            return None
        result = 1
        for i in range(1, n+1):
            result *=i
            return result
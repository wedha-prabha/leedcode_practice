def reverseWords(s):
    words = s.split()
    return " ".join(words[::-1])

# Example
s = "the sky is blue"
print(reverseWords(s))
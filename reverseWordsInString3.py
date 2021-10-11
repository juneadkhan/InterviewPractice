"""
Given a string s, reverse the order of characters in each word within a sentence
while still preserving whitespace and initial word order.

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

"""

# O(n) Time, O(n) Space
def reverseWords(s: str) -> str:
    out = []
    for count, value in enumerate(s.split()):
        out.append(value[::-1])
    return ' '.join(out)


# O(n) Time, O(n) Space
def reverseWords(s: str) -> str:
    return " ".join([i[::-1] for i in s.split()])
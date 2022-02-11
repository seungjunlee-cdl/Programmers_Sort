Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def solution(citations):
    citations.sort(reverse=True)
    for idx , citation in enumerate(citations):
        print(idx,citation)
        if idx >= citation:
            return idx
    return len(citations)
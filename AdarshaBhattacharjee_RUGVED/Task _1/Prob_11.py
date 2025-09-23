def coleman_liau_index(text):
    letters = sum(c.isalpha() for c in text)
    words = len(text.split())
    sentences = sum(text.count(end) for end in ['.', '!', '?'])


    L = (letters / words) * 100
    S = (sentences / words) * 100
    index = 0.0588 * L - 0.296 * S - 15.8
    return round(index)


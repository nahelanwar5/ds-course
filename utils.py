def safe_int(s):
    '''Clean an integer having commas and convert its type to int. Return None for types like "abc" which cannot be converted'''
    try:
        s = s.replace(",", "")
        return int(s)
    except ValueError:
        return None

def safe_float(s):
    '''Convert any item to a float. Return None for types like "abc" which cannot be converted'''
    try:
        return float(s)
    except ValueError:
        return None


def safe_divide(a, b):
    '''Perform division and return None in case denominator is 0'''
    try:
        return a / b
    except ZeroDivisionError:
        return None


def group_sum(pairs):
    '''Create a dictionary of grouped sums--values or repeating items are added'''
    totals = {}
    for key, amount in pairs:
        totals[key] = totals.get(key, 0) + amount
    return totals


def filter_over(dic, threshold=500):
    '''Keep items from a dictionary whose values meet a certain condition (only numerical)'''
    return {key: value for key, value in dic.items() if value >= threshold}

def count_words(text):
    '''Create a dictionary of word counts in a given text'''
    counts={}
    word_list= text.split()
    for word in word_list:
        counts[word]= counts.get(word, 0)+1
    return counts

def most_common_word(text):
    '''Return the word with maximum word count in a text, using the above word count dictionary'''
    counts= count_words(text)
    maxim= max(counts, key=counts.get)
    return maxim

def grades(score):  
    try:
        if score > 100 or score < 0:
            raise ValueError(score)
        if score>=80:
            return "A"
        if score>=65:
            return "B"
        if score>=50:
            return "C"
        return "F"
    except ValueError as e:
        return f"{e} is >100"
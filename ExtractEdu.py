import regex as re
from nltk.tokenize import word_tokenize

edu_key = [
            'BE','B.E.', 'B.E', 'BS', 'B.SC', 
            'ME', 'M.E', 'M.E.', 'MS', 'M.SC', 
            'B.COM', 'B. TECH', 'M.TECH', 'MTECH',
            'PH.D', 'M.COM', 'BA', 'ICSE', 'X', 'XII', 
            'SSC', 'HSC', 'CBSE', 'SECONDARY'
        ]

def extract_marks(i, l2):
    for ele in range(i, len(l2)):
        if re.match(rf'\d+\.\d+', l2[ele]):
            return l2[ele]
        if l2[ele] in edu_key:
            return None

def extract(education):
    edu = {}
    l1 = word_tokenize(' '.join(education))
    l2 = [x for x in l1 if x != ',' if x!= '%' if x != '(' if x != ')' if x != '&' if x != '.']
    for i in range(0, len(l2)):
        for j in range(0, len(edu_key)):
            if re.match(rf'(?=.*\b{edu_key[j]}\b)', l2[i]):
                temp = edu_key[j]
                marks = extract_marks(i+1, l2)
                edu[temp] = marks
    return edu
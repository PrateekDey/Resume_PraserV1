import pandas as pd
from nltk.tokenize import word_tokenize

skill_df = pd.read_csv(r"C:\Users\Win10\Documents\ML\Parser V1\model\skillset.csv")
skill_df = skill_df.applymap(lambda s:s.upper() if type(s) == str else s)

def extract_skill(txt):
    l1 = word_tokenize(' '.join(txt))
    l2 = [x for x in l1 if x != ',' if x!= '%' if x != '(' if x != ')' if x != '&' if x != '.' if x!= ':']
    skill_set = []
    for i in range(0, len(l2)):
        if l2[i] in skill_df.values:
            #print(l2[i])
            skill_set.append(l2[i])

    return skill_set
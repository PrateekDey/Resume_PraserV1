from tika import parser
import pandas


def clean_resume(raw_data):
    df = raw_data['content'].upper().splitlines()
    df2 = [x.strip() for x in df]
    df3 = [x for x in df2 if x != '']
    return df3


def getfile(filename):
    raw_data = parser.from_file(filename)
    cdf = clean_resume(raw_data)
    return cdf


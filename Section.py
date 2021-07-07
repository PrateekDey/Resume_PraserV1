import CleanData as cd
import Match
import ExtractEdu as ee
import Skills

info = {}


def formdict(key, line_num, cdf):
    key = Match.extract_key(key)
    s = []
    while line_num < len(cdf):
        if Match.match_line(cdf[line_num]):
            info[key] = s
            break
        else:
            s.append(cdf[line_num])
            line_num = line_num + 1
    return line_num


def division(cdf):
    for i in range(0, len(cdf)):
        if Match.match_line(cdf[i]):
            i = formdict(cdf[i], i+1, cdf)

    return info

import regex as re


def match_line(line):
    if re.match(r'(?=.*\bOBJECTIVE\b)', line):
        return True
    if re.match(r'(?=.*\bSUMMARY\b)', line):
        return True
    if re.match(r'(?=.*\bRESEARCH\b)', line):
        return True
    if re.match(r'(?=.*\bEDUCATION\b)', line):
        return True
    if re.match(r'(?=.*\bINTEREST\b)', line):
        return True
    if re.match(r'(?=.*\bINDUSTRY\b)', line):
        return True
    if re.match(r'(?=.*\bDEVELOPMENT\b)', line):
        return True
    if re.match(r'(?=.*\bSKILL\b)', line):
        return True
    if re.match(r'(?=.*\bPROJECT\b)', line):
        return True
    if re.match(r'(?=.*\bPROFILE\b)', line):
        return True
    if re.match(r'(?=.*\bAWARD\b)', line):
        return True
    if re.match(r'(?=.*\bEXPERIENCE\b)', line):
        return True
    if re.match(r'(?=.*\bPUBLICATION\b)', line):
        return True
    if re.match(r'(?=.*\bPROFESSIONAL\b)', line):
        return True
    if re.match(r'(?=.*\bCONFERENCE\b)', line):
        return True
    if re.match(r'(?=.*\bFEST\b)', line):
        return True
    if re.match(r'(?=.*\bEXAM\b)', line):
        return True
    if re.match(r'(?=.*\bCULTURAL\b)', line):
        return True
    if re.match(r'(?=.*\bEXTRA\b)', line):
        return True
    if re.match(r'(?=.*\bPERSONAL\b)', line):
        return True
    if re.match(r'(?=.*\bREFERENCE\b)', line):
        return True
    if re.match(r'(?=.*\bDECLARATION\b)', line):
        return True


def extract_key(line):
    if re.match(r'(?=.*\bOBJECTIVE\b)', line):
        return "OBJECTIVE"
    if re.match(r'(?=.*\bSUMMARY\b)', line):
        return "SUMMARY"
    if re.match(r'(?=.*\bRESEARCH\b)', line):
        return "RESEARCH"
    if re.match(r'(?=.*\bEDUCATION\b)', line):
        return "EDUCATION"
    if re.match(r'(?=.*\bINTEREST\b)', line):
        return "INTEREST"
    if re.match(r'(?=.*\bINDUSTRY\b)', line):
        return "INDUSTRY"
    if re.match(r'(?=.*\bDEVELOPMENT\b)', line):
        return "DEVELOPMENT"
    if re.match(r'(?=.*\bSKILL\b)', line):
        return "SKILL"
    if re.match(r'(?=.*\bPROJECT\b)', line):
        return "PROJECT"
    if re.match(r'(?=.*\bPROFILE\b)', line):
        return "PROFILE"
    if re.match(r'(?=.*\bAWARD\b)', line):
        return "AWARD"
    if re.match(r'(?=.*\bEXPERIENCE\b)', line):
        return "EXPERIENCE"
    if re.match(r'(?=.*\bPUBLICATION\b)', line):
        return "PUBLICATION"
    if re.match(r'(?=.*\bPROFESSIONAL\b)', line):
        return "PROFESSIONAL"
    if re.match(r'(?=.*\bCONFERENCE\b)', line):
        return "CONFERENCE"
    if re.match(r'(?=.*\bFEST\b)', line):
        return "FEST"
    if re.match(r'(?=.*\bEXAM\b)', line):
        return "EXAM"
    if re.match(r'(?=.*\bCULTURAL\b)', line):
        return "CULTURAL"
    if re.match(r'(?=.*\bEXTRA\b)', line):
        return "EXTRA"
    if re.match(r'(?=.*\bPERSONAL\b)', line):
        return "PERSONAL"
    if re.match(r'(?=.*\bREFERENCE\b)', line):
        return "REFERENCE"
    if re.match(r'(?=.*\bDECLARATION\b)', line):
        return "DECLARATION"

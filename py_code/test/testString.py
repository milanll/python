#Encoding=utf-8
def OnlyCharNum(s, oth=''):
    s2 = s.lower()
    fomart = 'abcdefghijklmnopqrstuvwxyz0123456789,.'
    for c in s2:
        if not c in fomart:
            s = s.replace(c, '')
    return s


def AMonitorRecord(str):
    str = str.split(":")
    return str[0] + "," + OnlyCharNum(str[1])
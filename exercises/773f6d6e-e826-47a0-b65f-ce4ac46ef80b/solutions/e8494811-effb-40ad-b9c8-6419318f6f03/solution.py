def timeConversion(s):
    hh, mm, ss = s[:-2].split(':')
    period = s[-2:]
    if period == 'AM' and hh == '12':
        hh = '00'
    elif period == 'PM' and hh != '12':
        hh = str(int(hh) + 12)
    return ':'.join([hh, mm, ss])
'''ALKIU - alkiu_util.py
'''

def mk_identifier(s):
    '''Convert an arbitary string to a string usable as an identifier
    '''
    ss = ''
    for i in s:
        if ((ord(i) >= ord('a') and ord(i) <= ord('z'))
            or (ord(i) >= ord('A') and ord(i) <= ord('Z'))
            or (ord(i) >= ord('0') and ord(i) <= ord('9'))):
            ss += i # As it is
        elif i == '_':
            ss+= '__'
        else:
            ss += '_%x_' % ord(i)
    return ss

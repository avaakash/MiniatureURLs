import string


def idToBase62(id: int) -> str:
    mapping = string.ascii_letters + string.digits
    res = ''
    while(id > 0):
        res += str(mapping[id%62])
        id = id // 62
    return res[::-1]


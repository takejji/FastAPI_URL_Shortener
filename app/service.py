import random
import string


def cut_link() -> str:
    return ''.join([random.choice(string.ascii_uppercase + string.digits) for i in range(7)])

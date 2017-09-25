import random
from string import ascii_letters
from string import ascii_lowercase
from string import ascii_uppercase
from string import digits

# 随机大写字母加数字
def random_string(size=6, chars = ascii_letters + digits ):
    return ''.join(random.choice(chars) for _ in range(size))

print(random_string())

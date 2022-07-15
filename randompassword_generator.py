import random
from secrets import choice
import string

password_length = int(input('Digite quantos digitos terá sua senha: '))

lower_case = string.ascii_lowercase + 'ç'
upper_case = string.ascii_uppercase + 'Ç'
punctuation = string.punctuation
numbers = random.randint(0, 9)
characters = lower_case + upper_case + punctuation + str(numbers)
password_result = ''

for i in range(password_length):
    password_result += choice(characters)

print(f'Sua senha é: {password_result}')
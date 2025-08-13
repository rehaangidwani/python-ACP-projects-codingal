import random
import string
password_length = 12
characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
password = ''.join(random.choice(characters) for _ in range(password_length))
password_list = list(password)
random.shuffle(password_list)
shuffled_password = ''.join(password_list)
print("Generated password:", shuffled_password)

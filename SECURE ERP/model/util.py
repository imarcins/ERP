import random
import string



def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):
                small_letters =string.ascii_lowercase
                capital_letters = string.ascii_uppercase
                numbers = string.digits
                special_char = string.punctuation

                generate = random.sample(small_letters,number_of_small_letters)
                generate_v2 = random.sample(capital_letters,number_of_capital_letters)
                generate_v3 = random.sample(numbers,number_of_digits)
                generate_v4 = random.sample(special_char,number_of_special_chars)
                sample = ""
                sample=sample.join(generate)
                sample =sample.join(generate_v2)
                sample= sample.join(generate_v3)
                sample = sample.join(generate_v4)
                return sample


                
    
    

    
    

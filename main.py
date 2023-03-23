import random
import hashlib
from colorama import Fore, Back, Style

class generate_otp(object):
    
    count = 0
    def __init__(self, time, token):
        hashL = hashlib.sha256(self)
        self.time = time
        self.token = token
        generate_otp.count += 1
    
    def otp(self):
        hashL.update(self.time + self.token)
        return hash.hexdigest(self)
        
        
    




from main import generate_otp
import time

t = time.localtime()
t = time.strftime("%H%M%S")
token = "sjdfh8qdh7qhf"

otp = generate_otp(t, token)
print(otp.otp())




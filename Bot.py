
from fbthon import Facebook
from fbthon import Web_Login
import os
import time

print ("[CODED BY BGKE04]")
print ("[BOT AUTO KOMEN]")


print ("")



email = "rhapnelreys@gmail.com"  # Ganti email ini dengan email akun Facebook kamu
password = "Rhapnel#0115" # Ganti password ini dengan password Akun Facebook kamu
login = Web_Login(email,password)
cookie = login.get_cookie_str() #janagn ganti
fb = Facebook(cookie)
print ("SEDANG MENGIRIM KOMEMTAR")
print("")


post = fb.post_parser("https://www.facebook.com/share/p/1J5GRc3w8h/")
post.send_comment("SO BEAUTIFUL KIND AND MAGANDA")
print ("SUCCES")
print ("")
os.system("python bot.py")
#jika sudah maka klik ctrl+x

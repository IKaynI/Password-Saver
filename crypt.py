import random
import string
import base64
# --------------------------------------------------------------------------- Crypt with Key -----------------------------------------------------------------       
# --------------------------------------------------------------------------- Uncrypt with Key -----------------------------------------------------------------
# --------------------------------------------------------------------------- Uncrypt with Key -----------------------------------------------------------------         
def uncrypt(target):
   Fs_string = target
   Fs_string_enc = Fs_string.encode("ascii")
   K64_enc = base64.b64decode(Fs_string_enc)
   Fs_uncrypt = K64_enc.decode("ascii")
   return Fs_uncrypt
   
 # ----------------------------------------------------- crypt-----------------------------------------------------------
def cryptage(target):
   Fs_string = target
   Fs_string_enc = Fs_string.encode("ascii")
   K64_enc = base64.b64encode(Fs_string_enc)
   Fs_crypt = K64_enc.decode("ascii")
   return Fs_crypt

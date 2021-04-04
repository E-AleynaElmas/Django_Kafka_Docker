'''Şifreli mesajın decode edilmesi'''
import base64
import numpy as np
from pathlib import Path

#Dosya sayısı kadar bir dizi
numbers = np.arange(0,494)
base64_array=[]

#sayıların base64'e göre yazılması ve tutulması
for number in numbers:
    sample_string = str(number)
    sample_string_bytes = sample_string.encode("ascii")

    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    base64_array.append(base64_string)

print(len(base64_array))

ascii_string = ""
# Artık hem base64'de hem de sıralanmış
# dosyalardaki binary mesajların okunması ve ascii_string'de tutulması

for base64 in base64_array:
    f = open('kartaca/' + base64, "r")
    a_binary_string= f.readline()
    binary_values = a_binary_string.split()
    for binary_value in binary_values:
        an_integer = int(binary_value, 2)
        ascii_character = chr(an_integer)
        ascii_string += ascii_character

#tüm mesajların bir dosyaya yazılması
message_file = open("message.txt","w")
message_file.write(ascii_string)

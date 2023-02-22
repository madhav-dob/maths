import numpy as np

ecm = [[3,4], [3,6]]
message = "hello world"
print(message)
l = []
for i in message:
    l.append(ord(i))


temp_len = len(l)

if temp_len % 2 == 1:
    l.append(0)
temp_len = len(l)
x22_message = []
a = []
b = []
for i in range(temp_len):
    if i < temp_len//2:
        a.append(l[i])
    else:
        b.append(l[i])


x22_message.append(a)
x22_message.append(b)

print(x22_message)
encoded_message = np.dot(ecm,x22_message)

print(encoded_message)


inv_ecm  = np.linalg.inv(ecm)
print(inv_ecm)
decoded_message = np.dot(inv_ecm,encoded_message)
print(decoded_message)
d1_decoded_message = []
for i in range(len(decoded_message)):
    for j in range(len(decoded_message[i])):
        t = decoded_message[i,j] 
        if t != 0:

            d1_decoded_message.append(int(t))

final = ''.join([chr(x) for x in d1_decoded_message])
print(final)

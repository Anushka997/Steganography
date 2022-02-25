import numpy as np
from PIL import Image


def get_choice():
    while True:
        ch = int(input("Enter an option : \n1. Encode\n2. Decode\n"))
        if ch == 1 or ch == 2:
            return ch
        else:
            print("Wrong choice..Please enter again")


def get_msg():
    msg = input("Enter the message : ")
    print("Length of message :", len(msg))
    while len(msg) > max_char:
        print("Data length limit exeeds..Please try again")
        msg = input("Enter the message : ")
        print("Length of message :", len(msg))
    l = []
    for i in msg:
        b = str(bin(ord(i))).replace('0b', '')
        no = '0' * (8 - len(b)) + b + '0'
        l.append(no)
    l[-1] = l[-1][0:-1] + '1'
    return l


def encode():
    x, y, z = 0, 0, 0
    msg_list = get_msg()
    print("Encoding...")
    for i in msg_list:
        for j in i:
            no = int(j)
            if no == 0 and img[x][y][z] % 2 != 0:
                img[x][y][z] -= 1
            elif no == 1 and img[x][y][z] % 2 == 0:
                img[x][y][z] += 1
            z += 1
            if z == 3:
                z = 0
                y += 1
            if y == width:
                x += 1
                y = 0
                z = 0

    new_image = Image.fromarray(img)
    save_loc = input("Enter image saving location(with name and extension) : ")
    new_image.save(save_loc)
    print("Message encoded sucessfully..")


def decode():
    k = 0
    l = ''
    x = 0
    while True:
        mat = img[x][k:k + 3]
        s = ''
        for i in mat:
            for j in i:
                if int(j) % 2 == 0:
                    s += '0'
                else:
                    s += '1'

        no = int(s[:8], 2)

        l += chr(no)
        if mat[2][2] % 2 == 1:
            break
        if k + 3 == width:
            x += 1
            k = 0
        else:
            k += 3
    print('length of decoded message is : ' + str(len(l)))
    print("The decoded message is : " + l)


img_name = input("Enter image name(with extension) : ")
img = np.array(Image.open(img_name))
width = img.shape[1]
height = img.shape[0]
max_char = height * width // 3
print("Image size : height x width =", height, 'x', width)
print("maximum characters can be encoded are", max_char)

ch = get_choice()
encode() if ch == 1 else decode()

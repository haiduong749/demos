#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ADMIN
#
# Created:     04/05/2022
# Copyright:   (c) ADMIN 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

a = input("Moi ban nhap chuoi")
vtri = int(input("Nhap vao vi tri"))
them = input("nhap ki tu muon them: ")
x = a[:vtri] + them + a[vtri:]
print(x)
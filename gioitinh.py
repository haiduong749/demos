#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ADMIN
#
# Created:     05/05/2022
# Copyright:   (c) ADMIN 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
x = int(input("Nhap tuoi"))
if x >= 18:
    y = input("Nhap gioi tinh: ")
    if y == "nam":
        print("Ahihi")
    else:
        if y == "Nu":
            print("Beatiful")
        else:
            print("Gioi tinh ko xac dinh ")
else:
    print("chua du 18t")
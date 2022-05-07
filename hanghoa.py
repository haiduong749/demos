#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ADMIN
#
# Created:     06/05/2022
# Copyright:   (c) ADMIN 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
x = int(input("Nhap so tien: "))
if x >= 150 :
    y = x - 50
    print("Tong so tien thanh toan: ",y)
elif x >= 100:
    y = x - 25
    print("Tong so tien thanh toan",y)
elif x >= 75:
    y = x - 15
    print("Tong so tien thanh toan",y)
else:
    print("Tong so tien thanh toan",x)

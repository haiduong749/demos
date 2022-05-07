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
x = float(input("Nhap so: "))
if x%2 == 0:
    print("So " + str(x) + " la so chan")
elif x%2 == 1:
    print("So " + str(x) + " la so le")
else:
    print("So " + str(x) + " ko la so tu nhien")
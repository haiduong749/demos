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
x = int(input("Nhap chieu cao(m): "))
y = int(input("Nhap can nang(kg): "))
BMI = y / (x*2)
if BMI > 40:
    print("béo phì cấp độ III")
elif 35 <= BMI < 40:
    print("béo phì cấp độ I")
elif 25 <= BMI < 30:
    print("thừa cân")
elif 18.5 <= BMI < 25:
    print("bình thường")
elif 17 <= BMI < 18.5:
    print("gầy cấp độ I")
elif 16 <= BMI < 17:
    print("gầy cấp độ II")
elif BMI < 16:
    print("gầy cấp độ III")
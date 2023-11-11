#ax + b phương trình bậc nhất
#a=0, b!=0 thì phương trình vô nghiệm
#a=0 ,b=0 thì phương trình có vô số nghiệm
#a!=0 thì phương trình có nghiệm bằng -b/a
a = float(input("Nhập giá trị a: "))
b = float(input("Nhấp giá trị b: "))
if a ==0:
    if b ==0:
        print("Phương trình vô nghiệm")
    else:
        print("phương trình có vô số nghiệm")  
else:
    x = -b/a
    print("Phương trình có nghiệm duy nhất là: ", x)          
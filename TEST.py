# 質數的測試 輸入一個數計算是不是質數
n = int(input("請輸入一個數值    "));
for x in range(2, n):
    print (x)
    if n % x == 0:
        print(n, '等于', x, '*', n//x)
        break
else:
        # 循环中没有找到元素
 print(n, ' 是质数')
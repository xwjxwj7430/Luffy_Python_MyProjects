# 假设一年期定期利率为3.25 %，计算一下需要过多少年，一万元的一年定期存款连本带息能翻番？（编程题）
r = 0.0325
m = 10000
yr = 0

while m < 20000:
    yr += 1
    m = m * (1+r)

print(yr)
print(m)

# 北京地铁交通价格调整为：6公里(含)内3元;6公里至12公里(含)4元;12公里至22公里(含)5元；22公里至32公里(含)6元;32公里以上部
# 分，每增加1元可乘坐20公里。使用市政交通一卡通刷卡乘坐轨道交通，每自然月内每张卡支出累计满100元以后的乘次价格给予8折优惠；
# 满150元以后的乘次给予5折优惠，假设每个月，小明都需要上20天班，每次上班需要来回1次，即每天需要乘坐2次同样路线的地铁,
# 编写程序，从键盘获取距离，帮小明计算每月的总花费。

distance = int(input("家到公司的地铁距离(单位:km):"))
# 先计算单次出行成本，再综合考虑优惠情形；
if 0 < distance <= 6:
    p = 3
elif 6 < distance <= 12:
    p = 4
elif 12 < distance <= 22:
    p = 5
elif 22 < distance <= 32:
    p = 6
else:
    p = 6 + ((distance - 32) // 20 + 1) * 1
    if (distance - 32) % 20 == 0:   # 此处是因为52,72等数应被包含在前一个价位中，所以特别处理
        p = p-1

print(p)

# 这里开始考虑优惠情形，分3档，100元以下，100-150元，150元以上；


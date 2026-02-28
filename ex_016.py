import math
cate_ad = float(input("Digite o cateto adjacente: "))
cate_op = float(input("Digite o cateto oposto: "))
# O Teorema de Pitágoras está também na bibliotaca math
hip = math.hypot(cate_ad,cate_op)

print(hip)

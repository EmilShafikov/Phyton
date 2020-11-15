name = "Tom"
height = 2
weight = 80

bmi = weight / (height ** 2)
print ("Индекс массы тела: " + str(bmi))

if bmi < 25:
    print ("У" + name + " нет лишнего веса")
else:
    print ("У" + name + " есть лишний вес")
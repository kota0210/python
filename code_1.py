x = ['a','b','c','d','e']
print(x[1:4])

y = 9
if y >= 10:
    print('10以上')
elif y >= 0:
    print('0以上10未満')
else:
    print('0未満')

class BodyCondition:
    def bmi_calc(self):
        print('あいうえお')

bc = BodyCondition()
bc.bmi_calc()

x = '山田'
y = '太郎'

result = f'{x + y}さん'
print(result)

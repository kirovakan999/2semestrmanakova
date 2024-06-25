# Составить генератор (yield),
# который переведет символы строки из верхнего регистра в нижний.

def symb_low(stroka):
    for symb in stroka:
        if symb.isupper():
            yield symb.lower()
        else:
            yield symb

test = 'ПрИМер СТРоки длЯ ТеСтИрОвАнИя'
result = ''.join(symb_low(test))
print(result)
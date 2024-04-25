print('[Asil-Bot] Assalomu aleykum')
question = input()
if question == 'Salom ' or ' Assalomu aleykum' or 'Hello':
    print('Salom')
print("User: ",question)

print('Bot: ''Sizga qanday yordam bera olaman?')
question = input()
if question =='Dasturlashni bilasizmi?':
     print('User: ',question)
print('Bot: ''Ha albatta')
if question == 'Menga streak ball oyinini chiqarib ber':
    print('User: ', question)
print('Streak Ball oyini:')
a = int(input('Strike-Ball o\'yini: '))
b = int(input('Ikkinchi son: '))
c = int(input('Uchinchi son: '))
if a == 5:
    print('Correct')
else:
    print('Error')
if b == 2:
    print('Correct')
else:
    print('Error')
if c == 3:
    print('Correct')
else:
    print('Error')



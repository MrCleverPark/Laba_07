k = int(input('k: '))
l = int(input('l: '))
m = int(input('m: '))
n = int(input('n: '))

figure = input('Выберите фигуру(латинскими ЗАГЛАВНЫМИ буквами):\nQ Ферзь\nR Ладья\nE Слон\nH Конь\n')
#if (figure!='Q' or figure!='R' or figure!='E' or figure!='H'):
 #   print('Некорректные значения')
  #  exit()

if ((figure == 'Q' and (k == m or l == n or k - l == m - n or k + l == m + n)) or 
(figure == 'R' and (k == m or l == n)) or 
(figure == 'E' and (k - l == m - n or k + l == m + n)) or
(figure == 'H' and ((abs(k - m) == 1 and abs(l - n) == 2) or (abs(k - m) == 2 and abs(l - n) == 1)))): 
    attack=1
    
else:
    attack=0 
figure2 = input('Выберите фигуру для задачки два(латинскими ЗАГЛАВНЫМИ буквами) \nQ Ферзь\nR Ладья\nE Слон\n')

#if (figure!='Q' or figure!='R'or figure!='E'):
 #   print('неправильные')
  #  exit()
if (k + l + m + n) % 2 == 0:
    print('а) Поле',(k,l),'и поле',(m,n), 'одного цвета')
else:
    print('а) Поле',(k,l),'и поле',(m,n), 'не одного цвета')

if attack==1:
    print('б) Фигура',figure, 'с координатами',(k,l),'угрожает полю',(m,n))
else:
    print('б) Фигура',figure, ' с координатами',(k,l),'не угрожает полю',(m,n))

if ((figure2 == 'Q' and (k == m or l == n or k - l == m - n or k + l == m + n)) or 
(figure2== 'R' and (k == m or l == n)) or # Ладья по горизонтали, вертикали
(figure2 == 'E' and (k - l == m - n or k + l == m + n))): # Слон по диагонали
    print('в) Фигура',figure2, 'с координатами',(k,l),'может одним ходом попасть на поле',(m,n))
else: 
    print('в) Фигура',figure2, 'с координатами',(k,l),'не может одним ходом попасть на поле',(m,n))
    
    if figure2 == 1 or figure2 == 2: # для ферзя и ладьи это ход по вертикали 
        print('Можно попасть за два хода. Следующий ход на клетку:',(k,n))
    elif figure2 == 3: 
        if (k + l + m + n) % 2 == 0: 
            for i in range(1, 9): 
                for o in range(1, 9): # Перебор клеток
                    if (i == k and o == l) or (i == m and o == n): 
                        continue
                    if (k - l == i - o or k + l == i + o) and (i - o == m - n or i + o == m + n): # если текущая клетка досягаема для слона 
                        print('Можно попасть за два хода. Следующий ход на клетку:',(i,o))
                        break
        else: # Слон не может перейти на другой цвет
            print('в) Фигура',figure2, 'на', (k,l),'не может попасть на поле', (m,n))
            


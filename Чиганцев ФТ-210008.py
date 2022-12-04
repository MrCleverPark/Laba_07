import logging
logging.basicConfig(filename = 'py_log.log', level = logging.INFO)
k = int(input('k: '))
l = int(input('l: '))
m = int(input('m: '))
n = int(input('n: '))
logging.info('Introduced coordinates for cells: k,l,m,n')
figure = int(input('Выберите фигуру:\n1 Ферзь\n2 Ладья\n3 Слон\n4 Конь\n'))
logging.info('One of the figures entered')
if ((figure == 1 and (k == m or l == n or k - l == m - n or k + l == m + n)) or 
(figure == 2 and (k == m or l == n)) or 
(figure == 3 and (k - l == m - n or k + l == m + n)) or
(figure == 4 and ((abs(k - m) == 1 and abs(l - n) == 2) or (abs(k - m) == 2 and abs(l - n) == 1)))): 
    attack=1
    
else:
    attack=0 
figure2 = int(input('Выберите фигуру для задачки два \n1 Ферзь\n2 Ладья\n3 Слон\n'))
logging.info('One of the figures entered')
if figure2 < 1 or figure2  > 3:
    print('Выберите цыфру  1, 2 или 3')
    logging.info('Выберите цыфру  1, 2 или 3')
    exit()
if (k + l + m + n) % 2 == 0:
    print('а) Поле',(k,l),'и поле',(m,n), 'одного цвета')
    logging.info('a) Single color field')
else:
    print('а) Поле',(k,l),'и поле',(m,n), 'не одного цвета')
    logging.info('a) Fields not the same color')

if attack==1:
    print('б) Фигура',figure, 'с координатами',(k,l),'угрожает полю',(m,n))
    logging.info('b) The figure threatens the field')
else:
    print('б) Фигура',figure, ' с координатами',(k,l),'не угрожает полю',(m,n))
    logging.info('b) The piece does not threaten the field')

if ((figure2 == 1 and (k == m or l == n or k - l == m - n or k + l == m + n)) or 
(figure2== 2 and (k == m or l == n)) or # Ладья по горизонтали, вертикали
(figure2 == 3 and (k - l == m - n or k + l == m + n))): # Слон по диагонали
    print('в) Фигура',figure2, 'с координатами',(k,l),'может одним ходом попасть на поле',(m,n))
    logging.info('B)a piece can land on a given square in one move')
else: 
    print('в) Фигура',figure2, 'с координатами',(k,l),'не может одним ходом попасть на поле',(m,n))
    logging.info('B)a piece cannot land on a given square in one move')
    if figure2 == 1 or figure2 == 2: # для ферзя и ладьи это ход по вертикали 
        print('Можно попасть за два хода. Следующий ход на клетку:',(k,n))
        logging.info('B)Can be hit in two moves')
    elif figure2 == 3: 
        if (k + l + m + n) % 2 == 0: 
            for i in range(1, 9): 
                for o in range(1, 9): # Перебор клеток
                    if (i == k and o == l) or (i == m and o == n): 
                        continue
                    if (k - l == i - o or k + l == i + o) and (i - o == m - n or i + o == m + n): # если текущая клетка досягаема для слона 
                        print('Можно попасть за два хода. Следующий ход на клетку:',(i,o))
                        logging.info('B)Can be hit in two moves')
                        break
        else: # Слон не может перейти на другой цвет
            print('в) Фигура',figure2, 'на', (k,l),'не может попасть на поле', (m,n))
            logging.info('B)a piece cannot enter the field')
            


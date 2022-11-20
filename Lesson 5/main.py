a = 4
b = 0

try:
    print(a/b)
except ZeroDivisionError:
    print('Делить на 0 нельзя!')
except Exception as error:
    print(f'Что-то пошло не так: {error}')
else:
    print('Ошибок не было')

print('Программа не вылетела')


# ========

try:
    # Код, который может выдать ошибку
    pass
except ZeroDivisionError:
    # Действия в случае деления на ноль
    pass
except Exception as error:
    # Действия в случае возникновения любой другой ошибки
    pass
else:
    # Действия в случае отсутствия ошибки
    pass


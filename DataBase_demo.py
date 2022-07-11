import datetime
from utilities.configurations import get_connection


# для подключения нужны 4 параметра: host, database, user, password
# можно подключиться так, просто и быстро:
# connection = mysql.connector.connect(host='localhost', database='APIDevelop', user='root', password='root')
# а можно более грамотно:
connection = get_connection()
assert connection.is_connected()

cursor = connection.cursor()
cursor.execute('select * from CustomerInfo')

# row = cursor.fetchone()  # вернёт первую запись ответа
# print(row)
# print(row[3])
#
# rowAll = cursor.fetchall()  # вернёт все записи ответа, но если использовалось перед этим cursor.fetchone(), то вернёт
#                             # все ОСТАВШИЕСЯ записи ответа, т.е. кроме первой, т.к. курсор уже находится на 2 позиции
# print(rowAll)
# print(rowAll[0][3])

# Existing DB
rows = cursor.fetchall()
print(len(rows))
sum = 0
for row in rows:
    print(row)
    sum = sum + row[2]
print(sum)
print('--------------------------')
assert sum == 340, f'Control sum must be 340, we have == {sum}'

# How add data to DB
query_insert = 'INSERT INTO CustomerInfo values (%s, %s, %s, %s)'
data_insert = ('WebServices', datetime.date.today(), 21, 'Asia')
cursor.execute(query_insert, data_insert)
connection.commit()  # если не закоммитить, то удаление будет видно только в Python, но не в самой базе
cursor.execute('select * from CustomerInfo')
afterInsert = cursor.fetchall()
print(len(afterInsert))
for row in afterInsert:
    print(row)
print('--------------------------')


# How update data in DB
query_update = 'update CustomerInfo set Location = %s where CourseName = %s'
data_update = ('Belarus', 'WebServices')
cursor.execute(query_update, data_update)
connection.commit()  # если не закоммитить, то изменение будет видно только в Python, но не в самой базе
cursor.execute('select * from CustomerInfo')
afterChange = cursor.fetchall()
print(len(afterChange))
for row in afterChange:
    print(row)
print('--------------------------')


# How delete data from DB
query_delete = 'delete from CustomerInfo where CourseName = %s'
data_delete = ('WebServices',)
cursor.execute(query_delete, data_delete)
connection.commit()  # если не закоммитить, то удаление будет видно только в Python, но не в самой базе
cursor.execute('select * from CustomerInfo')
afterDelete = cursor.fetchall()
print(len(afterDelete))
for row in afterDelete:
    print(row)
print('--------------------------')
connection.close()

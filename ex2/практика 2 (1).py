x = 0
y = 0
n = 0
flag = True
x1 = int(input())
y1 = int(input())
storona_kyda_idti = input()
chislenost_chagov = int(input())
while storona_kyda_idti != 'Стоп':
    if x1 == x and y1 == y:
        flag = False
    if storona_kyda_idti  == 'Вперед':
        y += chislenost_chagov
        if flag:
            n += 1
    elif storona_kyda_idti == 'Налево':
        x -= chislenost_chagov
        if flag:
            n += 1
    elif storona_kyda_idti == 'Разворот':
        y -= chislenost_chagov
        if flag:
            n += 1
    elif storona_kyda_idti == 'Направо':
        x += chislenost_chagov
        if flag:
            n += 1
    storona_kyda_idti = input()
    if storona_kyda_idti != 'Стоп':
        chislenost_chagov = int(input())
print(n)

# exam

ex01.py
moji = input( '文字列を入力してください >')

print(moji)
print(len(moji))





ex04.py
def pwdqieku():
    id = 'yoshino'
    pwd = 'yt1974'
    id1 = input( 'IDを入力してください >')
    pwd1 = input( 'pwdを入力してください >')
    if id == id1 and pwd==pwd1:
      print('okです')
    else :
      print('IDかパスワードが違います')

pwdqieku()


ex05.py
def listreplace():
    list= [13,17,31,57,' ',41,83]
    list.remove(' ')
    print(list)

listreplace()
def listave():
   list = [13,17,31,57,41,83]
   ave = sum(list) / len(list)

   print(ave)

listave()

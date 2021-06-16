def maildomein():
    mail = input('メールアドレスを入力してください:')
    word1 = '@'
   	motomail = mail.find(word1)
   	cutmail = mail[motomail+1:]
   	print(cutmail)
   	
maildomein()
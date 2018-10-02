def new_password(oldpassword, newpassword):
    if newpassword != oldpassword and len(newpassword) > 6:
        print(True)
    else: print(False)
new_password('boterham', 'boter2')

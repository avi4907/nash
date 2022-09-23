email=input('enter your email=>')
if '@' in email:
    print('your email does not have @')
elif len(email)<11:
    print('length of email not valid ')
elif '.com' in email or 'org' in email:
    print('your email look valid')
else:
    print('invalid email')
    

import pwinput

text='mysql -u uodksj20ljf64ecd -pKqhImxBuNUQFxIDekwVi -h bbvudwhkuqtqhqauukg6-mysql.services.clever-cloud.com -P 3306 -D bbvudwhkuqtqhqauukg6'

cmd=text.split()
host=''
user=''
port=''
database=''
password=''
for i in cmd:
    if i == '-h':
        host=cmd[cmd.index(i)+1]
    elif i == '-u':
        user=cmd[cmd.index(i)+1]
    elif i == '-P':
        port=cmd[cmd.index(i)+1]
    elif i == '-D':
        database=cmd[cmd.index(i)+1]
    elif i.startswith('-p') and len(i) > 2:
        password=i[2:]
    elif i == '-p':
        password = pwinput.pwinput(prompt='Enter your Password: ')

print(host)
print(user)
print(port)
print(database)
print(password)


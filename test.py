
db_name=''
ch = 'sw db -i 9'

if '-i' in ch.lower().split():
    db_name=ch.split()[-1]
else:
    pass

print(db_name)


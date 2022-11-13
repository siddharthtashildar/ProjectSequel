query='add data (1002,"Elon",978866,989877665,"Boca Chica,Texas") to bank'

text=''

print(query.partition('to')[2].partition('(')[0])

    
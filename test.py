query=r"modify pincode int(6) not null Primary key auto_increment after address in table bank"

print(query.partition('in table')[0].partition('modify')[2].partition('md')[2].strip())



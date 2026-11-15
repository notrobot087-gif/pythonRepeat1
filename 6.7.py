line=[]
for i in range(1,6):
    row=[]
    for j in range(1,6):
        row.append(i*j)
    line.append(row)
for row in line:
    print(row)
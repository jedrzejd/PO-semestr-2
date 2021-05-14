cnt = 0
with open('in.txt') as x:
    for line in x:
        f = line.split(' ')[0]
        b = line.split(' ')[1].split()[0]
        a = f.split('-')[0]
        b = f.split('-')[1]
        let = line.split(' ')[1][0]
        slo = line.split(' ')[2]
        licz=0
        for x in slo:
            if x == let:
                licz+=1 
        if (licz >= int(a) and licz <= int(b)):
            n+=1

print(n)

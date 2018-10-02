def main():

    lst =[]
    durn = []

    task= ['work,0650,0730',
          'read,1100,1115',
          'play,1210,1250',
          'read,1515,1530',
          'eat,1130,1430',
          'run,1750,1930',
          'eat,2000,2100',
          'play,1800,2100']

    lst1 = []
    for i in range(0, len(task)):
        x = task[i].split(',')
        lst1.append(x)
        s = x[1]
        t = x[2]
        s1 = ((int(s[:2]))*60) + (int(s[2:]))
        s2 = ((int(t[:2])) * 60) + (int(t[2:]))
        durn.append(s2-s1)
        lst.append(x[0])

    lst1.sort(key=lambda x: int(x[1]))

    print (lst)
    print (list(set(lst)))
    print(durn)
    for i in range(0,len(lst1)-1):
        if (lst1[i][2]) > (lst1[i+1][1]):
            print (str(lst1[i][0])+","+ str(lst1[i][1])+","+str(lst1[i][2]) +"  overlaps with  " + str(lst1[i+1][0])+","+ str(lst1[i+1][1])+","+str(lst1[i+1][2]))


if __name__== "__main__":
    main()
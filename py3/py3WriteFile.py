t1r = open('text1.txt').read()
t2r = open('text2.txt').read()
combine = t1r + ' and ' + t2r
opf1 = open('test3.txt','w')
opf1.write(combine)
opf1.close()

page = open('index')
page = page.read().replace('\n','')

isphylum = False
isclas = False
issubclas = False
isorder = False
issuborder = False
isfamily = False
isgenus = False
unclas = 'Unclassified'

c = 0
phylum = ""
clas = ""
subclas = ""
order = ""
suborder = ""
family = ""
genus = ""

phylums = []
clasers = []
subclasers = []
orders = []
suborders = []
families = []
genuses = []

alldata = []

for i in page:
    if c > 7 and c < len(page)-2:
        if (i == "'" or i == '"'):
            if page[c-11:c] == 'phylumlevel':
                isphylum = True
            elif page[c-10:c] == 'classlevel':
                isclas = True
            elif page[c-13:c] == 'subclasslevel':
                issubclas = True
            elif page[c-10:c] == 'orderlevel':
                isorder = True
            elif page[c-13:c] == 'suborderlevel':
                issuborder = True
            elif page[c-11:c] == 'familylevel':
                isfamily = True
            elif page[c-10:c] == 'genuslevel':
                isgenus = True
            else:
                genus = genus

        if isphylum:
            if page[c+2] != '<':
                phylum += page[c+2]
            else:
                isphylum = False
                phylum = phylum.replace('&quot;','')
                #phylum = phylum.replace('Phylum ','')
                phylums.append(phylum)
                #print phylum
                alldata.append(phylum)
                phylum = ''
        if isclas:
            if page[c+2] != '<':
                clas += page[c+2]
            else:
                isclas = False
                clas = clas.replace('Class ','')
                clas = clas.replace('&quot;','')
                if unclas in clas:
                    clas = '????????????'
                clas = 'Class ' + clas
                #print ' ' + clas
                alldata.append(clas)
                clas = ''
        if issubclas:
            if page[c+2] != '<':
                subclas += page[c+2]
            else:
                issubclas = False
                subclas = subclas.replace('Subclass ','')
                subclas = subclas.replace('&quot;','')
                if unclas in subclas:
                    subclas = '????????????'
                subclas = "Subclass " + subclas
                #print '  ' + subclas
                alldata.append(subclas)
                subclas = ''
        if isorder:
            if page[c+2] != '<':
                order += page[c+2]
            else:
                isorder = False
                order = order.replace('Order ','')
                order = order.replace('&quot;','')
                if unclas in order:
                    order = '????????????'
                order = 'Order ' + order
                orders.append(order)
                #print '   ' + order
                alldata.append(order)
                order = ''
        if issuborder:
            if page[c+2] != '<':
                suborder += page[c+2]
            else:
                issuborder = False
                suborder = suborder.replace('Suborder ','')
                suborder = suborder.replace('&quot;','')
                if unclas in suborder:
                    order = '????????????'
                suborder = 'Suborder ' + suborder
                #print '    ' + suborder
                alldata.append(suborder)
                suborder = ''
        if isfamily:
            if page[c+2] != '<':
                family += page[c+2]
            else:
                isfamily = False
                #family = family.replace('Family ','')
                family = family.replace('&quot;','')
                families.append(family)
                #print '     ' + family
                alldata.append(family)
                family = ''
        if isgenus:
            if page[c+2] != '<':
                genus += page[c+2]
            else:
                isgenus = False
                genus = genus.replace('&quot;','')
                genus = 'Genus ' + genus
                #print '      ' + genus
                alldata.append(genus)
                genus = ''
    c += 1







phylum = False
clas = False
subclas = False
order = False
suborder = False
genus = False 
arrdata = ['????????????','????????????','????????????','????????????','????????????','????????????','????????????']
thedata = []

for i in alldata:
    if 'Phylum ' in i:
        arrdata[0] = i.replace('Phylum ','')
        arrdata[1:] = [] 
        for j in range(1,7):
            arrdata.append('????????????')
    if 'Class ' == i[0:6]:
        if 'Sub' in i:
            arrdata[2] = i.replace('Class ','')
            arrdata[2] = arrdata[2].replace('Subclass ','')
            arrdata[3:] = []
            for j in range(3,7):
                arrdata.append('????????????')
        else:
            arrdata[1] = i.replace('Class ','')
            arrdata[2:] = []
            for j in range(2,7):
                arrdata.append('????????????')
    if 'Order ' == i[0:6]:
        if 'Sub' in i:
            arrdata[4] = i.replace('Order ','')
            arrdata[4] = arrdata[4].replace('Suborder ','')
            arrdata[5:] = []
            for j in range(5,7):
                arrdata.append('????????????')
            print arrdata
        else:
            arrdata[3] = i.replace('Order ','')
            arrdata[4:] = []
            for j in range(4,7):
                arrdata.append('????????????')
    if 'Family ' in i:
        arrdata[5] = i.replace('Family ','')
        arrdata[6] = '????????????' 
    if 'Genus ' in i:
        arrdata[6] = i.replace('Genus ','')
        #print arrdata
        thedata.append(arrdata[:])
'''
len1 = 0 
len2 = 0 
len3 = 0 
len4 = 0 
len5 = 0 
for i in thedata:
    if len(i[0]) > len1:
        len1 = len(i[0])
    if len(i[1]) > len2:
        len2 = len(i[1])
    if len(i[2]) > len3:
        len3 = len(i[2])
    if len(i[3]) > len4:
        len4 = len(i[3])
    if len(i[4]) > len5:
        len5 = len(i[4])
print len1,len2,len3,len4,len5
'''
alldatastr = ''
for i in range(0,len(thedata)):
    alldatastr += "%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % \
            (thedata[i][0], thedata[i][1],
             thedata[i][2], thedata[i][3],
             thedata[i][4], thedata[i][5],
             thedata[i][6])
f = open('data1','w')
f.write(alldatastr)
f.close()

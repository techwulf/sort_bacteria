page = open('index')
page = page.read().replace('\n','')

class CheckIt(object):


    def __init__(self, word):

        self.word = word
        self.name = self.word.replace('level','').title()
        self.name = self.name.replace("'",'')
        self.state = False
        self.bact = ''

    def checkstate(self, section):
        if self.word == section:
            self.state = True

    def addletter(self, letter):
        self.bact += letter


def iterate(page):
    c = 0
    alldata = []
    percent = len(page)/100
    loadbar = ''
    collumns = ["'phylumlevel'","'classlevel'","'subclasslevel'","'orderlevel'", \
                "'suborderlevel'","'familylevel'","'genuslevel'"]

    for k in range(0,len(collumns)):
        collumns[k] = CheckIt(collumns[k]) 

    for i in page:

        if c > 15 and c < len(page)-1:
            
            for j in range(len(collumns)):
                collumn = len(collumns[j].word) 
                section = page[c-collumn:c]
                collumns[j].checkstate(section)

                if collumns[j].state == True:

                    if page[c+1] != '<':
                        collumns[j].addletter(page[c+1])
                    else:
                        collumns[j].state = False
                        if 'Unclassified' in collumns[j].bact:
                            collumns[j].bact = '%s unclassified' % \
                                    collumns[j].name
                        if collumns[j].name == 'Genus':
                            collumns[j].bact = 'Genus %s' % \
                                    collumns[j].bact

                        alldata.append(collumns[j].bact.replace('&quot;',''))
                        collumns[j].bact = ''

        if c % percent == 0 and c != 0:
            loadbar = '#'*(c/percent)
            print "\r parsing : %s [{%s%s}]" % (100 - \
                                                (100 - len(loadbar)), \
                                                loadbar, ' '*\
                                                (100-len(loadbar))),

        c += 1

    print ''
    sort(alldata)

def sort(alldata):
    wholeset = [] 
    blankset = ['unclassified','unclassified','none','unclassified', \
                'none','unclassified','unclassified']

    bacts = ['Phylum ','Class ','Subclass ','Order ', \
             'Suborder ','Family ','Genus ']

    theset = blankset[:]

    for i in alldata:
        for j in range(0,len(bacts)):

            if bacts[j] in i:

                if bacts[j] == bacts[-1]:
                    theset[j] = i.replace(bacts[j],'')
                    wholeset.append(theset[:])  

                else:
                    theset[j] = i.replace(bacts[j],'')
                    del theset[j+1:]
                    for m in range(j+1,len(bacts)):
                        theset.append(blankset[m])






iterate(page)

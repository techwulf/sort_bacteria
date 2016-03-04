import time
from subprocess import call


call (["rm","-classifphyla.html"])
call (["wget","http://www.bacterio.net/-classifphyla.html"])
page = open('-classifphyla.html')
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
    un = 1
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
                    for k in range(0,6):
                        if theset[k] == 'unclassified':
                            if theset[k] in preset[k] and \
                               theset[0:k] == preset[0:k]:

                                theset[k] = preset[k]
                            else:
                                theset[k] = 'unclassified' + str(un)
                                un += 1
                        if theset[k] == theset[k+1]:
                            theset[k+1] = theset[k+1].lower()
                    wholeset.append(theset[:])  
                    preset = theset[:]

                else:
                    theset[j] = i.replace(bacts[j],'')
                    del theset[j+1:]
                    for m in range(j+1,len(bacts)):
                        theset.append(blankset[m])

    unchild(wholeset)



class UnChild(object):

    def __init__(self, parent):

        self.parent = parent
        self.children = 0
        self.child = ''

    def check(self, child):

        if self.child != child:
            self.child = child
            self.children += 1
        if self.parent == 'none':
            self.children = 0


def unchild(wholeset):
    wholeset = wholeset
    parent = ''
    child = ''
    parents = {} 
    row = 0
    un = 1
    cn = 1
    count = -1
    document = ''
    localtime = time.asctime( time.localtime(time.time()) )

    for i in wholeset:
        for j in range(0,6):
            parent = i[j]
            if parent not in parents:
                if i[j+cn] == 'none':
                    cn = 2

                child = i[j+cn]
                parents[parent] = UnChild(parent)
                parents[parent].check(child)
            else:
                if i[j+cn] == 'none':
                    cn = 2

                child = i[j+cn]
                parents[parent].check(child)
            wholeset[count][j] = parents[parent].parent
            wholeset[count][j+cn] = parents[parent].child
            cn = 1
        count += 1
        #for k in wholeset[count]:
            #print k,
            #if k in parents:
                #print parents[k].children,
        #print

    document = '################ %s ################\n' % localtime

    for i in wholeset:
        for j in range(0,len(i)):
            if i[j] in parents:
                document += '%s\t%s\t' % (i[j], parents[i[j]].children)
            else:
                document += '%s' % i[j]
        document += '\n'

    finished = open('%s.txt' % localtime,'w')
    finished.write(document)
    finished.close();





iterate(page)

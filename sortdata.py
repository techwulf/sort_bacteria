bacteria = open('data1')
bacteria = bacteria.read()
bacteria = bacteria[0:-2]
bacteria = bacteria.split('\n')

class Bacterium(object):

    def __init__(self, name, count, kid):
        self.name = name
        self.count = count
        self.kid = kid
        self.none = False
        if name == 'none':
            self.none = True

    def getname(self):
        return self.name

    def getkid(self):
        return self.kid

    def checkkid(self, newkid):
        if newkid != self.kid:
            self.kid = newkid
            self.count += 1
        if self.none == True:
            self.count = 0 
            return self

def dostuff(bacteria):

    bacteriums = {}
    ucount = 0

    for i in range(0,len(bacteria)):
        bacteria[i] = bacteria[i].split('\t')

        for k in (2,4):
            if '?' in bacteria[i][k]:
                bacteria[i][k] = 'none'

        for l in [0,1,3,5]:
            if '?' in bacteria[i][l]:
                bacteria[i][l] = 'unclassified'

        for j in range(0,6):
            parent = bacteria[i][j]
            kid = ''

            if parent == "none":
                ucount = ucount

            elif parent not in bacteriums:
                if bacteria[i][j+1] == "unclassified":
                    bacteria[i][j+1] = 'unclassified%s' % (ucount)
                    ucount += 1

                if bacteria[i][j+1] == "none":
                    if bacteria[i][j+2] == "unclassified":
                        bacteria[i][j+2] == 'unclassified%s' % (ucount)
                        ucount += 1

                    kid = bacteria[i][j+2]
                else:
                    kid = bacteria[i][j+1]

                bacteriums[parent] = Bacterium(parent, 0, kid)

            else:
                if 'unclassified' in '%s'%(bacteriums[parent].kid):
                    if bacteria[i][j+1] == "unclassified":
                        bacteria[i][j+1] = bacteriums[parent].kid 

                if bacteria[i][j+1] == "none":
                    if bacteria[i][j+2] == "unclassified":
                        bacteria[i][j+2] == 'unclassified%s' % (ucount)
                        ucount += 1

                    kid = bacteria[i][j+2]
                else:
                    kid = bacteria[i][j+1]

                bacteriums[parent].checkkid(kid)
    for i in bacteriums:
        item = bacteriums[i]
        if 'unclas' in item.name:
            print item.name, item.count

dostuff(bacteria)

bact = Bacterium('acidomera', 0, 'acidormia')
bact = bact.checkkid('acidomena')

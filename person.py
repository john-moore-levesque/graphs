import re
import datetime
from node import Node


class Person(Node):
    def __init__(self, firstname, middlename, Family, dob, gender, surname=None, dod=False):
        Node.__init__(self, firstname + ' ' + middlename)
        self.relatives = {'parents': {'father': [], 'mother': []},
                            'children': {'son': [], 'daughter': []}}
        if not surname:
            self.surname = Family.name
        else:
            self.surname = surname
        self.setGraph(Family)
        self.dob = formatDateString(dob)
        self.dod = formatDateString(dod)
        self.gender = gender
        self.adopted = False
        if gender == "male":
            self.childType = "son"
            self.parentType = "father"
        else:
            self.childType = "daughter"
            self.parentType = "mother"

    def addParent(self, Person):
        self.relatives['parents'][Person.parentType].append(Person)
        self.relate(Person, directed=True, weight=-1)

    def addChild(self, Person):
        self.relatives['children'][Person.childType].append(Person)
        self.relate(Person, directed=True, weight=1)

    def isAilve(self):
        return not self.dod

    def kill(self, dod):
        self.dod = formatDateString(dod)

    def newFamily(self, Family):
        self.setGraph(Family)
        self.surname = Family.name

    def married(self, Person, takeName=False, hybridName=False, joinFam=False):
        self.spouse = Person
        if takeName or hybridName:
            if hybridName:
                self.surname = hybridName
            else:
                self.surname = Person.surname
        if joinFam:
            self.family = self.setGraph(Person.graph)
        self.relate(Person, directed=False)

    def relate(self, Person, directed=True, weight=0):
        self.addNeighbor(Person, directed, weight=0)

    def divorce(self, Person, oldName=False):
        self.removeNeighbor(Person, directed=False)
        if oldName:
            self.surname = oldName

    def isSibling(self, Person):
        sharedParents = 0
        for ptype in self.relatives['parents']:
            for parent in self.relatives['parents'][ptype]:
                if parent in Person.relatives['parents'][ptype]:
                    sharedParents += 1
        if sharedParents == 2:
            return True
        elif sharedParents == 0:
            return False
        else:
            return 0.5

    def isAdopted(self, ParentArray):
        self.adopted = True
        for parent in ParentArray:
            self.relatives['parents'][parent.parentType].append(parent)

    def isAuntOrUncle(self, Person):
        for ptype in self.relatives['parents']:
            for parent in self.relatives['parents'][ptype]:
                if parent.isSibling(Person):
                    return True
        return False

    def isNieceOrNephew(self, Person):
        return Person.isAuntOrUncle(self)

    def isParent(self, Person):
        if Person in self.relatives['children'][Person.childType]:
            return True
        else:
            return False

    def isGrandparent(self, Person):
        for ptype in self.relatives['parents']:
            for parent in self.relatives['parents'][ptype]:
                if Person in parent.relatives['parents'][Person.parentType]:
                    return True
        return False

    def isGrandchild(self, Person):
        return Person.isGrandparent(self)

    def isCousin(self, Person):
        for ptype in Person.relatives['parents']:
            for prnt in Person.relatives['parents'][ptype]:
                for parent in self.relatives['parents'][ptype]:
                    if parent.isSibling(prnt):
                        return True
        return False


def formatDateString(dstr):
    '''
    convert dob (or dod) string to timestamp
    '''
    patterns = (
        ('\D{4,} \d{1,2} \d{4}$', '%B %d %Y'),
        ('\D{3} \d{1,2} \d{4}$', '%b %d %Y'),
        ('\d{1,2} \D{4,} \d{4}$', '%d %B %Y'),
        ('\d{1,2} \D{3} \d{4}$', '%d %b %Y'),
        ('\D{4,} \d{1,2} \d{2}$', '%B %d %y'),
        ('\D{3} \d{1,2} \d{2}$', '%b %d %y'),
        ('\d{1,2} \D{4,} \d{2}$', '%d %B %y'),
        ('\d{1,2} \D{3} \d{2}$', '%d %b %y'),
        ('(\d{1,2}\/){2}\d{4}$', '%m/%d/%Y'),
        ('(\d{1,2}\/){2}\d{2}$', '%m/%d/%y')
    )

    if not isinstance(dstr, str):
        return False

    if re.search('[a-zA-Z]', dstr):
        dstr = re.sub('\. |\, |\/|rd |th |st ', ' ', dstr)

    for pattern, dpat in patterns:
        if re.search(pattern, dstr):
            return datetime.datetime.strptime(dstr, dpat)
    return False

from graph import Graph


class Family(Graph):
    def __init__(self, familyname):
        Graph.__init__(self, familyname, True)

    def addPerson(self, Person):
        self.addNode(Person)

    def wedding(self, Person1, Person2, takeName1=False, takeName2=False,
                    hybridName1=False, hybridName2=False, joinFam1=False, joinFam2=False):
        Person1.married(Person2, takeName1, hybridName1, joinFam1)
        Person2.married(Person1, takeName2, hybridName2, joinFam2)

    def divorce(self, Person1, Person2, oldName1, oldName2):
        Person1.divorced(Person2, oldName1)
        Person2.divorced(Person1, oldName2)

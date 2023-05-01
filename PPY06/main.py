class Student:
    def __init__(self, email, name, surname, all_grade=None, status=None):
        if all_grade is None:
            self.all_grade = {
                "project": -1,
                "l_1": -1,
                "l_2": -1,
                "l_3": -1,
                "h_1": -1,
                "h_2": -1,
                "h_3": -1,
                "h_4": -1,
                "h_5": -1,
                "h_6": -1,
                "h_7": -1,
                "h_8": -1,
                "h_9": -1,
                "h_10": -1,
                "grade": -1,
            }
        else:
            self.all_grade = all_grade
        self.email = email
        self.name = name
        self.surname = surname
        if status is None:
            self.status = None
        else:
            self.status = status

    def __repr__(self):
        return f"Student(email='{self.email}', name = '{self.name}', surname = '{self.surname}', " \
               f"all_grade = {self.all_grade}, status = {self.status})"

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.email == other.email

    @staticmethod
    def compareStudentsNames(x, y):
        return x.name >= y.name

    @staticmethod
    def compareStudentsSurnames(x, y):
        return x.surname >= y.surname

    def getPersonalData(self):
        return self.email, self.name, self.surname


class Element:
    def __init__(self, data=None, nextE=None):
        self.data = data
        self.nextE = nextE


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        res = []
        cur = self.head
        while cur:
            res.append(str(cur.data))
            cur = cur.nextE
        return ' -> '.join(res)

    def get(self, e):
        cur = self.head
        while cur:
            if cur.data == e:
                return cur
            cur = cur.nextE
        return None

    def delete(self, e):
        if not self.head:
            return
        if self.head.data == e:
            self.head = self.head.nextE
            self.size -= 1
            return
        cur = self.head
        prev = None
        while cur:
            if cur.data == e:
                prev.nextE = cur.nextE
                self.size -= 1
                return
            prev = cur
            cur = cur.nextE

    def append(self, e, func=None):
        new_elem = Element(e)
        if not self.head:
            self.head = new_elem
            self.tail = new_elem
            self.size += 1
            return
        if func is None:
            func = lambda x, y: x >= y
        cur = self.head
        prev = None
        while cur:
            if func(cur.data, e):
                if not prev:
                    new_elem.nextE = self.head
                    self.head = new_elem
                else:
                    new_elem.nextE = cur
                    prev.nextE = new_elem
                self.size += 1
                return
            prev = cur
            cur = cur.nextE
        prev.nextE = new_elem
        self.tail = new_elem
        self.size += 1


list = MyLinkedList
list.__init__(list)
e = 2
e2 = 1
list.append(list,e)
list.append(list,e2)


print(list.__str__(list))

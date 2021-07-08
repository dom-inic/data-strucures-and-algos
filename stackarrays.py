class MyStack:

    def __init__(self):
        self.data=[]

    def length(self): #length of the list 
        return len(self.data)

    # check if the list is full of not
    def is_full(self):
        if len(self.data) == 5:
            return True
        else:
            return False

    # insert a new element
    def push(self, element):
        if len(self.data) < 5:
            self.data.append(element)
        else:
            return "overflow"

    def pop(self): # remove the last element from a list 
        if len(self.data) == 0:
            return "underflow"

        else:
            self.data.pop()


# create an instance of the object 
s = MyStack()

s.push(15)
s.push(8)
s.push(8)
s.push(8)
s.push(8)
s.push(8)

print(s.length())
s.push(85)
print(s.is_full())
s.pop()
print(s.length())
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
print(s.length())

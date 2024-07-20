print("===============================================================================")
class Stack:
    def __init__(self):
        self.values = []

    def pop(self):
        if self.isempty():
            return None
        return self.values.pop()
        #return self.values.pop(0)

    def push(self, item):
        self.values.append(item)
        #self.values = [item] + self.values

    def isempty(self):
        return len(self.values) == 0

    def peek(self):
        if self.isempty():
            return None
        return self.values[-1]

    def size(self):
        return len(self.values)

    def __str__(self):
        return str(self.values)


st = Stack()
print("Is stack empty?", st.isempty()) 
st.push("Zeeshan khursheed")
st.push("Age : 20")
st.push(40)
st.push("ai generator")
print("Is stack empty?", st.isempty()) 
print("Size of stack is:", st.size())
print("Top of stack is:", st.peek())
print("Stack is:", st)
print("Popped : ",st.pop())
print("Popped : ",st.pop())

print("Top of stack is:", st.peek())
print("Stack is:", st)

print("===============================================================================")
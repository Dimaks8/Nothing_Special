class MyNode: 
def __init__(self, value=None, next=None): 
self.value = value 
self.next = next 

class MyList: 
def __init__(self): 
self.head = None 
self.last = None 

def __str__(self): 
if self.head == None: 
return "Empty List" 
else: 
tmp = self.head 
str_out = str(tmp.value) + " " 
while tmp.next != None: 
tmp = tmp.next 
str_out = str_out + str(tmp.value) + " " 
return str_out 

def add(self, num): 
if self.head == None: 
self.head = self.last = MyNode(num) 
else: 
self.last.next = MyNode(num) 
self.last = self.last.next 

def find(self, num): 
if self.head == None: 
print("List is Empty;", end = ' ') 
return 
elif self.head.value == num: 
return self.head 
else: 
tmp = self.head 
while tmp.next != None: 
if tmp.next.value == num: 
return tmp 
tmp = tmp.next 
return None 

def delete(self, num): 
tmp = self.find(num) 
if tmp == None: 
print("Number is not defined") 
elif tmp == self.head and self.head.value == num: 
self.head = tmp.next 
elif tmp.next.next == None: 
tmp.next = None 
self.last = tmp 
else: 
tmp.next = tmp.next.next 

def NumberToList(self, num): 
if num == 0: 
self.add(0) 
else: 
while num != 0: 
self.add(num % 10) 
num //= 10 

if __name__ == "__main__": 
p = MyList() 
p.add(1) 
p.add(2) 
print(p) 
p.delete(1) 
p.add(4) 
print(p) 
p.delete(100) 
p.delete(2) 
p.delete(4) 
p.delete(2) 
print(p) 

listik = MyList() 
listik.NumberToList(1234) 
print(listik)

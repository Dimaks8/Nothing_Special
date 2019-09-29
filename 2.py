from 1 import *

def sum(l1,l2):
    listik = MyList()
    x = l1.value + l2.value
    listik.add(x % 10)
    x //= 10
    while l1.next != None:
        l1 = l1.next
        if l2.next != None:
            l2 = l2.next
            tmp = x + l1.value + l2.value
            listik.add(tmp % 10)
            x = tmp // 10
        else:
            tmp = x + l1.value
            listik.add(tmp % 10)
            x = tmp // 10
    else:
        while l2.next != None:
            l2 = l2.next
            tmp = x + l2.value
            listik.add(tmp % 10)
            x = tmp // 10
        if x > 0:
            listik.add(1)
    return listik
    
    
if __name__ == "__main__":
    p1 = MyList()
    p1.NumberToList(5678)
    p2 = MyList()
    p2.NumberToList(4567)
    print(p1)
    print(p2)
    print(sum(p1.head, p2.head))

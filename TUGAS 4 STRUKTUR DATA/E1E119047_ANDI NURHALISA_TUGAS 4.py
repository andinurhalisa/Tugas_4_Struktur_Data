class empty(Exception):
    pass

class array_stack:
    def __init__(self):
        self._data=[]

    def len(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data)==0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise empty("Stack Is Empty")
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise empty("Stack Is Empty")
        return self._data.pop()

def reverse_file(filename):
    S=array_stack()
    original = open(filename)
    for line in original:
        S.push(line.rstrip("\n"))
    original.close()

    output=open(filename, "w")
    while not S.is_empty():
        output.write(S.pop() + "\n")
    output.close()

    ofile=open (filename, "r")
    k=ofile.readlines()
    for i in k:
        print(i.rstrip())

def is_matched(expr):
    lefty="({[" #opening delimiters
    righty=")}]" #respective closing delims
    S=array_stack ()
    for c in expr:
        if c in lefty:
            S.push(c) #push left delimiter on stack
        elif c in righty:
            if S.is_empty():
                return False #nothing to match with
            if righty.index(c) != lefty.index(S.pop()):
                return False #mismatched
    return S.is_empty()

active=True

while active:
    print("\nMenu Pilihan : \n 1. Reverse File \n 2. Matching Delimiters \n 3. Keluar")
    pilihan=int(input("Masukan menu pilihan : "))
    if pilihan==1:
        nama_file=input ("Masukan Nama File : ")
        print(nama_file + ".txt")
        reverse_file(nama_file + ".txt")
    elif pilihan==2:
        expression=input ("Masukan Expression : ")
        match=is_matched (expression)
        if match:
            print("\nSemua Delimeters Cocok dengan baik")
        else:
            print("\nTerdapat Delimettrs yang Tidak Cocok")
    else:
        break

#дескриптор
from random import choice
import re
class IntValue:
    def __set_name__(self, owner, name):
        self.name = "__" + name
    
    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) == int or value is None: 
            setattr(instance, self.name, value)

class RSA:
    p = IntValue()
    q = IntValue()
    def __init__(self):
        self.simple_number = [x for x in range(2, 100) if self.isprime(x)]
        self.p = None
        self.q = None
        self.d = None
        self.e = None
        self.text = ""

    def isprime(self, n):
        return re.compile(r'^1?$|^(11+)\1+$').match('1' * n) is None


    def check_simple_number(self, number):
        return number in self.simple_number
    
    def greatestCommonDivisor(self, i, Pn):
        while i > 0:
            temp = i
            i = Pn % i
            Pn = temp
        return Pn

    def calculateE(self, Pn):
        #Выбирается целое число e ( 1 < i < Pn) взаимно простое со значением функции Эйлера (Pn)
        for i in range(2, Pn):
            if self.greatestCommonDivisor(i, Pn) == 1:
                return i
        return -1

    def calculateD(self, e, Pn):
        #Вычисляется число d, мультипликативно обратное к числу e по модулю φ(n), то есть число, удовлетворяющее сравнению:
        #d ⋅ e ≡ 1 (mod φ(n))
        d = 0
        k = 1
        while True:
            k = k + Pn
            if k % e == 0:
                d = (k // e)
                return d

    def calculate_open_close_key(self):
        self.n = self.p * self.q
        Pn = (self.p - 1) * (self.q - 1)
        #вычисляем открытый ключ
        self.e = self.calculateE(Pn)
        #вычисляем секретный ключ
        self.d = self.calculateD(self.e, Pn)


    @classmethod
    def __hash(cls, lst):
        return sum(bin(numbers).count("1") for numbers in lst)

    def сalculate_signature(self):
        self.h = 0
        lst_numbers = []
        for c in self.text:
            lst_numbers.append(ord(c))
        self.h = self.__hash(lst_numbers)
        if self.h == 0:
            self.h = 1
        self.s = (self.h ** self.d) % self.n
        return self.text, self.s
    
    def check_signature(self):
        h1 = (self.s ** self.e) % self.n
        if self.h == 2:
            return True
        return False


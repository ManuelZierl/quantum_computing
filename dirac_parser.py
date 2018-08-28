import re

from sympy import sqrt


class dirac_parser:
    def __init__(self):
        self.parse("(|0> + |1>)")

    def parse(self, string):
        "6 of(.*)fans"
        pass


class Statement:
    def __init__(self, *x):
        self.xs = [bin(i) for i in list(x)]
        print(self.xs)
        self.amplitudes = [1/sqrt(len(self.xs))]*len(self.xs)

    def __str__(self):
        return "".join(("" if a == 1 else str(a)) + "|" + str(w)[2:] + "> + " for a, w in list(zip(self.amplitudes,self.xs)))[:-3]

    def permutations(self):
        # -> to all possible permutations and there amplitudes

        pass

    def bitwise(self):
        pass

    def __add__(self, other):
        return Statement(*(self.xs + other.xs))

class Statement_2:
    def __init__(self, length, init=None): # todo init wih parser string
        self.length = length
        if init is None:
            self.amplitudes = [(1,0)]*self.length
        else:
            if len(self) != len(init):
                raise Exception("Wrong length")
            self.amplitudes = init
        print(self.amplitudes)

    def __mul__(self, other):
        return Statement_2(len(self) + len(other), init=self.amplitudes + other.amplitudes)

    def __len__(self):
        return self.length

    def show_detailed(self):
        out = ""
        op = False
        for ampl in self.amplitudes:


            if ampl[0] == 1 and ampl[1] == 0:
                if op == False:
                    out += "|"
                out += "0"
                op = True
                continue

            if ampl[0] == 0 and ampl[1] == 1:
                if op == False:
                    out += "|"
                out += "1"
                op = True
                continue

            if op == True:
                out += ">  "

            out += str(ampl[0]) + "|0> + " + str(ampl[1]) + "|1>   "
            op = False

        out += ">"
        if out.replace(" ", "")[-2:] == ">>":
            out = out[:-1]
        print(out)






s1 = Statement_2(6)
s1.show_detailed()
s2 = Statement_2(6)
s2.amplitudes = [(0,1)]*6
s2.show_detailed()

s3 = s1*s2

s3.show_detailed()
#print(0b11110%4)
#s_1 = Statement(40,30)
#print(s_1)
#
#print(1/sqrt(2)*0 + 1/sqrt(2)*1)
#
#print("x" if 1 == 0 else "z")
#s_1 = State(2)
#s_2 = State(5)
#
#print(s_1+s_2)
#

# s = "|1> + |22>"
# match = re.findall(r'\|[\d]*\>', s)
# print(match)



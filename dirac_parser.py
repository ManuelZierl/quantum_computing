import re


class dirac_parser():
    def __init__(self):
        self.parse("(|0> + |1>)")

    def parse(self, string):
        "6 of(.*)fans"
        pass


class Statement:
    # concat of ors
    def __init__(self, *x):
        self.x = list(x)

    def __str__(self):
        return "".join("|" + str(w) + "> + " for w in self.x)[:-3]

    def __add__(self, other):
        return Statement(*(self.x + other.x))

s_1 = Statement(1)
s_2 = Statement(2)
s3 = s_1 + s_2 + s_1

print(s3 + s3)

#s_1 = State(2)
#s_2 = State(5)
#
#print(s_1+s_2)
#

# s = "|1> + |22>"
# match = re.findall(r'\|[\d]*\>', s)
# print(match)



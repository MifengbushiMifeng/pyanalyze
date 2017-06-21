class Cls(object):
    cls_var = 1

    def __init__(self):
        self.ins_var = 2
        self.cls_var = 4


ins1 = Cls()
ins2 = Cls()

ins1.cls_var = 20
# ins2.cls_var = 30

print(Cls.cls_var)
print(ins1.cls_var)
print(ins2.cls_var)

Cls.cls_var = 11

print(Cls.cls_var)
print(ins1.cls_var)
print(ins2.cls_var)
# print('----------------------')
# cls.cls_var = 10#

# print(cls.cls_var)
# print(ins1.cls_var)
# print(ins2.cls_var)

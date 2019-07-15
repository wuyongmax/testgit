# from types import MethodType,FunctionType
#
# class Foo(object):
# 	def fetch(self):
# 		pass
#
# # print(isinstance(Foo.fetch,MethodType))
# # print(isinstance(Foo.fetch,FunctionType)) # True
#
# obj = Foo()
# print(isinstance(obj.fetch,MethodType)) # True
# print(isinstance(obj.fetch,FunctionType))


from functools import partial
def test(x,y,z):
    return x+y+z
test=partial(test,1)
print(test(2,3))
# print(test(1,2,3))
print('asbfasiu ***************')
print("adddasldkjas;")

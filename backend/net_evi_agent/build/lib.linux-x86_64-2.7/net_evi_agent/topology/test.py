#!/usr/bin/python3
class A:
	def __init__(self,name,sex):
		self.name=name
		self.sex=sex
	def printInfo(self):
		print (self.name+self.sex)
class B(A):
	def __init__(self,name,sex):
		A.__init__(self,name,sex)

a=A("WEX","GRIL")
b=B("HTL","BOY")

a.printInfo()
b.printInfo()

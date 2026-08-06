
# class product:
#     def show(self):
#         print('this name of product',self.name)
#         print('the price of product',self.price)
#
#
#
# class IIT(product):
#     def show(self):
#         super().show()
#         print('welcome to IIT mumbai')
#
#
#
# obj = IIT()
# obj.name='mobile'
# obj.price=30000
# obj.show()

#OVERLOADING METHOD

# class student:
#     def display(self):
#         print('welcome')
#
#     def display(self,name=''):
#         print('name',self.name)
#
#     def display(self,address=''):
#         print('address',self.address)
#
#
#
#
# obj = student()
# obj.display()
# obj.display('mukesh')
# obj.display('kolkata')


# Overradding method as Runtime polymorphism

# class product:
#     def display(self):
#         print('the name of product',self.name)
#         print('the price of product',self.price)
#
#
#
# class IIT(product):
#     def display(self):
#         print('welcome to IIT Mumbai')
#         super().display()
#
#
# obj = IIT()
# obj.name='laptop'
# obj.price=9021
# obj.display()

# Overloading method as Compiletime polymorphism

# class student:
#     def show(self):
#         print('this is very good student')
#
#     def show(self,name=''):
#         print('name',self.name)
#
#     def show(self,id):
#         print('the id',self.id)
#
#
# class IIT(student):
#     def show(self):
#         print('welcome to IIT delhi')
#
# obj = IIT()
# obj.name='mohit'
# obj.id=4356
# obj.show()
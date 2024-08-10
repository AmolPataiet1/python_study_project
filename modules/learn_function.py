#
# x= "Awesome"  #Global variable
# def myfunc():
#     x="Fantastic"  #//local varibale
#     global x
#     print("Python is", x)
#
# # myfunc()
# print("Python is", x)

#====================

# use global keyword,

def myglobfunc():
    global x
    x="Awesome & fantastic"

myglobfunc()
print("Python is " + x)
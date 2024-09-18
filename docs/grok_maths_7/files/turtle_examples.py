import turtle as t

t.shape("turtle")
t.speed(2)

# """square 100"""
# t.seth(0)
# for _ in range(4):
#     t.fd(100)
#     t.rt(90)


# '''rectangle w=30, h = user input'''
# t.seth(0)
# height = int(input('Height: '))
# width = 30
# t.lt(90)
# for _ in range(2):
#     t.fd(height)
#     t.rt(90)
#     t.fd(width)
#     t.rt(90)


# """triangle 100"""
# t.seth(0)
# for _ in range(3):
#     t.fd(100)
#     t.lt(120)


# '''protractor angle'''
# angle = int(input('How many degrees? '))

# t.fd(100)
# t.bk(100)
# t.lt(angle)
# t.fd(100)
# t.bk(100)

# '''house'''
# # roof
# t.seth(0)
# for _ in range(3):
#     t.fd(100)
#     t.lt(120)
# t.rt(90)
# # base
# for _ in range(3):
#     t.fd(100)
#     t.lt(90)


import turtle as t

size = int(input('House length? '))
# roof
t.seth(0)
for _ in range(3):
    t.fd(size)
    t.lt(120)
t.rt(90)
# base
for _ in range(3):
    t.fd(size)
    t.lt(90)

# This will keep the window open until you manually close it
t.done()
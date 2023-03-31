print("____________")
print("")
print("")
print("")
print("")
print("")


neco = input("zadejte text: ")
print("")

lenghtOfNeco = len(neco)

anotherNeco = 1

for x in range(lenghtOfNeco):
    print(neco[len(neco) - anotherNeco], end="")
    anotherNeco += 1

print("")
print("")
print("")
print("")
print("")
print("____________")
    



































































# import turtle as t

# # for x in range(10):
# #     for x in range(4):
# #         t.fd(10)
# #         t.lt(90)
# #     t.fd(10)

# t.speed(10)

# lenght = 10

# for x in range(10):
#     for x in range(10):
#         for x in range(4):
#             t.fd(10)
#             t.lt(90)
#         t.fd(10)
#     t.penup()
#     t.home()
#     t.pendown()
#     t.lt(90)
#     t.fd(lenght)
#     t.rt(90)
#     lenght += 10
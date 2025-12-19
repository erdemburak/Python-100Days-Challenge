
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Ad", "Yaş", "Meslek"]

table.add_row(["Burak", 30, "Developer"])
table.add_row(["Armağan", 28, "Psikolog"])

table.align = "l" # "l" "r" "c" ile tabloda konumlandırma işlemi yapılabilir

print(table)
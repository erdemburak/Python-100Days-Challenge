import turtle 
import pandas

screen = turtle.Screen()
screen.title("Türkiye City Game")

image = "turkey_city_game/turkey_empty_map.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=1200, height=651)

city_data = pandas.read_csv("turkey_city_game/81_city.csv")
all_city = city_data.city.to_list()
guessed_cities = []

while len(guessed_cities) < 81:
    answer_city = screen.textinput(title=f"{len(guessed_cities)}/81 City Correct", prompt="What's another city's name?").title()

    if answer_city == "Exit":
        missing_cities = [city for city in all_city if city not in guessed_cities]
        new_data = pandas.DataFrame(missing_cities)
        new_data.to_csv("cities_to_learn.csv")
        break
    if answer_city in all_city:
        guessed_cities.append(answer_city)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        cities = city_data[city_data.city == answer_city]
        t.goto((cities.x.item() - 10), cities.y.item())
        t.write(cities.city.item())

# Aşağıdaki kod ekranda tıklanan konumun koordinatını yazıyor
# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()
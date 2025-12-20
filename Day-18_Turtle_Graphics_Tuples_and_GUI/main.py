#from turtle import Turtle as T
from turtle import Turtle, Screen

# Python'ın default paketinde tüm kütüphaneler yok bu sebeple kullanılacak kütüphaneleri dışarıdan eklememiz gerek
# Bunun için projeye özgü sanal ortam oluşturuyoruz venv 
# python3 -m venv "proje dosya adresi"/venv ve tamam 
# pip install "libraryName" ile kullanacağımız kütüphaneyi ekleyebiliriz.
# indirilen kütüphane bu proje dosyasında oluşturulan venv için geçerli olacak başka bir projede aynı işlem tekrarlanmalı
import heroes 
import villains

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red","orange")

for i in range(4):
    timmy_the_turtle.right(90)
    timmy_the_turtle.forward(100)

screen = Screen()
screen.exitonclick()


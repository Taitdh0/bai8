print ("Tran Tuan Tai")
print("235752021610014")
import turtle

t = turtle.Turtle()

t.speed(2)

colors = ["blue", "cyan", "red"]

for i in range(12):
    t.color(colors[i % 3]) 
    t.circle(50)        
    t.right(30)            

turtle.done()


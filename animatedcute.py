import turtle

def draw_heart():
    # Setup window and pen
    window = turtle.Screen()
    window.bgcolor("#fff0f3")
    window.title("A Little Message for You... 💕")
    
    t = turtle.Turtle()
    t.color("#ff4d6d")
    t.fillcolor("#ff758f")
    t.pensize(5)
    t.speed(3)
    
    # Draw heart shape
    t.begin_fill()
    t.left(140)
    t.forward(180)
    t.circle(-90, 200)
    
    # Left curve
    t.left(120)
    t.circle(-90, 200)
    t.forward(180)
    t.end_fill()
    
    # Move pen to write text below heart
    t.up()
    t.goto(0, -70)
    t.down()
    t.color("#c9184a")
    
    # CUSTOMIZE YOUR MESSAGE HERE!
    t.write("You hold the key to my heart! 🗝️❤️", 
            align="center", font=("Arial", 16, "bold"))
    
    t.hideturtle()
    window.mainloop()

if __name__ == "__main__":
    draw_heart()

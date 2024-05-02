import turtle
import random

screen = turtle.Screen()
screen.title("Space Invaders")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

#punteggio
punteggio= turtle.Turtle()
punteggio.speed(0)
punteggio.color("white")
punteggio.penup()
punteggio.hideturtle()
punteggio.goto(-290, 250)
punti = 0

#livelli
barra_livello= turtle.Turtle()
barra_livello.speed(0)
barra_livello.color("white")
barra_livello.penup()
barra_livello.hideturtle()
barra_livello.goto(290, 250)

#VITE
contatore_vite=turtle.Turtle()
contatore_vite.speed(0)
contatore_vite.color("white")
contatore_vite.penup()
contatore_vite.hideturtle()
contatore_vite.goto(290,250)

#scritta YOU LOSE
YouLose = turtle.Turtle()
YouLose.speed(0)
YouLose.color("red")
YouLose.penup()
YouLose.hideturtle()
YouLose.goto(0,0)

#scritta YOU WIN
YouWin=turtle.Turtle()
YouWin.speed(0)
YouWin.color("green")
YouWin.penup()
YouWin.hideturtle()
YouWin.goto(0,0)



player=turtle.Turtle()
player.shape("triangle")
player.color("green")
player.penup()
player.speed(0)
player.goto(0,-250)
player.setheading(90)

#movimento (dx e sx)
player_speed = 20
def move_left():
    x= player.xcor()
    x -= player_speed
    if x < -290:
        x=-290
    player.setx(x)
    
def move_right():
    x= player.xcor()
    x += player_speed
    if x > 290:
        x= 290
    player.setx(x)
    
#sparare
bullet_speed = 2
def shoot_bullet():
    global state
    if state == "pronto":
        state = "sparo"
        x= player.xcor()
        y= player.ycor()
        bullet.setposition(x,y)
        bullet.showturtle()
        

screen.listen()
screen.onkey(move_right, "Right")
screen.onkey(move_left, "Left")
screen.onkey(shoot_bullet, "space")



def aggiorna_punteggio():
    punteggio.clear()
    punteggio.write("PUNTI : {}". format(punti), align= "left", font=("courier",  12, "normal"))
    
    

    
    
level=1
def aggiorna_livello():
    barra_livello.clear()
    barra_livello.write("LIVELLO {}". format(level), align= "right", font=("courier",  12, "normal"))




nInvaders = 5
invaders=[]
for _ in range(nInvaders):
    invader= turtle.Turtle()
    invader.shape("square")
    invader.color("white")
    invader.penup()
    invader.speed(0)
    y= random.randint(70,150)
    x= random.randint(-290,290)
    invader.goto(x,y)
    invaders.append(invader)

invader_speed = 2

def move_invaders():

    for invader in invaders:
        y = invader.ycor()
        y -= invader_speed
        invader.sety(y)
        
        if player.distance(invader) < 15:
           bullet.hideturtle()
           player.hideturtle()
           YouLose.write("YOU LOSE", align= "center", font=("Courier", 30, "normal"))
           
           for i in invaders:
               i.hideturtle()


            
        if y< -290:
            bullet.hideturtle()
            player.hideturtle()
            YouLose.write("YOU LOSE", align= "center", font=("Courier", 30, "normal"))
            for i in invaders:
                i.hideturtle()
            
    screen.update()
    screen.ontimer(move_invaders, 100)




move_invaders()          

            



#proiettile
bullet=turtle.Turtle()
bullet.shape("square")
bullet.color("green")
bullet.penup()
bullet.speed(10)
bullet.shapesize(stretch_wid=0.5, stretch_len = 0.5)
bullet.hideturtle()
state= "pronto"

aggiorna_punteggio()
aggiorna_livello()

target=50

while True:
    if state== "sparo":
        y= bullet.ycor()
        y += bullet_speed
        bullet.sety(y)
        
        for invader in invaders:
            if bullet.distance(invader) <= 10:
                bullet.hideturtle()
                state = "pronto"
                x = random.randint(-290, 290)
                y = random.randint(70, 150)
                invader.goto(x, y)
                punti += 10
                aggiorna_punteggio()
                
                if punti == target:
                    level +=1 
                    target += 50
                    aggiorna_livello()
                    
                if level ==100:
                    YouWin.write("YOU WIN", align= "center", font=("Courier", 30, "normal"))
                    player.hideturtle()
                    bullet.hideturtle()
                    
                    for i in invaders:
                        i.hideturtle()

                
                
            if y > 290:
                bullet.hideturtle()
                state = "pronto"
                

                
          

    screen.update()
    
    
    


#I-D
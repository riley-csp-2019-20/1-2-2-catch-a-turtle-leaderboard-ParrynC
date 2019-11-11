# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random
import leaderboard as lb 


#-----game configuration----
turtleshape= "turtle"
trtlcolor= "crimson"
trtlsize= random.choice([0.5, 2, 4, 6, 8, 10])
score = 0

#scoreboard variables
leaderboard_file_name="a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input("please enter your name")


font_setup = ("papyrus", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False

counter = trtl.Turtle()
counter.ht()
counter.penup
counter.goto(200, 275)




#-----initialize turtle-----
cocojumbo = trtl.Turtle(shape=turtleshape)
cocojumbo.color(trtlcolor)
cocojumbo.shapesize(trtlsize)
cocojumbo.speed(100)

scortle = trtl.Turtle()
scortle.penup()
scortle.goto(-300, 50)
scortle.ht()
font_setup= ("papyrus", 30, "bold")
scortle.write(score, font=font_setup)

#-----game functions--------
def cocojumbo_clicked(x,y):
    print("cocojumbo was clicked")
    change_position()
    update_score()
    trtlsize = random.choice([0.5, 2, 4, 6, 8, 10])

def change_position():
    cocojumbo.penup()
    cocojumbo.ht()
    if not timer_up:
        cocojumbox = random.randint(-400, 400)
        cocojumboy = random.randint(-300, 300)
        cocojumbo.goto(cocojumbox, cocojumboy)
        cocojumbo.st()

def update_score():
    global score
    score += 1
    print(score)
    scortle.clear()
    scortle.write(score, font=font_setup)
    

def cocojumbo_clicked(x,y):
    print("you got a point")
    change_position()
    update_score()
   

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font = font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)


# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global cocojumbo

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, cocojumbo, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, cocojumbo, score)


#-----events----------------
wn = trtl.Screen()
cocojumbo.onclick(cocojumbo_clicked)
wn.ontimer(countdown, counter_interval)
wn.mainloop()
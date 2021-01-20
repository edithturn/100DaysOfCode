![exercise](../img/reeborg03.png) 

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    while wall_on_right() == True:
        move()
    turn_right()
    move()
    turn_right()
    while wall_in_front() == False:
        move()
    turn_left()

while at_goal() == False:
    if wall_in_front() == True:
        turn_left()
        jump()
       
    else:
        move()
```
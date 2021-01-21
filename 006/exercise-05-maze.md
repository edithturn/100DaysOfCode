![exercise](../img/reeborg04.png) 


```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()
   
while at_goal() == False:
        if right_is_clear() == True:
            turn_right()
            move()
        elif wall_in_front() == True and wall_on_right() == True:
            turn_left()
        else:
            move()
```
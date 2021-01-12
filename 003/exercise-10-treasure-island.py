print('''
           .                .                    
            :"-.          .-";                    
            |:`.`.__..__.'.';|                    
            || :-"      "-; ||                    
            :;              :;                    
            /  .==.    .==.  \                    
           :      _.--._      ;                   
           ; .--.' `--' `.--. :                   
          :   __;`      ':__   ;                  
          ;  '  '-._:;_.-'  '  :                  
          '.       `--'       .'                  
           ."-._          _.-".                   
         .'     ""------""     `.                 
        /`-                    -'\                
       /`-                      -'\               
      :`-   .'              `.   -';              
      ;    /                  \    :              
     :    :                    ;    ;             
     ;    ;                    :    :             
     ':_:.'                    '.;_;'             
        :_                      _;                
        ; "-._                -" :`-.     _.._    
        :_          ()          _;   "--::__. `.  
         \"-                  -"/`._           :  
        .-"-.                 -"-.  ""--..____.'  
       /         .__  __.         \               
      : / ,       / "" \       . \ ; bug          
       "-:___..--"      "--..___;-"               
                                                  

''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

cursor = input("Left or Right?").lower()

if cursor == "left":
  print("You are into a Castell")
  cursor = input('First Floor (type: FF) or Second Floor (type: SF) \n').lower()
  if cursor == "sf":
    cursor = input("Which door?").lower()
    if cursor == "one":
      print("Burned by fire. Game Over!")  
    elif cursor == "two":
      print("Eating by big spiders. Game Over!")
    else:
      print("You Win! :) ")
  else:
    cursor = input("Take treasure: Yes or Not?").lower()
    if cursor == "yes":
      print("This is a trap. Game Over!")
    else:
      cursor = input("Take the diamond, Yes or Not").lower()
      if cursor == "yes":
        print("You Win!")
      else:
        print("You have no lives left. Game Over!")
else:
  print("Fall into a hole. Game Over!")
# ASL Robotics Project

---

This is a college course robotics project. Its purpose is to learn more about robotics, AI, mobility, computer vision, and decision making.

## mobility.py

---

Contains the Mobility class that controls the hardcoded movements of the bot with an OOP paradigm.

**Parameters**  
`l_forward` &rarr; The pin number that controls the left forward motor  
`r_forward` &rarr; The pin number that controls the right forward motor  
`l_reverse` &rarr; The pin number that controls the left reverse motor  
`r_reverse` &rarr; The pin number that controls the right reverse motor  
`l_velocity` &rarr; The pin number that controls the left velocity motor  
`r_velocity` &rarr; The pin number that controls the right velocity motor  

**Functions**
`forward` &rarr; Moves the bot forward  
`backward` &rarr; Moves the bot backward  
`turn_right` &rarr; Turns bot 90 degrees to the right  
`turn_left` &rarr; Turns bot 90 degrees to the left  
`motor_test` &rarr; Tests each wheel motor in turn  
`clean_up` &rarr; Cleans up all the GPIO pins (should be updated to only clean motor pins)  
`reset_pins`&rarr; Allows new pins to be used for motors  

# ASL Robotics Project

---

This is a college course robotics project. Its purpose is to learn more about robotics, AI, mobility, computer vision, and decision making.

## Requirements  

**RPi.GPIO Module**: The mobility.py was designed with a Raspberry Pi in mind. If you intend to use this without a Pi, you will need to find a workaround for this package.  

**Raspberry Pi**: This project was developed and tested using Raspberry Pi OS for the mobility testing,  

**Skid-Steer Mobile Robot**: We used the Yahboom Raspberry Pi G1 Tank when designing and testing this project. 


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
`go_right` &rarr; Moves the bot to the right  
`go_left` &rarr; Moves the bot to the left  
`square` &rarr; Moves the bot in a square pattern   
`spin` &rarr; Moves the bot in a spin pattern  
`motor_test` &rarr; Tests each wheel motor in turn  
`clean_up` &rarr; Cleans up all the GPIO pins (should be updated to only clean motor pins)  
`reset_pins`&rarr; Allows new pins to be used for motors  

## mobility_test.py
---

Creates a mobility object based on the hardcoded GPIO numbers and allows the user to input a letter to test the movements.  

**Commands**  
`test` &rarr; Runs the motor_test function to test each motor.  
`x` &rarr; Exits the program  
`f` &rarr; Runs forward function  
`b` &rarr; Runs backward function  
`l` &rarr; Runs go_left function  
`r` &rarr; Runs go_right function  
`c` &rarr; Runs the square function  
`s` &rarr; Runs the spin function  

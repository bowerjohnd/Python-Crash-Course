# Python Crash Course - Alien Invasion

**Chapter 12**  
 - Planning: Alien Invasion 
   - Player controls a rocket ship at the bottom of the screen
     - Move left and right using arrow keys
     - Shoot bullets using the space bar
   - When the game begins, a fleet of aliens appear
     - Aliens move across and down the screen
   - Gameplay
     - Player shoots and destroys aliens
     - All aliens destroyed, a new fleet of aliens appear
       - Each new fleet moves faster than previous fleet
     - Player loses a ship if:
       - An alien touches the player's ship
       - An alien reaches the bottom of the screen
     - Game ends when the player loses 3 ships

 - Coding: Alien Invasion
   - Set up game screen
     - Pygame
     - Create settings module for fine tuning
   - Ship image on screen
   - Move ship left and right
     - prevent ship from moving off screen
   - Bullets fired from ship
     - remove bullets from group when off screen
   - Misc. settings tuning
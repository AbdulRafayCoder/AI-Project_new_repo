**ARTIFICIAL INTELLIGENCE FINAL PROJECT**


**WORKING OF THE GAME:** 
Street Fighter is a classic PvP game back from the 1980s. The game has 12 playable characters, each with unique set of moves and skills. The player can play against CPU or another player. Our project was to create a
Machine Learning based model, that will play the game and win matches. This project becomes a learning block for understanding how data is generated and handled before being used in a ML model. Also how to create
a model script that will predict and perform actions based on the data. 

![image](https://github.com/user-attachments/assets/70e0a59a-0afe-4bd1-9bd0-d4f008bbbb00)

![image](https://github.com/user-attachments/assets/9275f895-8978-4932-a4d1-c1a665f50a15)

![image](https://github.com/user-attachments/assets/9e203951-9bb7-477c-9cad-5fb3b50b2134)



**SETUP:** 
The game was to be played using EmuHawk Emulator. The game was reflected using the SNES controller in which players can hit: 
  1. Heavy moves(W and E on the keyboard)
  2. Medium Attacks(Z and X)
  3. Light attacks(A and S)
  4. Arrow keys to control the character.
  5. Any combination of these to make special moves.

**DATA GENERATION:**
For any Machine Learning model, it is necessary to have the right amount of data. And not just data, but properly labelled data. Initially we played games and got data similar to sample data set provided. 
But after 4 times generating data from scratch and using a hit and trial approach, we finally found the perfect attributes(labels) needed to train the model. 

**Initial Labels:** timer	fight_resul, has_round_started, is_round_over, Player1_ID	health, x_coord, y_coord, is_jumping, is_crouching, is_player_in_move	move_id, player1_buttons_up, player1_buttons down	
player1_buttons right, player1_buttons left, Player2_ID	Player2 health, Player2 x_coord, Player2 y_coord, Player2 is_jumping, Player2 is_crouching, Player2 is_player_in_move, Player2 move_id, player2_buttons up	
player2_buttons down, player2_buttons right, player2_buttons left

**Final Labels:** timer, has_round_started, is_round_over, Player1_ID, Player1_health, Player1_x, Player1_y, Player1_up, Player1_down, Player1_right, Player1_left, Player1_Y, 
Player1_B, Player1_X, Player1_A, Player1_L, Player1_R, Player1_in_move, Player1_move_id, Player1_jumping, Player1_crouching, Player2_ID, Player2_health, Player2_x, Player2_y, 
Player2_up, Player2_down, Player2_right, Player2_left, Player2_Y, Player2_B, Player2_X, Player2_A, Player2_L, Player2_R, Player2_in_move, Player2_move_id, Player2_jumping, Player2_crouching


After the hit and trial method and finding the perfect labels, we generated extensive amount of data by playing the game ourselves. 

**HOW DATA WAS GENERATED?**
We generated the data using pynput library, recording each action of the user. The reason for playing the game ourselves was to generate better quality data. If the functionality of bot.py file was used, 
then we would have gotten random data with no cohesion or logic. So we played the game ourselves so that the bot will mimic human behaviour and preferably win games(which it is winning). 

![image](https://github.com/user-attachments/assets/0cb43811-beeb-44a1-872d-a17a3749c2fb)



**CODE OF USER INPUT**


**Libraries** 

![image](https://github.com/user-attachments/assets/93de7055-d204-4f6d-96a9-4c077e78e96b)


**Key Press Logic**

![image](https://github.com/user-attachments/assets/ef94ed71-f52e-48f9-b5bc-6796eef618ab)


**Connection with emulator**

![image](https://github.com/user-attachments/assets/b8c9a528-d142-4412-9f4f-cd65102e0b86)


**OUR MODEL**

The model we have used is Random Forest Classifier. It predicts the next set of actions for the Player based on the current game state and player 2 actions. 

**Key steps:**

**Data Loading:** It reads gameplay data from trainData3.csv, which contains positions, health values, and button presses for both players.

**Extra Features:** New features like health difference and distances between players are computed to help the model understand game context better.

**Inputs:** Game state variables and Player 2's actions.

**Outputs:** Predicted button presses for Player 1 (like up, down, A, B, etc.).

**Model:** A RandomForestClassifier wrapped in MultiOutputClassifier is used to handle multiple action predictions at once.

**Evaluation:** The model's performance is measured using classification metrics and exact match accuracy (how often the entire predicted set matches the actual actions)

**Libraries**

![image](https://github.com/user-attachments/assets/b726e75d-51b2-47e5-9f10-5ae349349208)


**Data Pre-processing**

![image](https://github.com/user-attachments/assets/e17d6317-347b-44d0-9923-5772f106c3ec)


**Prediction Logic**

![image](https://github.com/user-attachments/assets/dd33169d-9f29-4a0c-a2ce-4338ff2ecea3)



**CONCLUSION**

All of our group members agree on the fact that this project was really helpful in learning the pre-requisites of any model. This project will prove to be our basis for further ML and AI courses. In the end, we have successfully developed a model that predicts moves, performs logical actions and wins games often. We are proud of our work and hope that this project learning will be the stepping stone for next projects. 

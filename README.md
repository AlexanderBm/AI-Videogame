# Boss AI Training Game

## Game Description

In the game, the player and boss characters have their own attributes and actions:

- **Player**: The player character has 10 health points (HP) and can deal 10-20 damage per turn. The player can also be stunned, preventing it from dealing damage on its next turn.
  
- **Boss**: The boss character has 30 health points (HP) and two different kinds of attacks:
    - Basic Attack: Deals 2-7 damage.
    - Stun Attack: Always deals 1 damage but stuns the player, preventing it from attacking on its next turn.

The boss's strategy is to choose between these two attacks based on probabilities. Initially, the boss chooses attacks randomly, but it learns to optimize its strategy through machine learning training.

## Training Process

The boss AI is trained using a machine learning model, specifically a recurrent neural network (RNN) implemented using TensorFlow and Keras. The training process involves the following steps:

1. **Data Generation**: The game is simulated multiple times, with the boss playing against the player. The game states and actions taken by both characters are recorded as training data.

2. **Model Training**: The training data is used to train the machine learning model. The model learns to predict the boss's optimal strategy based on the current game state.

3. **Model Evaluation and Refinement**: The trained model is evaluated by playing against the player character. The model's performance is analyzed, and if necessary, the model is refined and retrained with additional data.

4. **Convergence**: The training process continues until the boss AI converges to a strategy that maximizes its chances of winning against the player.

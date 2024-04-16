## Pet Simulator Documentation
github: https://github.com/SamAdams1/VirtualPetOOP

### Introduction
The Pet Simulator is a virtual pet simulation game developed using the Pygame library in Python. In this game, players can interact with virtual pets, take care of their needs, navigate through different rooms, and participate in various activities to keep their pets happy and healthy.

### Design Choices
The Pet Simulator is designed to provide an engaging and interactive experience for players while simulating the responsibilities of owning a pet. Here are some key design choices:

1. **Pygame Framework**: Pygame is chosen as the framework for developing the game due to its simplicity and suitability for 2D game development in Python.

2. **Object-Oriented Design**: The game is designed using object-oriented principles to encapsulate entities such as pets, buttons, health bars, and rooms as objects with defined behaviors and attributes.

3. **Modular Structure**: The codebase is organized into modules for better maintainability and readability. Modules such as `gui`, `pet`, and `src` contain related functionalities grouped together.

4. **User Interaction**: The game utilizes mouse input for interaction with buttons and user interface elements. Players can navigate through rooms, interact with their pets, and perform actions by clicking on buttons.

### Data Structures
1. **Doubly Linked List**: Used to implement navigation between rooms. Each room is represented as a node in the doubly linked list, allowing for easy traversal forward and backward.

2. **Dictionary**: Dictionaries are extensively used to store information such as pet data, save data, room functions, and tutorial messages. They provide efficient lookup and manipulation of key-value pairs.

### Algorithms Used
1. **Timers**: Timers are implemented using Pygame's `get_ticks()` function to measure elapsed time. Timers are used to update pet stats periodically and trigger events such updating the pets stats.

2. **Random Events**: Random events are simulated using a random number generator. These events occur based on predefined probabilities and can impact the pet's status or trigger specific actions.

### Interacting with the Pet Simulator
To interact with the Pet Simulator, players use mouse input to navigate menus, interact with buttons, and perform actions. Here's a basic guide on how to interact with the game:

1. **Starting the Game**: Upon launching the VirtualPet.exe, players are presented with a start menu.

2. **Choosing a Pet**: After starting the game, players can choose a pet from three available options: blue, yellow, or red bird. Click on the desired bird and click the "Enter" button to select it as your pet.

3. **Naming Your Pet**: Once a pet is selected, players can enter a name for their pet. Type the desired name into the text box and click the "Enter" button to confirm.

4. **Taking Care of Your Pet**: Players navigate through different rooms using the left and right arrow buttons. Each room corresponds to a different aspect of the pet's well-being (e.g., bedroom for sleep, kitchen for feeding). Click on the buttons in each room to perform actions such as feeding, washing, or playing with the pet.

5. **Monitoring Pet Stats**: Keep an eye on the pet's health, hunger, cleanliness, energy, and mood bars displayed on the screen. Ensure that these bars stay within healthy ranges by taking appropriate actions in each room.

6. **Dealing with Random Events**: Occasionally, random events may occur, such as the pet running away or losing its toy. Handle these events by following the on-screen instructions.

7. **Saving Progress**: The game automatically saves progress when exiting. Players can continue their game from where they left off the next time they launch the game.

8. **Exiting the Game**: To exit the game, simply click the close button on the window.
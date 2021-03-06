from .state import State
from .gamescreen import GameScreen


class StateManager:

    def __init__(self, window, state: State):
        self.window = window
        self.currentState = state

    def changeState(self, state: State):
        """
        Switch states
        :param state: The next state to show
        :return: None
        """
        self.exit()
        self.currentState = state
        self.start()

    def update(self):
        self.currentState.update()

    def fixedUpdate(self):
        self.currentState.fixedUpdate()
        pass

    def start(self):
        self.currentState.window = self.window  # Give the state a reference to the window
        self.currentState.loadUi()  # Load the states UI
        self.window.gameScreen = self.window.findChild(GameScreen)
        self.currentState.start()  # Start the state
        pass

    def exit(self):
        self.currentState.exit()
        pass

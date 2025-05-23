import qiskit
import qiskit_aer
import pygame

class Computer:
    def __init__(self):
        pass
    def update(self):
        pass

class ClassicalComputer(Computer):
    def __init__(self, paddle):
        self.paddle = paddle
        self.score = 0
        # How fast classical computer is 
        self.speed = 3
    
    def update(self, ball):
        # Uses centery rather y because because y in rectangle is top left we want center
        if self.paddle.rect.centery - ball.rect.centery > 0:
            self.paddle.rect.y -= self.speed
        else: # If paddle is above the ball then do the opposite
            self.paddle.rect.y += self.speed
        
        if pygame.sprite.collide_mask(ball, self.paddle):
            ball.bounce()

class QuantumComputer(Computer):
    def __init__(self, quantum_paddles, circuit_grid):
        # quantum_paddles.paddles is a list of sprite paddles
        self.paddles = quantum_paddles.paddles
        self.score = 0
        self.circuit_grid = circuit_grid

    def update(self, ball):
        # Will simulate a quantum circuit
        simulator = qiskit_aer.StatevectorSimulator(precision='single')
        # We will use this circuit for the simulator
        circuit = self.circuit_grid.model.compute_circuit()
        # transpile the circuit first
        transpiled_circuit = qiskit.transpile(circuit, simulator)
        # reduces the number of shots so that the game is faster
        statevector = simulator.run(transpiled_circuit, shots=100).result().get_statevector()

        for basis_state, amplitude in enumerate(statevector):
            # amplitude^2 is the probability * 255 ()
            self.paddles[basis_state].image.set_alpha(amplitude**2*255)


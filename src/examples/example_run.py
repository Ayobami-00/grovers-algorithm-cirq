import cirq
from src.grover.grover_algorithm import grovers_algorithm
from src.grover.oracle import grover_oracle

# Create 2 qubits
qubits = [cirq.LineQubit(i) for i in range(2)]

# Create the Grover's algorithm circuit
circuit = grovers_algorithm(qubits, grover_oracle, num_iterations=1)

# Print the circuit
print("Grover's Algorithm Circuit:")
print(circuit)

# Simulate the quantum circuit
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=1000)

# Print the measurement results
print("\nMeasurement results:")
print(result.histogram(key='result'))

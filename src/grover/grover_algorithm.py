import cirq
import numpy as np

def grovers_algorithm(qubits, oracle, num_iterations=1):
    """
    Implements Grover's algorithm for quantum search.

    Parameters:
    qubits: A list of qubits on which the algorithm will be applied.
    oracle: A callable that defines the oracle for Grover's search.
    num_iterations: Number of Grover iterations (default is 1).
    
    Returns:
    circuit: The quantum circuit representing Grover's algorithm.
    """
    # Initialize the circuit
    circuit = cirq.Circuit()

    # Apply Hadamard gates to all qubits
    circuit.append(cirq.H(q) for q in qubits)

    for _ in range(num_iterations):
        # Apply oracle
        circuit.append(oracle(qubits))

        # Apply Grover's diffusion operator
        circuit.append(cirq.H(q) for q in qubits)
        circuit.append(cirq.X(q) for q in qubits)
        circuit.append(cirq.H(qubits[-1]))
        circuit.append(cirq.CNOT(qubits[0], qubits[1]))
        circuit.append(cirq.H(qubits[-1]))
        circuit.append(cirq.X(q) for q in qubits)
        circuit.append(cirq.H(q) for q in qubits)

    # Measure the qubits
    circuit.append(cirq.measure(*qubits, key='result'))

    return circuit

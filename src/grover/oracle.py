import cirq

def grover_oracle(qubits):
    """
    A simple Grover oracle for a 2-qubit system that marks the state |11>.
    
    Parameters:
    qubits: A list of qubits to apply the oracle to.
    
    Returns:
    circuit: The quantum circuit representing the oracle.
    """
    # Apply a Z gate to the second qubit if both are |1>
    circuit = cirq.Circuit()
    circuit.append(cirq.CNOT(qubits[0], qubits[1]))
    circuit.append(cirq.Z(qubits[1]))
    return circuit

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def create_circuit(qubits=1):
    circuit = QuantumCircuit(qubits)
    circuit.rz(0, 0)
    return circuit

def run_simulation(circ):
    simulator = AerSimulator(method='statevector')
    circ.save_statevector()
    result = simulator.run(circ).result()
    return result

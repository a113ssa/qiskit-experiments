from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def create_circuit(qubits=1):
    circuit = QuantumCircuit(qubits)
    qubits_arr = [i for i in range(qubits)]
    circuit.rz(0, qubits_arr)
    return circuit

def run_simulation(circ, method='statevector'):
    simulator = AerSimulator(method=method)
    if method == 'statevector':
        circ.save_statevector()

    result = simulator.run(circ).result()
    return result

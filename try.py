from math import pi

from qiskit import Aer, QuantumCircuit, execute
from qiskit.visualization import plot_bloch_multivector

if __name__ == "__main__":
    qc = QuantumCircuit(2)

    qc.h(0)
    qc.x(1)
    qc.cu1(-pi / 2, 1, 0)

    print(qc.draw("text"))

    final_state = execute(qc, Aer.get_backend("statevector_simulator")).result()

    print(final_state.get_statevector())

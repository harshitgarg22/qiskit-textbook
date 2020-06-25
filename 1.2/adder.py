from qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram


def adder(qc: QuantumCircuit):
    qc.cx(0, 2)
    qc.cx(1, 2)
    qc.ccx(0, 1, 3)


def adder_demo():
    # Here we add |0> and |1> to give |01>.
    qc = QuantumCircuit(4, 2)

    # qc.x(0)
    qc.x(1)
    qc.barrier()
    adder(qc)
    qc.barrier()
    qc.measure(2, 0)
    qc.measure(3, 1)

    qc.draw("mpl", filename="adder.png")

    counts = execute(qc, Aer.get_backend("qasm_simulator")).result().get_counts()
    plot_histogram(counts).savefig("counts.png")


if __name__ == "__main__":
    adder_demo()

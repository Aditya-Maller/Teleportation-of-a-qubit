import streamlit as st

# Q# Code to display
qsharp_code = """
namespace Sample {
    open Microsoft.Quantum.Diagnostics;
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Measurement;

    @EntryPoint()
    operation Main() : Result[] {
        use (message, target) = (Qubit(), Qubit());
        let stateInitializerBasisTuples = [
            ("|0〉", I, PauliZ),
            ("|0〉", I, PauliZ),
            ("|0〉", I, PauliZ),
            ("|0〉", I, PauliZ)
        ];

        mutable results = [];
        
        // Loop to teleport multiple states
        for (state, initializer, basis) in stateInitializerBasisTuples {
            initializer(message);
            Message($"Teleporting state {state}");
            DumpMachine();
            Teleport(message, target);
            Message($"Received state {state}");
            DumpMachine();
            let result = Measure([basis], [target]);
            set results += [result];
            ResetAll([message, target]);
        }
        return results;
    }

    // Teleportation operation
    operation Teleport(message : Qubit, target : Qubit) : Unit {
        use auxiliary = Qubit();
        
        // Entanglement generation
        H(auxiliary);
        CNOT(auxiliary, target);
        CNOT(message, auxiliary);
        H(message);

        // Measurement and conditional gates
        if M(message) == One {
            Z(target);
        }
        if M(auxiliary) == One {
            X(target);
        }

        // Reset the auxiliary qubit
        Reset(auxiliary);
    }
}
"""

# Display Q# Teleportation Code
st.title("Quantum Teleportation: Project Showcase and Deep Dive")
st.write("## Q# Code for Quantum Teleportation Protocol")
st.code(qsharp_code, language="qsharp")

st.write("""
### Code Description:
This Q# program demonstrates **quantum teleportation** using the following steps:
1. **State Initialization**: Prepares qubits for teleportation.
2. **Entanglement Generation**: Entangles an auxiliary qubit with the target qubit using quantum gates.
3. **Bell State Measurement**: Alice measures the message qubit and the auxiliary qubit.
4. **Conditional Corrections**: Based on classical results, Bob reconstructs the state using Pauli gates.
""")

# Add Exploration Section
st.write("## Explore More About Quantum Mechanics and Teleportation")

menu = st.sidebar.radio(
    "Select a Topic to Explore:",
    [
        "Project Code Walkthrough",
        "History of Quantum Mechanics",
        "Current Quantum World",
        "Quantum Math and Notations",
        "Quantum Gates and Operations",
        "Teleportation Steps and Circuitry",
        "Mind-Blowing Quantum Experiments",
        "Theoretical Ideas Yet to Be Proven",
        "RV University and CQST"
    ]
)

# Content Functions
def code_walkthrough():
    st.header("Project Code Walkthrough")
    st.write("""
    - **Main Operation**: Initializes qubits and iteratively teleports states using `Teleport` operation.
    - **Teleport Operation**: 
        1. Generates entanglement.
        2. Performs measurements.
        3. Applies corrections conditionally.
    """)

def history_of_quantum_mechanics():
    st.header("History of Quantum Mechanics")
    st.write("""
    - **1900**: Max Planck proposed quantization of energy.
    - **1925-27**: Schrödinger and Heisenberg formalized quantum mechanics.
    - **1980s**: Feynman envisioned quantum computers.
    """)

def current_quantum_world():
    st.header("The Current Quantum World")
    st.write("""
    Quantum computing is now at the forefront of technological innovation. Key players:
    - **Google**: Quantum supremacy with Sycamore.
    - **IBM**: Offering cloud-based quantum systems.
    """)

def quantum_math_and_notations():
    st.header("Quantum Math and Notations")
    st.write("""
    - **Superposition**: |ψ⟩ = α|0⟩ + β|1⟩.
    - **Dirac Notation**: States are represented as kets (|ψ⟩).
    - **Bloch Sphere**: Visualizes qubit states.
    """)

def quantum_gates():
    st.header("Quantum Gates and Operations")
    st.write("""
    - **Hadamard Gate**: Creates superposition.
    - **CNOT Gate**: Entangles two qubits.
    - **Pauli Gates**:
        - X: Flips |0⟩ ↔ |1⟩.
        - Z: Phase-flip on |1⟩.
    """)

def teleportation_steps():
    st.header("Teleportation Steps and Circuitry")
    st.write("""
    - Step 1: Create entanglement.
    - Step 2: Alice performs measurements.
    - Step 3: Classical communication.
    - Step 4: Bob applies corrections.
    """)

def quantum_experiments():
    st.header("Mind-Blowing Quantum Experiments")
    st.write("""
    1. **Double-Slit Experiment**: Particles behave like waves.
    2. **Quantum Eraser**: Observation changes history.
    3. **Schrödinger’s Cat**: Superposition of life and death.
    """)

def theoretical_ideas():
    st.header("Theoretical Ideas Yet to Be Proven")
    st.write("""
    1. **Quantum Gravity**: Bridging relativity and quantum theory.
    2. **Time Crystals**: Perpetual motion without energy.
    3. **ER=EPR**: Linking entanglement with wormholes.
    """)

def rv_university_section():
    st.header("RV University and the Center for Quantum Science and Technologies (CQST)")
    st.write("""
    The **Center for Quantum Science and Technology (CQST)** at RV University is dedicated to cutting-edge research in quantum computing.

    **Acknowledgments**:
    - Dr. P.C. Deshmukh: Exceptional mentorship.
    - Prof. Vaidyanathan Sivasubramanian: Insightful guidance.
    - Prof. Bharath Manchikodi: Constant support.

    Visit CQST: [RV University](https://www.rvu.edu.in)
    """)

# Menu Content Mapping
if menu == "Project Code Walkthrough":
    code_walkthrough()
elif menu == "History of Quantum Mechanics":
    history_of_quantum_mechanics()
elif menu == "Current Quantum World":
    current_quantum_world()
elif menu == "Quantum Math and Notations":
    quantum_math_and_notations()
elif menu == "Quantum Gates and Operations":
    quantum_gates()
elif menu == "Teleportation Steps and Circuitry":
    teleportation_steps()
elif menu == "Mind-Blowing Quantum Experiments":
    quantum_experiments()
elif menu == "Theoretical Ideas Yet to Be Proven":
    theoretical_ideas()
elif menu == "RV University and CQST":
    rv_university_section()

st.write("---")
st.write("Explore, learn, and dive deep into the world of quantum mechanics. 🚀")

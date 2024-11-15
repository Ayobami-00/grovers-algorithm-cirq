# Grover's Algorithm in Cirq

This repository contains an implementation of **Grover's Algorithm** using **Cirq**, a quantum computing framework developed by Google. Grover's Algorithm is a quantum search algorithm that finds the unique input to a black-box function (oracle) that produces a marked output with a quadratic speedup over classical search algorithms.

## Project Structure

- **grover/**: Contains the core implementation of Grover's Algorithm.
  - `grover_algorithm.py`: The main implementation of Grover's search algorithm.
  - `oracle.py`: Implements the oracle function used in the algorithm.
  
- **examples/**: Contains example scripts demonstrating how to run the algorithm and visualize results.
  - `example_run.py`: A simple example to run Grover’s algorithm on a 2-qubit system.
  - `result_visualization.py`: Script to visualize the measurement outcomes and success rate.

- **requirements.txt**: Lists the Python dependencies needed for the project.

- **LICENSE**: The license under which the project is distributed. (Apache 2.0)

## Prerequisites

You will need Python 3.7 or higher and the following Python libraries:

- Cirq: Quantum computing framework
- numpy: For handling mathematical operations

Install the dependencies using:

```bash
pip install -r requirements.txt

# Euler Number Calculator
Calculates the euler number (Euler-Poincaré characteristic) for a .dot graph.
Aimed at the analysis of capillary networks.

## Requirements
Required packages are listed in requirements.txt and can be installed using pip as follows:\
`pip3 install -r requirements.txt`

## Input
- .dot graph
- Optional: Output filename (-o argument)

## Output
- .csv containing the euler number

## Usage example
`python3 euler_number.py mygraph.dot -o myoutputfile.csv`
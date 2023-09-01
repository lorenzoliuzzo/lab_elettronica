import math

def process_columns(input_file, output_file, delimiter='\t'):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    with open(output_file, 'w') as file:
        for line in lines:
            columns = line.split(delimiter)
            if len(columns) >= 4:
                # only for the differentiator's phase
                # ngspice acquire phase only in range [-pi, pi]
                value = float(columns[3])
                if value > 0.0: 
                    value -= 2.0 * math.pi 
                columns[3] = str(value)
                modified_columns = [columns[1], columns[2], columns[3]]
                file.write(delimiter.join(modified_columns) + '\n')

# Replace with your input and output file paths
input_file = 'ngspice_data.txt'
output_file = 'differentiator.txt'
# output_file = 'integrator.txt'

process_columns(input_file, output_file)
print('Data written to ', output_file)
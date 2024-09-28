import subprocess

def compile_and_run_c_program(c_file):
    exe_file = c_file.replace('.c', '.exe')

    case = 'medium1'

    compile_command = ['gcc', c_file, '-o', exe_file]
    # compile_command = ['gcc','-fopenmp ', '-o', exe_file,c_file]
    try:
        subprocess.run(compile_command, check=True)
        print(f"Compiled {c_file} to {exe_file} successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to compile {c_file}.")
        return

    try:
        with open(f'input_{case}.txt', 'r') as input_demo:
            with open('output.txt', 'w') as output_demo:
                subprocess.run([exe_file], check=True, stdin=input_demo, stdout=output_demo)
    except subprocess.CalledProcessError:
        print(f"Failed to run {exe_file}.")
        return
    
    output_lines,expected_lines = '',''
    with open('output.txt', 'r') as output_demo:
        output_lines = output_demo.readlines()

    with open(f'output_{case}.txt', 'r') as expected_output:
        expected_lines = expected_output.readlines()
    print()
    for i, (line1, line2) in enumerate(zip(output_lines, expected_lines)):
        if line1 != line2:
            print(f"\033[91mOutput does not match expected output at line {i}.\033[0m")
            return
    else:
        print("\033[92mOutput matches expected output.\033[0m")

    print(f"\033[93m{output_lines[-1]}\033[0m")

c_file = 'conv_template.c' 
compile_and_run_c_program(c_file)
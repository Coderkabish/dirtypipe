import os 

import sys
import os
import subprocess

if len(sys.argv) < 2:
    print("Usage: python script.py <filename.c>")
    sys.exit(1)

arg1 = sys.argv[1]

# Check if file exists
if not os.path.isfile(arg1):
    print(f"Error: File '{arg1}' not found.")
    sys.exit(1)

# Compile the C file
compile_cmd = f"gcc {arg1} -o output"
if os.system(compile_cmd) == 0:  # Check if compilation is successful
    print("Compilation successful. Running the program...")
    
    # Run the compiled program
os.system("./output /bin/su")

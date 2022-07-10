# create dictionaries
operations = {"ADD": "0000",
           "AND": "0001",
           "OR": "0010",
           "XOR": "0011",
           "ADDI": "0100",
           "ANDI": "0101",
           "ORI": "0110",
           "XORI": "0111",
           "LD": "1000",
           "ST": "1001",
           "JUMP": "1010",
           "BEQ": "1011",
           "BLT": "1100",
           "BGT": "1101",
           "BLE": "1110",
           "BGE": "1111"}

registers = {"R0": "0000",
             "R1": "0001",
             "R2": "0010",
             "R3": "0011",
             "R4": "0100",
             "R5": "0101",
             "R6": "0110",
             "R7": "0111",
             "R8": "1000",
             "R9": "1001",
             "R10": "1010",
             "R11": "1011",
             "R12": "1100",
             "R13": "1101",
             "R14": "1110",
             "R15": "1111"}

# create variable for hex result
hex_result = ""
# open input file readonly to read instructions
with open("input.txt", "r") as inputFile:
    lines = inputFile.readlines()
    # loop through each instruction
    for line in lines:
        # create variable for binary result, add 2 bits to make total 20 bits
        binary_result = "00"
        # split line with space to define operation
        parts = line.replace('\n', "").split(" ")
        operation = parts[0]
        binary_result += operations[operation]
        # split rest line with comma
        regs = parts[1].split(',')
        # add registers
        for reg in regs:
            if reg.startswith("R"):
                binary_result += registers[reg]
        # check operation for various results
        if operation == "ADD" or operation == "AND" or operation == "OR" or operation == "XOR":
            # first 2 bits
            binary_result += "00"
        elif operation == "LD" or operation == "ST":
            # LD/ST address value
            binary_result += '{:010b}'.format(int(reg) & 0x3ff)
        elif operation == "JUMP":
            # jump address value
            binary_result += '{:014b}'.format(int(regs[0]) & 0x3fff)
        else:
            # immediate or branch address value
            binary_result += '{:06b}'.format(int(reg) & 0x3f)

        # produce result string as hex
        hex_result += '{0:05x}'.format(int(binary_result, 2)) + "\n"

# open output file for writing
with open("output.hex", 'w+') as outputFile:
    outputFile.writelines("v2.0 raw\n")
    outputFile.writelines(hex_result)

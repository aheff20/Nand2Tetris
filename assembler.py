# symbol table dictionary
variables = {
            "SP": 0,
            "LCL": 1,
            "ARG": 2,
            "THIS": 3,
            "THAT": 4,
            "R0": 0,
            "R1": 1,
            "R2": 2,
            "R3": 3,
            "R4": 4,
            "R5": 5,
            "R6": 6,
            "R7": 7,
            "R8": 8,
            "R9": 9,
            "R10": 10,
            "R11": 11,
            "R12": 12,
            "R13": 13,
            "R14": 14,
            "R15": 15,
            "SCREEN": 16384,
            "KBD": 24576
        }
# dictionaries with all binary codes for C instructions
destinations = {
            "M": "001",
            "D": "010",
            "MD": "011",
            "A": "100",
            "AM": "101",
            "AD": "110"
        }
jumps = {
            "JGT": "001",
            "JEQ": "010",
            "JGE": "011",
            "JLT": "100",
            "JNE": "101",
            "JLE": "110",
            "JMP": "111"
        }
comps = {
            "0": "0101010",
            "1": "0111111",
            "-1": "0111010",
            "D": "0001100",
            "A": "0110000",
            "!D": "0001101",
            "!A": "0110001",
            "-D": "0001111",
            "-A": "0110011",
            "D+1": "0011111",
            "A+1": "0110111",
            "D-1": "0001110",
            "A-1": "0110010",
            "D+A": "0000010",
            "D-A": "0010011",
            "A-D": "0000111",
            "D&A": "0000000",
            "D|A": "0010101",
            "M": "1110000",
            "!M": "1110001",
            "-M": "1110011",
            "M+1": "1110111",
            "M-1": "1110010",
            "D+M": "1000010",
            "M+D": "1000010",
            "D-M": "1010011",
            "M-D": "1000111",
            "D&M": "1000000",
            "D|M": "1010101"
        }
# initial address to start storing new variables
spot = 16

fileName = input("Enter the name of the file: ")

# get all label values
with open(fileName, 'r') as assemblerCode:
    lineNumber = 0
    for i, line in enumerate(assemblerCode):
        if "(" in line:
            label = line[line.find("(")+1:line.find(")")]
            variables[label] = lineNumber
            continue
        if line[-1] == "\n":
            line = line[:-1]
        line = line.replace(" ", "")
        if line == "":
            continue
        if line[0] == "/":
            continue
        lineNumber += 1


with open("assemblerOutput.hack", 'w') as writeFile:
    with open(fileName, 'r') as assemblerCode:
        for i, line in enumerate(assemblerCode):
            ans = ""

            # remove trailing new line
            if line[-1] == "\n":
                line = line[:-1]

            # remove any spaces or whitespace
            line = line.replace(" ", "")

            # find any comments and ignore anything after
            if "//" in line:
                line = line[:line.find("//")]

            # ignore empty lines
            if line == "":
                continue

            #print(line + ": ", end="")

            # check if line starts with @ and is a valid A instruction
            if line[0] == "@":
                # check if we are looking at a numbered address
                if line[1:].isnumeric():
                    # get binary version of number
                    num = bin(int(line[1:]))[2:]
                    ans = str(num).zfill(16)
                    print(ans)
                    writeFile.write(ans + "\n")
                    continue
                else:
                    # if the variable name already exists, just grab its value
                    if line[1:] in variables:
                        num = bin(variables[line[1:]])[2:]
                        ans = str(num.zfill(16))
                        print(ans)
                        writeFile.write(ans + "\n")
                        continue
                    else:
                        # if the variable doesn't exist, make a new one
                        variableName = line[1:]
                        variables[variableName] = spot
                        num = bin(int(spot))[2:]
                        ans = str(num.zfill(16))
                        print(ans)
                        writeFile.write(ans + "\n")
                        spot += 1
                        continue

            # check C instructions
            ans = "111"
            # contains a dest
            if "=" in line:
                dest = line[:line.find("=")]
                destStr = destinations[dest]
                line = line[line.find("=")+1:]
            else:
                destStr = "000"

            # contains a jump
            if ";" in line:
                jump = line[line.find(";")+1:]
                jumpStr = jumps[jump]
                line = line[:line.find(";")]
            else:
                jumpStr = "000"

            # only thing left is a comp
            if "(" in line or ")" in line:
                #print()
                continue
            compStr = comps[line]

            ans += compStr + destStr + jumpStr
            print(ans)
            writeFile.write(ans + "\n")

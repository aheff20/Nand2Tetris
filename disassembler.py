# dictionaries with all binary codes for C instructions
destinations = {
            "000": "",
            "001": "M",
            "010": "D",
            "011": "MD",
            "100": "A",
            "101": "AM",
            "110": "AD"
        }
jumps = {
            "000": "",
            "001": "JGT",
            "010": "JEQ",
            "011": "JGE",
            "100": "JLT",
            "101": "JNE",
            "110": "JLE",
            "111": "JMP"
        }
comps = {
            "0101010": "0",
            "0111111": "1",
            "0111010": "-1",
            "0001100": "D",
            "0110000": "A",
            "0001101": "!D",
            "0110001": "!A",
            "0001111": "-D",
            "0110011": "-A",
            "0011111": "D+1",
            "0110111": "A+1",
            "0001110": "D-1",
            "0110010": "A-1",
            "0000010": "D+A",
            "0010011": "D-A",
            "0000111": "A-D",
            "0000000": "D&A",
            "0010101": "D|A",
            "1110000": "M",
            "1110001": "!M",
            "1110011": "-M",
            "1110111": "M+1",
            "1110010": "M-1",
            "1000010": "D+M",
            "1010011": "D-M",
            "1000111": "M-D",
            "1000000": "D&M",
            "1010101": "D|M"
        }

fileName = input("Enter the name of the file: ")
with open("disassemblerOutput.asm", 'w') as writeFile:
    with open(fileName, 'r') as hackCode:
        for i, line in enumerate(hackCode):
            ans = ""
            if line == "":
                continue

            if line[-1] == "\n":
                line = line[:-1]

            # A instruction
            if line[0] == "0":
                num = line[1:]
                num = int(num, 2)
                ans = "@" + str(num)
                writeFile.write(ans + "\n")
                print(ans)
                continue

            # C instruction
            else:
                comp = line[3:10]
                dest = line[10:13]
                jump = line[13:]

                compStr = comps[comp]
                destStr = destinations[dest]
                jumpStr = jumps[jump]

                if destStr:
                    destStr += "="
                if jumpStr:
                    jumpStr = ";" + jumpStr

                ans = destStr + compStr + jumpStr
                writeFile.write(ans + "\n")
                print(ans)

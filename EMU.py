import random

class CPU:
    def __init__(self):
        self.registers = [0] * 4  # 4 general-purpose registers
        self.pc = 0  # program counter
        self.memory = [0] * 256  # 256 bytes of memory

    def load_program(self, program):
        for addr, instr in enumerate(program):
            self.memory[addr] = instr

    def fetch(self):
        instruction = self.memory[self.pc]
        self.pc += 1
        return instruction

    def decode_execute(self, instruction):
        opcode = (instruction & 0xF0) >> 4
        operand = instruction & 0x0F

        if opcode == 0x0:
            # NOP (no operation)
            pass
        elif opcode == 0x1:
            # ADD immediate to register A
            self.registers[0] += operand
        elif opcode == 0x2:
            # SUB immediate from register A
            self.registers[0] -= operand
        elif opcode == 0xF:
            # HLT (halt)
            print("Halted")
            return False
        else:
            print(f"Unknown opcode {opcode}")

        return True

    def run(self):
        running = True
        while running:
            instr = self.fetch()
            running = self.decode_execute(instr)


def main():
    # Example program for our hypothetical CPU
    program = [
        0x10, 0x05,   # ADD 5 to register A
        0x1F, 0x03,   # SUB 3 from register A
        0xF0          # HLT (halt)
    ]

    cpu = CPU()
    cpu.load_program(program)
    cpu.run()

if __name__ == "__main__":
    main()

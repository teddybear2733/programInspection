import os
from pathlib import Path
import argparse
from datetime import date

class Program():
    def __init__(self, program):
        self.todays_date = date.today()
        self.filePath = Path(program)
        if not self.filePath.exists():
            raise("File Not Found!!!!")
    
    def createObjDump(self):
        os.system(f"objdump -D {self.filePath} > ./objDumps/{self.todays_date.year}_{self.todays_date.month}_{self.todays_date.day}_objDump")   

class Inspection():
    def __init__(self):
        pass
    
    def return_msg(self):
        print("Happy Hacking!")



if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--program", help="Path to program")
    #parser.add_argument("--function", help="For future use")
    args = parser.parse_args()
    
    print(f"Inspecting Program: {args.program}")
    p = Program(args.program)

    p.createObjDump()


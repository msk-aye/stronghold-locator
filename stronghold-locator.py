# Author: msk-aye
import math
import numpy as np
import sys

def parse_input():
  try:
    arg1 = input("Enter the first position: ").split(" ")
    arg2 = input("Enter the second position: ").split(" ")

    x1 = float(arg1[8])
    y1 = float(arg1[6])
    t1 = math.radians(float(arg1[9]) * (-1))

    x2 = float(arg2[8])
    y2 = float(arg2[6])
    t2 = math.radians(float(arg2[9]) * (-1))

    return x1, y1, t1, x2, y2, t2

  except Exception:
    print("Unable to parse input, please enter exactly as copied using f3 + c")
    output = parse_input()
    return output

def calculate(x1, y1, t1, x2, y2, t2):
  try:
    b1 = y1 - math.tan(t1) * x1
    b2 = y2 - math.tan(t2) * x2

    equations = np.array([[1, -(math.tan(t1))], [1, -(math.tan(t2))]])
    solutions = np.array([b1, b2])

    coords = np.linalg.solve(equations, solutions)
    return coords

  except Exception:
    print("Unable to complete calculation. You on your own on this one gang 😭🙏.")
    sys.exit(1)

def main():
  x1, y1, t1, x2, y2, t2 = parse_input()
  print("------------ Calculating stronghold location ------------")

  x, y = calculate(x1, y1, t1, x2, y2, t2)

  print(f"Overworld coordinates: ({round(x)}, {round(y)})")
  print(f"Nether coordinates: ({round(x/8)}, {round(y/8)})")

  sys.exit(0)

if __name__ == "__main__":
  main()
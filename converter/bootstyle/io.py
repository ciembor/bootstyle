import sys

def getFilenames():
  try:
    if len(sys.argv) > 3:
      sys.exit("Too many arguments.")
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    return (input_filename, output_filename)
  except IndexError:
    sys.exit("Too few arguments.")
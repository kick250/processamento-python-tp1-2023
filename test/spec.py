import sys
import io

def expect_print(out_function, expected_out):
  capturedOutput = io.StringIO()
  sys.stdout = capturedOutput
  out_function()
  sys.stdout = sys.__stdout__
  value = capturedOutput.getvalue()
  assert value == expected_out
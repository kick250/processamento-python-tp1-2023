import sys
import io

sys.path.insert(1, '../')


def expect_print(out_function, expected_out):
  capturedOutput = io.StringIO()
  sys.stdout = capturedOutput
  out_function()
  sys.stdout = sys.__stdout__
  value = capturedOutput.getvalue()
  assert value == expected_out
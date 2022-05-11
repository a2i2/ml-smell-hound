import os
import subprocess

# Helper function for getting the output of a command.
def get_command_output(cargs, is_text=True, cmd_input=None, print=False, my_env={**os.environ}, stdout=subprocess.PIPE):
    return subprocess.run(args=cargs, stdout=stdout, stderr=subprocess.PIPE, text=is_text, input=cmd_input, env=my_env)

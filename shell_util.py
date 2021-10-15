import os
import subprocess

def pretty_print(str):
    print(f"==> {str}")

# Helper function for printing what command is being executed to stdout.
def command_print(command):
    pretty_print(f"Executing command: {command}")
    return command

# Helper function for getting the output of a command.
def get_command_output(command, is_text=True, cmd_input=None, print=False, my_env={**os.environ}, stdout=subprocess.PIPE):
    if print:
        cargs = command_print(command.split())
    else:
        cargs = command.split()
    return subprocess.run(args=cargs, stdout=stdout, stderr=subprocess.PIPE, text=is_text, input=cmd_input, env=my_env)

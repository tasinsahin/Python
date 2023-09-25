import subprocess


def clear():
    command_to_execute = 'extension.clearTerminal'
    subprocess.run(['code', '--command', command_to_execute])
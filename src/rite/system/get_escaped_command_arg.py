from shlex import quote


def get_escaped_command_arg(arg) -> str:
    """Escapes a command line argument to make it safe for shell usage."""
    return quote(arg)

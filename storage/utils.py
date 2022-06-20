# External/Internal/Builtin Librarys
import os, sys


def clear(title: str) -> None:
    """Clear Terminal"""
    os.system(f"@cls & @title {title}") if os.name == "nt" else os.system(
        "clear"
    ) and sys.stdout.write(title)


def close(code: int = None, command: str = None) -> None:
    """Exit/Close Pomegranate"""
    sys.exit(code) if code != None else sys.exit(command)

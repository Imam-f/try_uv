import numpy
import sys
import tkinter

# cp -r ~/.local/share/uv/python/cpython-3.12.8-linux-x86_64-gnu/lib/tcl8.6 .venv/lib/

def main():
    print("Hello from project!")
    print(numpy.__version__)
    # Print python version
    print("Python version:", sys.version)
    tcl = tkinter.Tcl()
    print(tcl.eval("puts \"Hello, world!\""))


if __name__ == "__main__":
    main()

"""Module for cleaning git."""
import os

def main():
    """Clean git."""
    os.system("git clean -f")
    os.system("git stash")

if __name__ == '__main__':
    main()
"""Windows compatibility shim for the missing fcntl module.

Gunicorn expects the Unix `fcntl` module on some paths. On Windows this module
is not available, so we provide a minimal stub that allows Gunicorn to import.
"""

import os

LOCK_EX = 1
LOCK_SH = 2
LOCK_NB = 4
LOCK_UN = 8


def fcntl(fd, op, arg=0):
    return 0


def ioctl(fd, op, arg=0, mutable_buffer=False):
    return 0


def flock(fd, op):
    return 0


def lockf(fd, operation, length=0, start=0, whence=0):
    return 0

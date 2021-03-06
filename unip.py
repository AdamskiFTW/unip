#!/usr/bin/python
#unip is a simple tool for copying, moving, deleting or renaming files

import os, sys, shutil

def copy(src, dst):
    print("Copy ") + src + (" to ") + dst + ("?")
    copyans = raw_input("")
    if copyans[0].lower() == "y":
        return shutil.copy(src, dst)
    else:
        return sys.exit()

def move(src, dst):
    print("Move ") + src + (" to ") + dst + ("?")
    moveans = raw_input("")
    if moveans[0].lower() == "y":
        return shutil.move(src, dst)
    else:
        return sys.exit()

def delete(name):
    print("Delete file ") + name + ("?")
    delans = raw_input("")
    if delans[0].lower() == "y":
        return os.remove(name)
    else:
        return sys.exit()

def rename(name, rename):
    print("Rename ") + name + (" to ") + rename + ("?")
    reans = raw_input("")
    if reans[0].lower() == "y":
        return os.rename(name, rename)
    else:
        return sys.exit()

def help():
    print("unip is a simple utility tool to copy, move, delete and rename files\n")
    print("Usage: " + os.path.basename(__file__) + " <function> <filename> <pathname>\n")
    print("<function> can be copy, move, delete or rename\n")
    print("<filename> is the name of the target file\n")
    print("<pathname> is the name of the target pathname (where applicable)")

if len(sys.argv) == 1:
    print("Use \'" + os.path.basename(__file__) + " help\' for info")
    sys.exit()
else:
    func1 = sys.argv[1]
    if func1.lower() == "delete":
        delete(sys.argv[2])
    elif func1.lower() == "rename":
        rename(sys.argv[2], sys.argv[3])
    elif func1.lower() == "move":
        move(sys.argv[2], sys.argv[3])
    elif func1.lower() == "copy":
        copy(sys.argv[2], sys.argv[3])
    elif func1.lower() == "help":
        help()
    else:
        print("Unknown command. For help use 'unip help'")
        sys.exit()

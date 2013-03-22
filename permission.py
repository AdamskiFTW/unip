import os, sys

def permission():
    chmodname = sys.argv[2]
    mode = sys.argv[3]
    print("Change ") + name + (" to mode ") + mode + ("?")
    modeans = raw_input("")
    if modeans[0].lower() == "y":
        chmod()
    else:
        sys.exit()


def chmod():
    if mode == "-r":
        os.chmod(chmodname, stat.S_IREAD)
    elif mode == "-w":
        os.chmod(chmodname, stat.S_IWRITE)
    elif mode == "-x":
        os.chmod(chmodname, stat.S_IXEC)
    elif mode == "-rw":
        os.chmod(chmodname, stat.SIREAD)
        os.chmod(chmodname, stat.SIWRITE)
    elif mode == "-rx":
        os.chmod(chmodname, stat.S_IREAD)
        os.chmod(chmodname, stat.S_IXEC)
    elif mode == "-wx":
        os.chmod(chmodname, stat.S_IWRITE)
        os.chmod(chmodname, stat.S_IXEC)
    elif mode == "-rwx":
        os.chmod(chmodname, stat.S_IRWXU)
    else:
        sys.exit()

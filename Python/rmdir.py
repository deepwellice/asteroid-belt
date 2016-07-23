import shutil, os, sys, stat

def rmtree_onerror(function, exc_path, excinfo):
    if isinstance(excinfo[1], PermissionError):
        os.chmod(exc_path, stat.S_IWRITE)
        print('Removing {0} again......'.format(exc_path))
        os.remove(exc_path)
    else:
        raise
    return

def remove_dir(path):
    shutil.rmtree(path, onerror=rmtree_onerror)
    return 0

if __name__ == '__main__':
    sys.exit(remove_dir(sys.argv[1]))


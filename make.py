from distutils.core import setup
import py2exe
import os
includes = []
for root, dirs, files in os.walk('.') :
    for file in files :
        if file[-3:] == '.py' :
            print file
            includes.append(file[:-3])

excludes = [
    "pywin",
    "pywin.debugger",
    "pywin.debugger.dbgcon",
    "pywin.dialogs",
    "pywin.dialogs.list",
    "win32com.server",
]

options = {
    "bundle_files": 1,                 # create singlefile exe
    "compressed"  : 1,                 # compress the library archive
    "excludes"    : excludes,
    "includes"    : includes,
    "dll_excludes": ["w9xpopen.exe"]   # we don't need this
}

setup(
    options = {"py2exe": options},
    zipfile = None,
    console = ['main.py']
)
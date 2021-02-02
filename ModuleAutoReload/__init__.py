#only been tested in Python 3.9, in windows 10!
#needed packages: watchdog
#pip install watchdog

from importlib import reload
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

import os
import time

#import subprocess
#import sys
#def install():
#    subprocess.check_call([sys.executable, "-m", "pip", "install", "watchdog"])

class ModifiedEventHandler(FileSystemEventHandler):
    def __init__(self, module, callback, logging):
        self.module = module
        self.logging = logging
        self.prev_time = 0
        self.isdir = module.__file__.endswith("__init__.py")
        self.callback = callback

    def Reload(self):
        if(time.time() - self.prev_time > 0.5):
            self.prev_time = time.time()
            try:
                reload(self.module)
                if self.callback:
                    self.callback()
                if(self.logging):
                    print("Successfully loaded module:", self.module.__spec__.name)
            except Exception as err:
                if(self.logging):
                    print ("Error while loading module:", self.module.__spec__.name)
                    print(str(err))

    def on_modified(self, event):
        if(self.isdir):
            self.Reload()
        elif(os.path.isfile(event.src_path) and event.src_path.endswith(".py")):
            if (os.path.normcase(os.path.abspath(event.src_path)) == os.path.normcase(self.module.__file__)):
                self.Reload()

class ModuleAutoReload():
    def __init__(self, module, callback=None, logging=False):
        path = os.path.dirname(module.__file__)
        event_handler = ModifiedEventHandler(module, callback, logging)
        observer = Observer()
        observer.schedule(event_handler, path, recursive=True)
        observer.start()

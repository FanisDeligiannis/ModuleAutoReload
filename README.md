# ModuleAutoReload
Auto reloads a python module/package when you change something in it. That's pretty much it


Usage example:
```python
from ModuleAutoReload import ModuleAutoReload
import my_module

ModuleAutoReload(my_module)
```



Usage example with logging:

```python
from ModuleAutoReload import ModuleAutoReload
import my_module

ModuleAutoReload(my_module, logging=True)
```



Usage example with callback:

```python
from ModuleAutoReload import ModuleAutoReload
import my_module

def module_callback():
  print("Module reloaded!!")

ModuleAutoReload(my_module, callback=module_callback)
```

# importer.py
print('Running importer.py')

import os.path
import types
import sys

def import_(module_name, module_file, module_path):
    if module_name in sys.modules:
        return sys.modules[module_name]
    
    module_rel_file_path = os.path.join(module_path, module_file)
    module_abs_file_path = os.path.abspath(module_rel_file_path)

    with open(module_abs_file_path, 'r') as code_file:
        source_code = code_file.read()
    
    mod = types.ModuleType(module_name)
    mod.__file__ = module_abs_file_path

    sys.modules[module_name] = mod

    code = compile(source_code, filename=module_abs_file_path, mode='exec')

    exec(code, mod.__dict__)

    return sys.modules[module_name]
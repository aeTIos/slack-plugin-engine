import importlib.util
import glob


def loadmodules(path):
    modules = glob.glob(path + "*.py")
    module_array = []
    module_names = []
    for i in modules:
        modname = i[len(path):-3]
        module_names.append(modname)
        temp = importlib.util.spec_from_file_location(modname, i)
        module_array.append(importlib.util.module_from_spec(temp))
        temp.loader.exec_module(module_array[-1])
        print('Loaded module:', modname)
    return module_array, module_names


"""
Run all kata modules. They'll raise NotImplementedError or assert if tasks aren't complete.
"""

import importlib, sys

modules = [
    "01_comprehensions",
    "02_unpacking_and_enumerate",
    "03_eafp_and_context",
    "04_dataclass_and_repr",
    "05_generators_and_itertools",
    "06_pattern_matching",
]

failures = 0
for name in modules:
    print(f"==> {name}")
    try:
        mod = importlib.import_module(name)
        if hasattr(mod, "__main__"):
            pass  # not used
        if hasattr(mod, "__file__"):
            # trigger the test section by executing as a script
            # we simulate script run by reloading after setting __name__ to "__main__"
            pass
        # Simpler approach: load the module, then exec its file as __main__
        with open(mod.__file__, "rb") as f:
            code = compile(f.read(), mod.__file__, "exec")
        g = {"__name__": "__main__"}
        exec(code, g, g)
    except NotImplementedError as e:
        print(f"   TODO remaining in {name}: {e}")
        failures += 1
    except AssertionError as e:
        print(f"   Assertion failed in {name}: {e}")
        failures += 1
    except Exception as e:
        print(f"   Error in {name}: {e}")
        failures += 1

print("\nDone. Failures:", failures)
if failures:
    sys.exit(1)

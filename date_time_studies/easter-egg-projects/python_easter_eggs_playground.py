#!/usr/bin/env python3
"""
Python Easter Eggs Playground
-----------------------------
Run this once to tour a handful of Python's cheeky built-ins.

Usage:
    python python_easter_eggs_playground.py [--antigravity]

Notes:
- `import antigravity` opens a browser tab to xkcd #353. It's OFF by default.
- We sandbox the FLUFL (<> not-equal) demo by creating a tiny temp script that
  uses `from __future__ import barry_as_FLUFL`, then run it in a subprocess.
- We show the `braces` gag and the Zen ROT13 cipher too.

"""
import sys
import os
import subprocess
import tempfile
import codecs

def header(title: str):
    print("\n" + "="*80)
    print(title)
    print("="*80)

def zen_of_python():
    header("1) The Zen of Python  (import this) + ROT13 peek")
    import this  # prints nothing by itself when imported programmatically
    # The poem is printed when importing interactively; here, we decode the source string.
    print("Decoded Zen via ROT13:\n")
    print(codecs.decode(this.s, "rot13"))

def antigravity_maybe(enable: bool):
    header("2) Antigravity (opens xkcd #353)")
    if enable:
        print("Launching browser to xkcd #353...")
        import antigravity  # noqa: F401  # side-effect: opens browser
        print("If your browser didn't open, you're likely in a headless or locked-down env.")
    else:
        print("Skipped. Re-run with --antigravity to open the comic in your browser.")

def hello_modules():
    header("3) __hello__ and __phello__")
    import __hello__   # prints "Hello world!"
    try:
        import __phello__
        import __phello__.world
    except ImportError as e:
        print(f"__phello__ import not available: {e}")
    except Exception as e:
        print(f"__phello__ import oddity raised: {e!r} (this can vary by Python version)")

def braces_gag():
    header("4) from __future__ import braces (the classic jab)")
    code = "from __future__ import braces\n"
    try:
        exec(code, {})
    except SyntaxError as e:
        print("Result:", e)

def flufl_demo():
    header("5) FLUFL: bring back the '<>' not-equal operator via a tiny script")
    script = "from __future__ import barry_as_FLUFL\nprint('1 <> 2 ->', 1 <> 2)"
    with tempfile.TemporaryDirectory() as td:
        p = os.path.join(td, "flufl_demo.py")
        with open(p, "w") as f:
            f.write(script)
        try:
            out = subprocess.check_output([sys.executable, p], stderr=subprocess.STDOUT, text=True)
            print(out.strip())
        except subprocess.CalledProcessError as cpe:
            print("Running FLUFL demo failed. Output:\n", cpe.output)

def hash_note():
    header("6) Hash randomization tidbit")
    s = "hashes vary per process by design"
    print("hash('Python') this run:", hash("Python"))
    print("hash('Python') another run will likely differ due to PYTHONHASHSEED randomization.")
    print("Note: This is a security feature; set PYTHONHASHSEED for stable hashes if needed.")

def main(argv):
    antigrav = "--antigravity" in argv
    zen_of_python()
    antigravity_maybe(antigrav)
    hello_modules()
    braces_gag()
    flufl_demo()
    hash_note()
    print("\nDone. Re-run with --antigravity to launch the xkcd page.")

if __name__ == "__main__":
    main(sys.argv[1:])

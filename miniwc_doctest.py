# Author: Jiacheng Li
# Date: 30/9/2018
"""
>>> import subprocess
>>> subprocess.check_output('python3 miniwc.py testinputs/test1.txt', shell=True)
b'\\t10\\t10\\t20 testinputs/test1.txt\\n'
>>> subprocess.check_output('python3 miniwc.py testinputs/test2.txt', shell=True)
b'\\t2\\t2\\t12 testinputs/test2.txt\\n'
"""

 # We add the boilerplate to make this module both executable and importable.
if __name__ == "__main__":
    import doctest
    # The following command extracts all testable docstrings from the current module.
    doctest.testmod()
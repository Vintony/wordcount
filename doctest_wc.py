# Author Jiacheng Li
# Date: 7/10/2018
"""
>>> import subprocess
>>> subprocess.check_output('python3 wc.py testinputs/test1.txt', shell = True)
b'\\t10\\t10\\t20\\ttestinputs/test1.txt\\n'
>>> subprocess.check_output('python3 wc.py -wcl testinputs/test1.txt', shell = True)
b'\\t10\\t10\\t20\\ttestinputs/test1.txt\\n'
>>> subprocess.check_output('python3 wc.py -wwwwwwcccclllcccwww testinputs/test1.txt', shell = True)
b'\\t10\\t10\\t20\\ttestinputs/test1.txt\\n'
>>> subprocess.check_output('python3 wc.py -wcllcwqqq testinputs/test1.txt', shell = True)
b'wc: illegal option -- q\nusage: wc [-clmw] [file ...]'
>>> subprocess.check_output('python3 wc.py testinputs/test1.txt testinputs/test2.txt', shell = True)
b'\\t10\\t10\\t20\\ttestinputs/test1.txt\\n\\t2\\t2\\t12\\ttestinputs/test2.txt\\n\\t12\\t12\\t32\\ttotal\\n'
>>> subprocess.check_output('python3 wc.py testinputs/test9.txt testinputs/test2.txt', shell = True)
b'wc: testinputs/test9.txt: open: No such file or directory\\n\\t2\\t2\\t12\\ttestinputs/test2.txt\\n\\t2\\t2\\t12\\ttotal\\n'
>>> subprocess.check_output('python3 wc.py -w -l testinputs/test1.txt', shell = True)
b'\\t10\\t10\\ttestinputs/test1.txt\\n'
>>> subprocess.check_output('python3 wc.py -c -w testinputs/test1.txt', shell = True)
b'\\t10\\t20\\ttestinputs/test1.txt\\n'
>>> subprocess.check_output('python3 wc.py -w -c -l -wcllll testinputs/test1.txt', shell = True)
b'\\t10\\t10\\t20\\ttestinputs/test1.txt\\n'
>>> subprocess.check_output('python3 wc.py -wcllcwqqq testinputs/test1.txt testinputs/test2.txt', shell = True)
b'wc: illegal option -- q\\nusage: wc [-clmw] [file ...]'
>>> subprocess.check_output('python3 wc.py  -wcl testinputs/test1.txt -wclwcl', shell = True)
b'\\t10\\t10\\t20\\ttestinputs/test1.txt\\nwc: -wclwcl: open: No such file or directory\\n\\t10\\t10\\t20\ttotal\\n'
>>> subprocess.check_output('python3 wc.py testinputs/test9.txt', shell = True)
b'wc: testinputs/test9.txt: open: No such file or directory\\n'
>>> subprocess.check_output('python3 wc.py testinputs/-test1.txt', shell = True)
b'\\t10\\t10\\t20\\ttestinputs/-test1.txt\\n'
>>> subprocess.check_output('python3 wc.py -test1.txt', shell = True)
b'wc: illegal option -- t\\nusage: wc [-clmw] [file ...]'
>>> subprocess.check_output('python3 wc.py -cwl.txt', shell = True)
b'wc: illegal option -- .\\nusage: wc [-clmw] [file ...]'
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()

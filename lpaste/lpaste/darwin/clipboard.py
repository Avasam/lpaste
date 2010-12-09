import os
from lpaste.source import Source

# from pyperclip (http://coffeeghost.net/2010/10/09/pyperclip-a-cross-platform-clipboard-module-for-python)

def macSetClipboard(text):
	outf = os.popen('pbcopy', 'w')
	outf.write(text)
	outf.close()

def macGetClipboard():
	outf = os.popen('pbpaste', 'r')
	content = outf.read()
	outf.close()
	return content

def get_source():
	code = macGetClipboard()
	src = Source(code=code)
	try:
		# see if the code can compile as Python
		compile(code, 'pasted_code.py', 'exec')
		src.format = 'python'
	except:
		pass # use default format
	return src

set_text = macSetClipboard
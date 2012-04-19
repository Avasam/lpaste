import sys
import platform
from collections import defaultdict

import setuptools

py26reqs = ['importlib'] if sys.version_info < (2, 7) else []

# add any platform-specific requirements
clipboard_support = defaultdict(lambda: [], {
	'Windows': ['jaraco.windows>=2.1'],
	})[platform.system()]

setup_params = dict(
	name="lpaste",
	use_hg_version=True,
	packages=setuptools.find_packages(),
	entry_points = {
		'console_scripts': [
			'lpaste = lpaste.lpaste:main',
		],
	},
	install_requires = [
		'poster',
		'keyring>=0.6',
	] + py26reqs,
	extras_require = dict(
		clipboard = clipboard_support,
	),
	description="Library Paste command-line client",
	license = 'MIT',
	author="Chris Mulligan",
	author_email="chmullig@gmail.com",
	maintainer = 'Chris Mulligan',
	maintainer_email = 'chmullig@gmail.com',
	url = 'http://bitbucket.org/chmullig/librarypaste-tools/lpaste',
	classifiers=[
		'Development Status :: 4 - Beta',
		'License :: OSI Approved :: MIT License',
		'Operating System :: POSIX',
		'Programming Language :: Python :: 2.6',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
	],
	setup_requires = [
		'hgtools',
	],
	use_2to3=True,
)

if __name__ == '__main__':
	setuptools.setup(**setup_params)
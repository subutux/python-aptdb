python-aptdb
============

A collection of classes to interact with apt repositories

Example
-------

```python
import aptdb
adb = aptdb("http://be.archive.ubuntu.com/ubuntu",'quantal','main','i386')
print adb.db['zsh'].Description
for dependicy in adb.db['zsh'].Depends:
	print adb.db[dependicy[0]]

```
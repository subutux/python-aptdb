python-aptdb
============

A collection of classes to interact with apt repositories

Example
-------

```python
import aptdb
adb = aptdb("http://be.archive.ubuntu.com/ubuntu",'quantal','main','i386')
print adb.db['zsh'].Description
#shell with lots of features
for dependicy in adb.db['zsh'].Depends:
	print adb.db[dependicy[0]]

#<AptPackage 'libc6' v2.15-0ubuntu20>
#<AptPackage 'libcap2' v1:2.22-1ubuntu4>
#<AptPackage 'libtinfo5' v5.9-10ubuntu1>
```
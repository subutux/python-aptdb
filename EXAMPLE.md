Example Usage
=============

Fetching the Packages database
------------------------------
```python
>>> import aptdb
>>> adb = aptdb.aptdb("http://be.archive.ubuntu.com/ubuntu",'quantal','main','i386',changelogserver="http://changelogs.ubuntu.com/changelogs")
Downloading http://be.archive.ubuntu.com/ubuntu/dists/quantal/main/binary-i386/Packages.gz
Done downloading
Loading into database
Converting into AptPackage instances
>>> print adb.db['zsh'].Description
shell with lots of features
>>> print adb.db['zsh'].Bugs
https://bugs.launchpad.net/ubuntu/+filebug
>>> for pkg in adb.db['zsh'].Depends: print adb.db[pkg[0]]
...
<AptPackage 'libc6' v2.15-0ubuntu20>
<AptPackage 'libcap2' v1:2.22-1ubuntu4>
<AptPackage 'libtinfo5' v5.9-10ubuntu1>
>>> print adb.db['zsh']
<AptPackage 'zsh' v5.0.0-2ubuntu1>
>>> print adb.db['zsh'].getCurrentChangelog()
{'Author': 'Adam Conrad', 'Author_Email': 'red@ct.ed', 'Changelog': "\n  * Merge from Debian experimental, remaining changes:\n    - debian/zshrc: Enable completions by default, unless\n      skip_global_compinit is set\n    - Keep using the upstream tarball that contains pre-generated docs as\n      yodl is required to build them but the MIR hasn't been approved.\n    - Drop yodl from Build-Depends.\n\n", 'Date': 'Sun, 16 Sep 2012 02:23:12 -0600', 'Version': '5.0.0-2ubuntu1', 'Release': 'quantal', 'urgency': 'low'}
```

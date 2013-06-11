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
print adb.db['zsh'].__json__()
```
```json
{
    "MD5sum": "7cfde66728c1060be1bafd311de04f66", 
    "Section": "libs", 
    "Filename": "pool/main/e/eglibc/libc6_2.15-0ubuntu20_i386.deb", 
    "Priority": "required", 
    "Source": "eglibc", 
    "Replaces": [
        [
            "belocs-locales-bin"
        ], 
        [
            "libc6-i386"
        ]
    ], 
    "Pre_Depends": null, 
    "Provides": "glibc-2.13-1, libc6-i686", 
    "SHA256": "63c805b709c244a1c57a5ca9b6ad65e6d4d92ac1cd527320b087d3e2998b1417", 
    "Homepage": "http://www.eglibc.org", 
    "Original-Maintainer": "GNU Libc Maintainers <debian-glibc@lists.debian.org>", 
    "Recommends": null, 
    "Description": "Embedded GNU C Library", 
    "Breaks": [
        [
            "libhwloc0", 
            "(<< 1.2-3)"
        ], 
        [
            "liblouis0", 
            "(<< 2.3.0-2)"
        ], 
        [
            "liblouisxml1", 
            "(<< 2.4.0-2)"
        ], 
        [
            "nscd", 
            "(<< 2.15)"
        ]
    ], 
    "Installed-Size": "9130", 
    "Conflicts": [
        [
            "belocs-locales-bin"
        ], 
        [
            "libc6-i686"
        ], 
        [
            "prelink", 
            "(<< 0.0.20090925)"
        ], 
        [
            "tzdata", 
            "(<< 2007k-1)"
        ], 
        [
            "tzdata-etch"
        ]
    ], 
    "SHA1": "1a702d7c07ee58b9a2c276d97e6fd35039042f6d", 
    "Package": "libc6", 
    "Multi-Arch": "same", 
    "Bugs": "https://bugs.launchpad.net/ubuntu/+filebug", 
    "Suggests": [
        [
            "glibc-doc"
        ], 
        [
            "debconf", 
            "| debconf-2.0"
        ], 
        [
            "locales"
        ]
    ], 
    "Architecture": "i386", 
    "Origin": "Ubuntu", 
    "Tasks": null, 
    "Maintainer": "Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>", 
    "Supported": "18m", 
    "Depends": [
        [
            "libc-bin", 
            "(= 2.15-0ubuntu20)"
        ], 
        [
            "libgcc1"
        ], 
        [
            "tzdata"
        ]
    ], 
    "Version": "2.15-0ubuntu20", 
    "Task": "minimal", 
    "Description-md5": "5089b4da6684d7432ab618fb5b79cec5", 
    "Size": "3940124"
}
>>> print adb.db['zsh'].__json__()
{
    "MD5sum": "275cb172c7193ec19a464180479db5c9", 
    "Section": "shells", 
    "Filename": "pool/main/z/zsh/zsh_5.0.0-2ubuntu1_i386.deb", 
    "Priority": "optional", 
    "Version": "5.0.0-2ubuntu1", 
    "Pre_Depends": null, 
    "Replaces": null, 
    "SHA256": "de31410c2d1f8f31e0bbf1e2cf30d34756bf8e807f2310815bb42d35db138d95", 
    "Homepage": "http://www.zsh.org/", 
    "Original-Maintainer": "Debian Zsh Maintainers <pkg-zsh-devel@lists.alioth.debian.org>", 
    "Recommends": [
        [
            "libncursesw5", 
            "(>= 5.6+20070908)"
        ], 
        [
            "libpcre3", 
            "(>= 8.10)"
        ]
    ], 
    "Description": "shell with lots of features", 
    "Breaks": null, 
    "Installed-Size": "11506", 
    "Conflicts": null, 
    "SHA1": "88019b9a7753c679469a7a26c6fc4946799f5855", 
    "Package": "zsh", 
    "Bugs": "https://bugs.launchpad.net/ubuntu/+filebug", 
    "Suggests": [
        [
            "zsh-doc"
        ]
    ], 
    "Architecture": "i386", 
    "Origin": "Ubuntu", 
    "Tasks": null, 
    "Maintainer": "Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>", 
    "Supported": "18m", 
    "Depends": [
        [
            "libc6", 
            "(>= 2.15)"
        ], 
        [
            "libcap2", 
            "(>= 2.10)"
        ], 
        [
            "libtinfo5"
        ]
    ], 
    "Description-md5": "a129d6b2d23d2d5d3a6b822d3f8f856d", 
    "Size": "4776376"
}
```

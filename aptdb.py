#!/usr/bin/env python
# This file is part of python-aptdb.

# python-aptdb is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# python-aptdb is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with python-aptdb.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright 2012-2013, Stijn Van Campenhout <stijn.vancampenhout@gmail.com>

import urllib2
import gzip
import json
import tempfile
import re
class AptPackage(object):
	def __init__(self,json):
		self.Changelog = None
		for k,v in json.items():
			if k.find('-') > -1:
				k = k.replace('-','_')
			setattr(self,k,v)
		if hasattr(self,'Depends'):
			if self.Depends == "":
				self.Depends == None
			else:
				self.Depends = [item.replace('(','').replace(')','').split(' ', 1) for item in self.Depends.split(', ')]
		else:
			setattr(self,'Depends',None)

		if hasattr(self,'Pre_Depends'):
			if self.Pre_Depends == "":
				self.Pre_Depends == None
			else:
				self.Pre_Depends = [item.replace('(','').replace(')','').split(' ', 1) for item in self.Pre_Depends.split(', ')]
		else:
			setattr(self,'Pre_Depends',None)

		if hasattr(self,'Suggests'):
			if self.Suggests == "":
				self.Suggests == None
			else:
				self.Suggests = [item.replace('(','').replace(')','').split(' ', 1) for item in self.Suggests.split(', ')]
		else:
			setattr(self,'Suggests',None)

		if hasattr(self,'Replaces'):
			if self.Replaces == "":
				self.Replaces == None
			else:
				self.Replaces = [item.replace('(','').replace(')','').split(' ', 1) for item in self.Replaces.split(', ')]
		else:
			setattr(self,'Replaces',None)

		if hasattr(self,'Conflicts'):
			if self.Conflicts == "":
				self.Conflicts == None
			else:
				self.Conflicts = [item.replace('(','').replace(')','').split(' ', 1) for item in self.Conflicts.split(', ')]
		else:
			setattr(self,'Conflicts',None)

		if hasattr(self,'Breaks'):
			if self.Breaks == "":
				self.Breaks == None
			else:
				self.Breaks = [item.replace('(','').replace(')','').split(' ', 1) for item in self.Breaks.split(', ')]
		else:
			setattr(self,'Breaks',None)

		if hasattr(self,'Recommends'):
			if self.Recommends == "":
				self.Recommends == None
			else:
				self.Recommends = [item.replace('(','').replace(')','').split(' ', 1) for item in self.Recommends.split(', ')]
		else:
			setattr(self,'Recommends',None)

		if hasattr(self,'Tasks'):
			if self.Tasks == "":
				self.Tasks == None
			else:
				self.Tasks = self.Tasks.split(', ')
		else:
			setattr(self,'Tasks',None)

	def __checkChangelog(self):
		if self.Changelog == None:
			if self.Changelog_Server:
				url = self.Changelog_Server + '/' + self.Filename.replace('_' + self.Architecture + '.deb','') + '/changelog'
				ul = urllib2.urlopen(url)
				changelog = ul.read()
				self.Changelog = self.__parseChangelog(changelog)
	def getChangelog(self):
		self.__checkChangelog()
		return self.Changelog
	def getCurrentChangelog(self):
		self.__checkChangelog()
		return self.Changelog[self.Version]
	def getChangelogVersion(self,version):
		self.__checkChangelog()
		return self.Changelog[version]

	def __parseChangelog(self,changelog):
		changelogs = {}
		currChangelog = {}
		regexStart = re.compile(self.Package + ' \((.*)\) ([a-zA-Z \s]+); (\w+)\=(\w+)')
		regexEnd = re.compile(' -- ([a-zA-Z \s]+) \<([A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]+)\>  (.*)')
		for line in changelog.split('\n'):
			if regexStart.match(line):
				res = regexStart.search(line).groups()
				currChangelog['Version'] = res[0]
				currChangelog['Release'] = res[1]
				currChangelog[res[2]] = res[3]
				currChangelog['Changelog'] = ""
			elif regexEnd.match(line):
				res = regexEnd.search(line).groups()
				currChangelog['Author'] = res[0]
				currChangelog['Author_Email'] = res[1]
				currChangelog['Date'] = res[2]
				changelogs[currChangelog['Version']] = currChangelog
				currChangelog = {}
			else:
				if currChangelog != {}:
					currChangelog['Changelog'] += line+"\n"
		return changelogs

	def __repr__(self):
		return "<AptPackage '" + self.Package + "' v" + str(self.Version) + ">"
	def __json__(self):
		return json.dumps(self.__dict__, indent=4)

class aptdb(object):
	def __init__(self,burl,dist,repo,arch,changelogserver=None):
		self.packages = {}
		self.url = burl + '/dists/' + dist + '/' + repo + '/binary-' + arch + '/Packages.gz'
		self.baseUrl = burl
		self.dist = dist
		self.repo = repo
		self.arch = arch
		self.changelogserver = changelogserver
		Pgz = self.fetch()
		self.load(Pgz)
		self.db = self.getPackages()
	def fetch(self):
		print "Downloading",self.url
		try:
			ul = urllib2.urlopen(self.url)
		except:
			print "error",e
		tmp = tempfile.gettempdir() + '/python-aptdb-Packages.gz'
		tmpfile = open(tmp,'wb')
		tmpfile.write(ul.read())
		tmpfile.close
		print "Done downloading"
		return tmp
	def load(self,PgzFile):
		print "Loading into database"
		Pgz = gzip.open(PgzFile)
		total = 0
		currPackage = {}
		for line in Pgz.readlines():
			if line == "\n":
				total = total + 1
				if self.changelogserver:
					currPackage['Changelog-Server'] = self.changelogserver
				self.packages[currPackage['Package']] = currPackage
				currPackage = {}
			else:
				l = line.split(': ')
				currPackage[l[0]] = l[1].strip('\n')
	def saveJson(self,file):
		fb = open(file,'wb')
		fb.write(json.dumps(self.packages, indent = 4))
		fb.close()
	def getPackages(self):
		print "Converting into AptPackage instances"
		pkgs = {}
		for package in self.packages:
			pkgs[package] = AptPackage(self.packages[package])
		return pkgs

#adb = aptdb("http://be.archive.ubuntu.com/ubuntu",'quantal','main','i386')
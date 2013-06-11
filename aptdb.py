#!/usr/bin/env python

import urllib2
import gzip
import json
import tempfile
class AptPackage(object):
	def __init__(self,json):
		for k,v in json.items():
			if k.find('-') > -1:
				k.replace('-','_')
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

	def __repr__(self):
		return "<AptPackage '" + self.Package + "' v" + str(self.Version) + ">"
	def __json__(self):
		return json.dumps(self.__dict__, indent=4)

class aptdb(object):
	def __init__(self,burl,dist,repo,arch):
		self.packages = {}
		self.url = burl + '/dists/' + dist + '/' + repo + '/binary-' + arch + '/Packages.gz'
		self.baseUrl = burl
		self.dist = dist
		self.repo = repo
		self.arch = arch
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
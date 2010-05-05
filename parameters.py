import os, sys

###sample configuration file
##host=localhost
##user=learn
##password=learn
##db=learn

###other sample configuration file
##INPUTFILE=xxx.dat
##DELIM=|
##FIELD,calledType=1
##FIELD,callingType=2

class Parameter:

	#-function to get all parameter on configuration file
	def getParams(self, cfgFile=None):
		isConf = lambda x: x.split(',')
		isName = lambda x: x.split('=')
		isFields = lambda x: x.split(',')

		fieldFlag = False
		params = {}
		fields = {}
		try:

			if cfgFile == None:
				return params

			cfg = open(cfgFile,'r')
			for line in cfg.xreadlines():
				line = line.strip()
				if line == '' or line == None:
					continue
				if self.isComment(line):
					continue
				else:
					configs = isName(line)

					if self.isField(configs[0]):
						tmpFields = isFields(configs[0])
						fields[tmpFields[1]] = int(configs[1])
						fieldFlag = True
					else:
						params[configs[0]] = configs[1]
						#-check for tab character
						if configs[1] == '\\t':
							params[configs[0]] = '\t'

			if fieldFlag:
				params['FIELDS'] = self.sort(fields)

		#except Exception, errmsg:
			#sys.stderr.write('Exception@getParams : ' + str(errmsg) + '\n')
		finally:
			cfg.close()
			return params

	#-sort dictionary function
	def sort(self, data):
		par = {}
		tmp = sorted(data.iteritems(), key=lambda (k,v):(v,k), reverse=True)
		for key, val in tmp:
			par[key] = val

		return par

	#-function to know that is comment
	def isComment(self, values):
		result = False
		try:
			if values.find('#') > -1:
				result = True
			else:
				result = False
		#except:
			#pass
		finally:
			return result

	#-function to know that is fields configuration
	def isField(self, values):
		result = False
		try:
			if values.find(',') > -1:
				result = True
			else:
				result = False
		#except:
			#pass
		finally:
			return result


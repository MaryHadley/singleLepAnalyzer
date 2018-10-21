import os,sys,fnmatch

templateDir='/user_data/ssagir/CMSSW_7_4_7/src/singleLepAnalyzer/x53x53_2016/makeTemplates/'
#templateDir+='templates_minMlb_2016_10_29' #Total number of jobs submitted: 3402
#templateDir+='templates_ST_2016_10_29' #Total number of jobs submitted: 4374
templateDir+='templates_M17WtSF_2017_3_31_SRpCR'
thetaConfigTemp = os.getcwd()+'/theta_config_template_noCRsys.py'
lumiInFile = '35p867fb'

toFilter0 = ['pdf','muR','muF','muRFcorrd','muRFcorrdNew','trigeff'] #always remove in case they are in templates
#toFilter0+= ['pileup','jec','jer','jms','jmr','tau21','taupt','topsf','toppt','pdfNew','trigeff','btag','mistag','topmuRFcorrdNew','ewkmuRFcorrdNew','qcdmuRFcorrdNew','ht']#,'jsf'
toFilter0 = ['__'+item+'__' for item in toFilter0]

catList = ['isE_nT0p_nW0p_nB1','isE_nT0p_nW0p_nB2p',
           'isE_nT0p_nW0_nB0','isE_nT0p_nW1p_nB0',
           'isE_nT0_nW0_nB1','isE_nT0_nW0_nB2p',
           'isE_nT0_nW1p_nB1','isE_nT0_nW1p_nB2p',
           'isE_nT1p_nW0_nB1','isE_nT1p_nW0_nB2p',
           'isE_nT1p_nW1p_nB1','isE_nT1p_nW1p_nB2p',
           ]
catList+=[item.replace('isE_','isM_') for item in catList]
catList = ['nT0p_nW0p_nB1','nT0p_nW0p_nB2p',
           'nT0p_nW0_nB0','nT0p_nW1p_nB0',
           'nT0_nW0_nB1','nT0_nW0_nB2p',
           'nT0_nW1p_nB1','nT0_nW1p_nB2p',
           'nT1p_nW0_nB1','nT1p_nW0_nB2p',
           'nT1p_nW1p_nB1','nT1p_nW1p_nB2p',
           ]

limitConfs = {#'<limit type>':[filter list]
# 			  'all_new':[],
# 			  'all_noJEC':['__jec__'],
# 			  'all_no1pT1pW1B':['_nT1p_nW1p_nB1_'],
# 			  'all_no1pT1pW2pB':['_nT1p_nW1p_nB2p_'],
			  'all_no1pT1pW':['_nT1p_nW1p_'],
# 			  'nT1p_nW1p_nB2p_noTopPt':[item for item in catList if item!='nT1p_nW1p_nB2p'],
# 			  'nT1p_nW1p_nB2p_noSyst':[item for item in catList if item!='nT1p_nW1p_nB2p'],
# 			  'isE':['isM'], #only electron channel
# 			  'isM':['isE'], #only muon channel
# 			  'nT0':['nT1p'], #only 0 t tag category
# 			  'nT1p':['nT0'], #only 1p t tag category
# 			  'nW0':['nW1p'], #only 0 W tag category
# 			  'nW1p':['nW0'], #only 1p W tag category
# 			  'nB1':['nB2p'], #only 1 b tag category
# 			  'nB2p':['nB1'], #only 2p b tag category
			  }
#for cat in catList: limitConfs[cat]=[item for item in catList if item!=cat]

limitType = '_test'#'_simulfit'
outputDir = '/user_data/ssagir/x53x53_limits_2016/'+templateDir.split('/')[-1]+limitType+'/' #prevent writing these (they are large) to brux6 common area
if not os.path.exists(outputDir): os.system('mkdir '+outputDir)
print outputDir

def findfiles(path, filtre):
    for root, dirs, files in os.walk(path):
        for f in fnmatch.filter(files, filtre):
            yield os.path.join(root, f)
            
rootfilelist = []
i=0
for rootfile in findfiles(templateDir, '*.root'):
    if 'rebinned_stat0p3.' not in rootfile: continue
    #if 'right' in rootfile: continue
    if 'plots' in rootfile: continue
    if 'YLD' in rootfile: continue
    #if 'minMlb' not in rootfile: continue
    #if 'X53X53M1300' in rootfile: continue
    #if 'X53X53M1400' in rootfile: continue
    #if 'X53X53M1500' in rootfile: continue
    #if 'X53X53M1600' in rootfile: continue
    rootfilelist.append(rootfile)
    i+=1

f = open(thetaConfigTemp, 'rU')
thetaConfigLines = f.readlines()
f.close()

def makeThetaConfig(rFile,outDir,toFilter):
	with open(outDir+'/'+rFile.split('/')[-1][:-5]+'.py','w') as fout:
		for line in thetaConfigLines:
			if line.startswith('input ='): fout.write('input = \''+rFile+'\'')
			elif line.startswith('    model = build_model_from_rootfile('): 
				if len(toFilter)!=0:
					model='    model = build_model_from_rootfile(input,include_mc_uncertainties=True,histogram_filter = (lambda s:  s.count(\''+toFilter[0]+'\')==0'
					for item in toFilter: 
						if item!=toFilter[0]: model+=' and s.count(\''+item+'\')==0'
					model+='))'
					fout.write(model)
				else: fout.write(line)
			else: fout.write(line)
	with open(outDir+'/'+rFile.split('/')[-1][:-5]+'.sh','w') as fout:
		fout.write('#!/bin/sh \n')
		fout.write('cd /home/ssagir/CMSSW_7_3_0/src/\n')
		fout.write('source /cvmfs/cms.cern.ch/cmsset_default.sh\n')
		fout.write('cmsenv\n')
		fout.write('cd '+outDir+'\n')
		fout.write('/home/ssagir/CMSSW_7_3_0/src/theta/utils2/theta-auto.py ' + outDir+'/'+rFile.split('/')[-1][:-5]+'.py')

count=0
for limitConf in limitConfs:
	toFilter = toFilter0 + limitConfs[limitConf]
	print limitConf,'=',toFilter
	for file in rootfilelist:
		fileName = file.split('/')[-1]
		signal = fileName.split('_')[2]
		BRStr = fileName[fileName.find(signal)+len(signal):fileName.find('_'+lumiInFile)]
		outDir = outputDir+limitConf+BRStr+'/'
		print signal,BRStr
		if not os.path.exists(outDir): os.system('mkdir '+outDir)
		os.chdir(outDir)
		fileDir = ''
		if templateDir.split('/')[-1]!=file.split('/')[-2]:
			fileDir = file.split('/')[-2]
			if not os.path.exists(outDir+fileDir): os.system('mkdir '+fileDir)
			os.chdir(fileDir)
		outDir=outDir+fileDir
		makeThetaConfig(file,outDir,toFilter)

		dict={'configdir':outDir,'configfile':file.split('/')[-1][:-5]}

		jdf=open(file.split('/')[-1][:-5]+'.job','w')
		jdf.write(
"""universe = vanilla
Executable = %(configfile)s.sh
Should_Transfer_Files = YES
WhenToTransferOutput = ON_EXIT
Notification = Error
request_memory = 3072
Output = %(configfile)s.out
Error = %(configfile)s.err
Log = %(configfile)s.log

Queue 1"""%dict)
		jdf.close()

		os.system('chmod +x '+file.split('/')[-1][:-5]+'.sh')
		os.system('condor_submit '+file.split('/')[-1][:-5]+'.job')
		os.chdir('..')
		count+=1
print "Total number of jobs submitted:", count
                  

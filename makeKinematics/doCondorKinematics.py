import os,sys,datetime

thisDir = os.getcwd()
outputDir = thisDir+'/'

cutConf = 'finalSel' #'preSel', 'finalSel', or 'finalSelnoDR'

cTime=datetime.datetime.now()
date='%i_%i_%i'%(cTime.year,cTime.month,cTime.day)
time='%i_%i_%i'%(cTime.hour,cTime.minute,cTime.second)
pfix='kinematics_'+cutConf+'_noJSF'
pfix+='_'+date#+'_'+time

plotList = [#distribution name as defined in "doHists.py"
			'NPV',
			'lepPt',
			'lepEta',
			'JetEta',
			'JetPt' ,
			'Jet1Pt',
			'Jet2Pt',
			'Jet3Pt',
			'Jet4Pt',
			'Jet5Pt',
			'Jet6Pt',
			'HT',
			'ST',
			'MET',
			'NJets' ,
			'NBJets',
			'NWJets',
			'NJetsAK8',
			'JetPtAK8',
			'JetEtaAK8',
			'Tau21',
			'Tau32',
			'mindeltaR',
			'deltaRjet1',
			'deltaRjet2',
			'deltaRjet3',
			'PtRel',
			'PrunedSmeared',
			'SDMass',
			'NTJetsSF',
			'minMlb',
			]

catList = ['E','M','L']

outDir = outputDir+pfix
if not os.path.exists(outDir): os.system('mkdir '+outDir)
os.system('cp ../analyze.py doHists.py ../weights.py ../samples.py ../utils.py doCondorKinematics.py doCondorKinematics.sh '+outDir+'/')
os.chdir(outDir)

count = 0
for distribution in plotList:
	for cat in catList:
		print cat
		if not os.path.exists(outDir+'/'+cat): os.system('mkdir '+cat)
		os.chdir(cat)
		
		dict={'dir':outputDir,'dist':distribution,'cat':cat,'cut':cutConf}

		jdf=open('condor_'+distribution+'.job','w')
		jdf.write(
"""universe = vanilla
Executable = %(dir)s/doCondorKinematics.sh
Should_Transfer_Files = YES
transfer_input_files = %(dir)s/doHists.py,%(dir)s/../samples.py,%(dir)s/../weights.py,%(dir)s/../analyze.py,%(dir)s/../utils.py
WhenToTransferOutput = ON_EXIT
request_memory = 3072
arguments = ""
Output = condor_%(dist)s.out
Error = condor_%(dist)s.err
Log = condor_%(dist)s.log
Notification = Error
Arguments = %(dir)s %(dist)s %(cat)s %(cut)s

Queue 1"""%dict)
		jdf.close()

		os.system('condor_submit condor_'+distribution+'.job')
		os.chdir('..')
		count+=1
									
print "Total jobs submitted:", count             

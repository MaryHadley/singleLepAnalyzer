import os,sys,datetime,itertools

#Basic kinematic cuts optimization configuration (w/o shapes) -- minMlb -- x53x53/2016 dataset (Total jobs submitted: 9072):
# lepPtCutList  = [30, 50, 60, 80, 100, 150]
# jet1PtCutList = [50, 100, 150, 200, 250, 300, 450]
# jet2PtCutList = [30, 50, 90, 150, 300]
# metCutList    = [30, 50, 80, 100, 150, 200, 250]
# njetsCutList  = [3, 4, 5]
# nbjetsCutList = [0]
# jet3PtCutList = [0]
# jet4PtCutList = [0]
# jet5PtCutList = [0]
# drCutList     = [0.75, 1, 1.25]
# Wjet1PtCutList= [0]
# bjet1PtCutList= [0]
# htCutList     = [0]
# stCutList     = [0]
# minMlbCutList = [0]
#Basic kinematic cuts optimization configuration (w/o shapes) -- ST -- x53x53/2016 dataset (Total jobs submitted: 2340):
lepPtCutList  = [30, 50, 60, 80]
jet1PtCutList = [200, 250, 300, 450]
jet2PtCutList = [50, 90, 150, 300]
metCutList    = [80, 100, 150, 200, 250]
njetsCutList  = [3, 4, 5]
nbjetsCutList = [0]
jet3PtCutList = [0]
jet4PtCutList = [0]
jet5PtCutList = [0]
drCutList     = [0.75, 1, 1.25]
Wjet1PtCutList= [0]
bjet1PtCutList= [0]
htCutList     = [0]
stCutList     = [0]
minMlbCutList = [0]

cutConfigs = list(itertools.product(lepPtCutList,jet1PtCutList,jet2PtCutList,metCutList,njetsCutList,nbjetsCutList,jet3PtCutList,jet4PtCutList,jet5PtCutList,drCutList,Wjet1PtCutList,bjet1PtCutList,htCutList,stCutList,minMlbCutList))

thisDir = os.getcwd()
outputDir = thisDir+'/'

cTime=datetime.datetime.now()
date='%i_%i_%i'%(cTime.year,cTime.month,cTime.day)
time='%i_%i_%i'%(cTime.hour,cTime.minute,cTime.second)
pfix='templates_ST'
pfix+='_'+date#+'_'+time

outDir = outputDir+pfix
if not os.path.exists(outDir): os.system('mkdir '+outDir)

count=0
for conf in cutConfigs:
	lepPtCut,jet1PtCut,jet2PtCut,metCut,njetsCut,nbjetsCut,jet3PtCut,jet4PtCut,jet5PtCut,drCut,Wjet1PtCut,bjet1PtCut,htCut,stCut,minMlbCut=conf[0],conf[1],conf[2],conf[3],conf[4],conf[5],conf[6],conf[7],conf[8],conf[9],conf[10],conf[11],conf[12],conf[13],conf[14]
	if jet2PtCut >= jet1PtCut or jet3PtCut >= jet1PtCut or jet4PtCut >= jet1PtCut or jet5PtCut >= jet1PtCut: continue
	if jet3PtCut >= jet2PtCut or jet4PtCut >= jet2PtCut or jet5PtCut >= jet2PtCut: continue
	if (jet4PtCut >= jet3PtCut or jet5PtCut >= jet3PtCut) and jet3PtCut!=0: continue
	if jet5PtCut >= jet4PtCut and jet4PtCut!=0: continue
	cutString = 'lep'+str(int(lepPtCut))+'_MET'+str(int(metCut))+'_NJets'+str(int(njetsCut))+'_NBJets'+str(int(nbjetsCut))+'_DR'+str(drCut)
	cutString+= '_1jet'+str(int(jet1PtCut))+'_2jet'+str(int(jet2PtCut))+'_3jet'+str(int(jet3PtCut))#+'_4jet'+str(int(jet4PtCut))+'_5jet'+str(int(jet5PtCut))
	#cutString+= '_1Wjet'+str(Wjet1PtCut)+'_1bjet'+str(bjet1PtCut)+'_HT'+str(htCut)+'_ST'+str(stCut)+'_minMlb'+str(minMlbCut)
	os.chdir(outDir)
	print cutString
	if not os.path.exists(outDir+'/'+cutString): os.system('mkdir '+cutString)
	os.chdir(cutString)

	dict={'dir':outputDir,'lepPtCut':lepPtCut,'jet1PtCut':jet1PtCut,'jet2PtCut':jet2PtCut,
		  'metCut':metCut,'njetsCut':njetsCut,'nbjetsCut':nbjetsCut,'jet3PtCut':jet3PtCut,
		  'jet4PtCut':jet4PtCut,'jet5PtCut':jet5PtCut,'drCut':drCut,'Wjet1PtCut':Wjet1PtCut,
		  'bjet1PtCut':bjet1PtCut,'htCut':htCut,'stCut':stCut,'minMlbCut':minMlbCut}

	jdf=open('condor.job','w')
	jdf.write(
"""universe = vanilla
Executable = %(dir)s/doCondorThetaTemplates.sh
Should_Transfer_Files = YES
WhenToTransferOutput = ON_EXIT
request_memory = 3072

arguments      = ""

Output = condor.out
Error = condor.err
Log = condor.log
Notification = Error
Arguments = %(dir)s %(lepPtCut)s %(jet1PtCut)s %(jet2PtCut)s %(metCut)s %(njetsCut)s %(nbjetsCut)s %(jet3PtCut)s %(jet4PtCut)s %(jet5PtCut)s %(drCut)s %(Wjet1PtCut)s %(bjet1PtCut)s %(htCut)s %(stCut)s %(minMlbCut)s

Queue 1"""%dict)
	jdf.close()

	os.system('condor_submit condor.job')
	os.chdir('..')
	count+=1
									
print "Total jobs submitted:", count



                  
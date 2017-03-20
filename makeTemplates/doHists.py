#!/usr/bin/python

import os,sys,time,math,datetime,pickle,itertools,getopt
from ROOT import TH1D,gROOT,TFile,TTree
parent = os.path.dirname(os.getcwd())
sys.path.append(parent)
from numpy import linspace
import argparse
from weights import *
from analyze import *
from samples import *
from utils import *

gROOT.SetBatch(1)
start_time = time.time()

# parser = argparse.ArgumentParser(description='Welcome to singleLepAnalyzer!')
# parser.add_argument('-i','--input', help='Input file name',required=True)
# parser.add_argument('-o','--output',help='Output file name', required=True)
# args = parser.parse_args()

lumiStr = str(targetlumi/1000).replace('.','p') # 1/fb
step1Dir = '/user_data/jlee/chargedHiggs/LHCP2017/TTbar/BDTGhalfTT_Brown_16vars_MLowMedHigh/nominal'
"""
Note: 
--Each process in step1 (or step2) directories should have the root files hadded! 
--The code will look for <step1Dir>/<process>_hadd.root for nominal trees.
The uncertainty shape shifted files will be taken from <step1Dir>/../<shape>/<process>_hadd.root,
where <shape> is for example "JECUp". hadder.py can be used to prepare input files this way! 
--Each process given in the lists below must have a definition in "samples.py"
--Check the set of cuts in "analyze.py"
"""	
bkgList = [
		  'DYMG',
		  #'WJetsMG',
		  'WJetsHT100','WJetsHT200','WJetsHT400','WJetsHT600','WJetsHT800','WJetsHT1200','WJetsHT2500',
          #'WJetsMGPt100','WJetsMGPt250','WJetsMGPt400','WJetsMGPt600',
		  #'WW','WZ','ZZ',
		  'TTJetsPH700to1000inc', 'TTJetsPH1000toINFinc','TTJetsPH700mtt','TTJetsPH1000mtt',
		  'TTWl','TTWq','TTZl','TTZq',
		  'Tt','Tbt','Ts','TtW','TbtW',
		  'QCDht100','QCDht200','QCDht300','QCDht500','QCDht700','QCDht1000','QCDht1500','QCDht2000',
		  ]
for ind in range(1,12): bkgList.append('TTJetsPH0to700inc_'+str(ind))
#for ind in range(1,14): bkgList.append('TTJetsPHSL_'+str(ind))
ttFlvs = ['_ttflv','_ttbbflv','_ttbjflv','_ttccflv','_ttcjflv','_ttllflv','_ttlfflv']
dataList = ['DataERRB2H','DataMRRB2H']

whichSignal = 'HTB' #HTB, TT, BB, or X53X53
#massList = range(180,200+1,20)+range(250,500+1,50)+[750,800,1000,2000,3000]
massList = [180,200,220,250,300,400,500,800,1000,2000,3000]
sigList = [whichSignal+'M'+str(mass) for mass in massList]
if whichSignal=='X53X53': sigList = [whichSignal+'M'+str(mass)+chiral for mass in massList for chiral in ['left','right']]
if whichSignal=='TT': decays = ['BWBW','THTH','TZTZ','TZBW','THBW','TZTH'] #T' decays
if whichSignal=='BB': decays = ['TWTW','BHBH','BZBZ','BZTW','BHTW','BZBH'] #B' decays
if whichSignal=='X53X53': decays = [''] #decays to tWtW 100% of the time
if whichSignal=='HTB': decays = ['']

sigTrained = 'Low'
if len(sys.argv)>10: sigTrained=sys.argv[10]
iPlot = 'minMlbpBDT' #choose a discriminant from plotList below!
if len(sys.argv)>2: iPlot=sys.argv[2]
region = 'SR'
if len(sys.argv)>3: region=sys.argv[3]
isCategorized = 1
if len(sys.argv)>4: isCategorized=int(sys.argv[4])
doJetRwt= 0
doAllSys= False
doQ2sys = False
q2List  = [#energy scale sample to be processed
	       'TTJetsPHQ2U','TTJetsPHQ2D',
	       #'TtWQ2U','TbtWQ2U',
	       #'TtWQ2D','TbtWQ2D',
	       ]

cutList = {'lepPtCut':35,'metCut':30,'drCut':0,'jet1PtCut':40,'jet2PtCut':40,'jet3PtCut':0}

cutString  = 'lep'+str(int(cutList['lepPtCut']))+'_MET'+str(int(cutList['metCut']))
#cutString += '_NJets'+str(int(cutList['njetsCut']))
#cutString += '_NBJets'+str(int(cutList['nbjetsCut']))
cutString += '_DR'+str(cutList['drCut'])+'_1jet'+str(int(cutList['jet1PtCut']))
cutString += '_2jet'+str(int(cutList['jet2PtCut']))#+'_3jet'+str(int(cutList['jet3PtCut']))
# cutString += '_4jet'+str(int(cutList['jet4PtCut']))+'_5jet'+str(int(cutList['jet5PtCut']))
# cutString += '_1Wjet'+str(cutList['Wjet1PtCut'])+'_1bjet'+str(cutList['bjet1PtCut'])
# cutString += '_HT'+str(cutList['htCut'])+'_ST'+str(cutList['stCut'])+'_minMlb'+str(cutList['minMlbCut'])

cTime=datetime.datetime.now()
datestr='%i_%i_%i'%(cTime.year,cTime.month,cTime.day)
timestr='%i_%i_%i'%(cTime.hour,cTime.minute,cTime.second)
pfix='templates'
if not isCategorized: pfix='kinematics_'+region
pfix+='_'+datestr#+'_'+timestr
		
if len(sys.argv)>5: isEMlist=[str(sys.argv[5])]
else: isEMlist = ['E','M']
if len(sys.argv)>6: nttaglist=[str(sys.argv[6])]
else: nttaglist = ['0p']
if len(sys.argv)>7: nWtaglist=[str(sys.argv[7])]
else: nWtaglist = ['0p']
if len(sys.argv)>8: nbtaglist=[str(sys.argv[8])]
else: 
	if not isCategorized: nbtaglist = ['2p']
	else: nbtaglist = ['1','2','2p','3p']
if len(sys.argv)>9: njetslist=[str(sys.argv[9])]
else:
	if not isCategorized: njetslist = ['2p']
	else: njetslist = ['3','4','5','6p']

catList = list(itertools.product(isEMlist,nttaglist,nWtaglist,nbtaglist,njetslist))

def readTree(file):
	if not os.path.exists(file): 
		print "Error: File does not exist! Aborting ...",file
		os._exit(1)
	tFile = TFile(file,'READ')
	tTree = tFile.Get('ljmet')
	return tFile, tTree 

print "READING TREES"
shapesFiles = ['jec','jer']
tTreeData = {}
tFileData = {}
for data in dataList:
	print "READING:", data
	tFileData[data],tTreeData[data]=readTree(step1Dir+'/'+samples[data]+'_hadd.root')

tTreeSig = {}
tFileSig = {}
for sig in sigList:
	for decay in decays:
		print "READING:", sig+decay
		print "        nominal"
		tFileSig[sig+decay],tTreeSig[sig+decay]=readTree(step1Dir+'/'+samples[sig+decay]+'_hadd.root')
		if doAllSys:
			for syst in shapesFiles:
				for ud in ['Up','Down']:
					print "        "+syst+ud
					tFileSig[sig+decay+syst+ud],tTreeSig[sig+decay+syst+ud]=readTree(step1Dir.replace('nominal',syst.upper()+ud.lower())+'/'+samples[sig+decay]+'_hadd.root')

tTreeBkg = {}
tFileBkg = {}
for bkg in bkgList+q2List:
	if bkg in q2List and not doQ2sys: continue
	print "READING:",bkg
	print "        nominal"
	tFileBkg[bkg],tTreeBkg[bkg]=readTree(step1Dir+'/'+samples[bkg]+'_hadd.root')
	if doAllSys:
		for syst in shapesFiles:
			for ud in ['Up','Down']:
				if bkg in q2List:
					tFileBkg[bkg+syst+ud],tTreeBkg[bkg+syst+ud]=None,None
				else:
					print "        "+syst+ud
					tFileBkg[bkg+syst+ud],tTreeBkg[bkg+syst+ud]=readTree(step1Dir.replace('nominal',syst.upper()+ud.lower())+'/'+samples[bkg]+'_hadd.root')
print "FINISHED READING"

bigbins = [0,50,100,150,200,250,300,350,400,450,500,600,700,800,1000,1200,1500]
#bigbins = [0,50,100,125,150,175,200,225,250,275,300,325,350,375,400,450,500,600,700,800,900,1000,1200,1400,1600,1800,2000,2500,3000,3500,4000,5000]

plotList = {#discriminantName:(discriminantLJMETName, binning, xAxisLabel)
	'NPV':('nPV_singleLepCalc',linspace(0, 40, 41).tolist(),';PV multiplicity'),
	'MTlmet':('MT_lepMet',linspace(0,250,51).tolist(),';M_{T}(l,#slash{E}_{T}) [GeV]'),
	'topPt':('topPt',linspace(0,1500,51).tolist(),';p_{T}^{rec}(t) [GeV]'),
	'Bjet1Pt':('BJetLeadPt',linspace(0,1500,51).tolist(),';p_{T}(b_{1}) [GeV]'),
	'lepPt':('leptonPt_singleLepCalc',linspace(0, 1000, 51).tolist(),';Lepton p_{T} [GeV]'),
	'lepEta':('leptonEta_singleLepCalc',linspace(-4, 4, 41).tolist(),';Lepton #eta'),
	'JetEta':('theJetEta_JetSubCalc_PtOrdered',linspace(-4, 4, 41).tolist(),';AK4 Jet #eta'),
	'JetPt' :('theJetPt_JetSubCalc_PtOrdered',linspace(0, 1500, 51).tolist(),';jet p_{T} [GeV]'),
	'Jet1Pt':('theJetPt_JetSubCalc_PtOrdered[0]',linspace(0, 1500, 51).tolist(),';p_{T}(j_{1}), AK4 [GeV]'),
	'Jet2Pt':('theJetPt_JetSubCalc_PtOrdered[1]',linspace(0, 1500, 51).tolist(),';p_{T}(j_{2}), AK4 [GeV]'),
	'Jet3Pt':('theJetPt_JetSubCalc_PtOrdered[2]',linspace(0, 800, 51).tolist(),';p_{T}(j_{3}), AK4 [GeV]'),
	'deltaPhilepJets0':('deltaPhi_lepJets0',linspace(0,3.2,51).tolist(),';#Delta#phi(l,j_{1})'),
	'deltaPhilepJets1':('deltaPhi_lepJets1',linspace(0,3.2,51).tolist(),';#Delta#phi(l,j_{2})'),
	'deltaPhilepJets2':('deltaPhi_lepJets2',linspace(0,3.2,51).tolist(),';#Delta#phi(l,j_{3})'),
	'deltaRlepJets0':('deltaR_lepJets0',linspace(0,6,51).tolist(),';#DeltaR(l,j_{1})'),
	'deltaRlepJets1':('deltaR_lepJets1',linspace(0,6,51).tolist(),';#DeltaR(l,j_{2})'),
	'deltaRlepJets2':('deltaR_lepJets2',linspace(0,6,51).tolist(),';#DeltaR(l,j_{3})'),
	'deltaR_lepBJets0':('deltaR_lepBJets0',linspace(0,6,51).tolist(),';#DeltaR(l,b_{1})'),
	'mindeltaRlb':('minDR_lepBJet',linspace(0,6,51).tolist(),';min[#DeltaR(l,b)]'),
	'masslepJets0':('mass_lepJets0',linspace(0,1000,51).tolist(),';M(l,j_{1}) [GeV]'),
	'masslepJets1':('mass_lepJets1',linspace(0,1000,51).tolist(),';M(l,j_{2}) [GeV]'),
	'masslepJets2':('mass_lepJets2',linspace(0,1000,51).tolist(),';M(l,j_{3}) [GeV]'),
	'masslepBJets0':('mass_lepBJet0',linspace(0,1000,51).tolist(),';M(l,b_{1}) [GeV]'),
	'mindeltaR':('minDR_lepJet',linspace(0, 6, 51).tolist(),';min[#DeltaR(l,j)]'),
	'MET':('corr_met_singleLepCalc',linspace(0, 1500, 51).tolist(),';#slash{E}_{T} [GeV]'),
	'NJets':('NJets_JetSubCalc',linspace(0, 15, 16).tolist(),';jet multiplicity'),
	'NBJetsNoSF':('NJetsCSV_JetSubCalc',linspace(0, 10, 11).tolist(),';b tag multiplicity'),
	'NBJets':('NJetsCSVwithSF_JetSubCalc',linspace(0, 10, 11).tolist(),';b tag multiplicity'),
	'PtRel':('ptRel_lepJet',linspace(0,500,51).tolist(),';p_{T,rel}(l, closest jet) [GeV]'),
	'LeadJetPt':('theJetLeadPt',linspace(0, 1500, 51).tolist(),';p_{T}(j_{1}) [GeV]'),
	'aveBBdr':('aveBBdr',linspace(0, 6, 51).tolist(),';#bar{#DeltaR(b,b)}'),
	'minBBdr':('minBBdr',linspace(0, 6, 51).tolist(),';min[#DeltaR(b,b)]'),
	'mass_maxJJJpt':('mass_maxJJJpt',linspace(0, 3000, 51).tolist(),';M(jjj) with max[p_{T}(jjj)] [GeV]'),
	'mass_maxBBmass':('mass_maxBBmass',linspace(0, 1500, 51).tolist(),';max[M(b,b)] [GeV]'),
	'mass_maxBBpt':('mass_maxBBpt',linspace(0, 1500, 51).tolist(),';M(b,b) with max[p_{T}(bb)] [GeV]'),
	'lepDR_minBBdr':('lepDR_minBBdr',linspace(0, 6, 51).tolist(),';#DeltaR(l,bb) with min[#DeltaR(b,b)]'),
	'mass_minBBdr':('mass_minBBdr',linspace(0, 1000, 51).tolist(),';M(b,b) with min[#DeltaR(b,b)] [GeV]'),
	'mass_minLLdr':('mass_minLLdr',linspace(0, 1000, 51).tolist(),';M(j,j) with min[#DeltaR(j,j)], j #neq b [GeV]'),
 	'mass_lepBB_minBBdr':('mass_lepBB_minBBdr',linspace(0, 1000, 51).tolist(),';M(l,bb) with min[#DeltaR(b,b)] [GeV]'),
	'mass_lepJJ_minJJdr':('mass_lepJJ_minJJdr',linspace(0, 1000, 51).tolist(),';M(l,jj) with min[#DeltaR(j,j)], j #neq b [GeV]'),

    'HT':('AK4HT',linspace(0, 3000, 51).tolist(),';H_{T} [GeV]'),
 	'ST':('AK4HTpMETpLepPt',linspace(0, 3000, 51).tolist(),';S_{T} [GeV]'),
	'minMlb':('minMleppBjet',linspace(0, 1000, 51).tolist(),';min[M(l,b)] [GeV]'),
	'BDT':('BDT'+sigTrained,linspace(-1, 1, 37).tolist(),';BDT'),
	
	'STpBDT':('AK4HTpMETpLepPt',linspace(0, 3000, 51).tolist(),';S_{T} [GeV]','BDT'+sigTrained,linspace(-1, 1, 37).tolist(),';BDT'),
	'HTpBDT':('AK4HT',linspace(0, 3000, 51).tolist(),';H_{T} [GeV]','BDT'+sigTrained,linspace(-1, 1, 37).tolist(),';BDT'),
	'minMlbpBDT':('minMleppBjet',linspace(0, 1000, 51).tolist(),';min[M(l,b)] [GeV]','BDT'+sigTrained,linspace(-1, 1, 37).tolist(),';BDT'),

	'NJets_vs_NBJets':('NJets_JetSubCalc:NJetsCSV_JetSubCalc',linspace(0, 15, 16).tolist(),';jet multiplicity',linspace(0, 10, 11).tolist(),';b tag multiplicity'),
	}
#plotList[iPlot][0] = plotList[iPlot][0]+str(massList[0])
print "PLOTTING:",iPlot
print "         LJMET Variable:",plotList[iPlot][0]
print "         X-AXIS TITLE  :",plotList[iPlot][2]
print "         BINNING USED  :",plotList[iPlot][1]

runData = True
runBkgs = True
runSigs = True
nCats  = len(catList)

catInd = 1
for cat in catList:
 	if not runData: break
 	if skip(cat[4],cat[3]) and isCategorized: continue #DO YOU WANT TO HAVE THIS??
 	catDir = cat[0]+'_nT'+cat[1]+'_nW'+cat[2]+'_nB'+cat[3]+'_nJ'+cat[4]
 	datahists = {}
 	if len(sys.argv)>1: outDir=sys.argv[1]
 	else: 
		outDir = os.getcwd()
		outDir+='/'+pfix
		if not os.path.exists(outDir): os.system('mkdir '+outDir)
		outDir+='/'+cutString
		if not os.path.exists(outDir): os.system('mkdir '+outDir)
		outDir+='/'+catDir
		if not os.path.exists(outDir): os.system('mkdir '+outDir)
 	category = {'isEM':cat[0],'nttag':cat[1],'nWtag':cat[2],'nbtag':cat[3],'njets':cat[4]}
 	for data in dataList: 
 		datahists.update(analyze(tTreeData,data,data,cutList,False,doJetRwt,iPlot,plotList[iPlot],category,region,isCategorized))
 		if catInd==nCats: del tFileData[data]
 	pickle.dump(datahists,open(outDir+'/datahists_'+iPlot+'.p','wb'))
 	catInd+=1

catInd = 1
for cat in catList:
 	if not runBkgs: break
 	if skip(cat[4],cat[3]) and isCategorized: continue #DO YOU WANT TO HAVE THIS??
 	catDir = cat[0]+'_nT'+cat[1]+'_nW'+cat[2]+'_nB'+cat[3]+'_nJ'+cat[4]
 	bkghists  = {}
 	if len(sys.argv)>1: outDir=sys.argv[1]
 	else: 
		outDir = os.getcwd()
		outDir+='/'+pfix
		if not os.path.exists(outDir): os.system('mkdir '+outDir)
		outDir+='/'+cutString
		if not os.path.exists(outDir): os.system('mkdir '+outDir)
		outDir+='/'+catDir
		if not os.path.exists(outDir): os.system('mkdir '+outDir)
 	category = {'isEM':cat[0],'nttag':cat[1],'nWtag':cat[2],'nbtag':cat[3],'njets':cat[4]}
 	for bkg in bkgList: 
 		bkghists.update(analyze(tTreeBkg,bkg,bkg,cutList,doAllSys,doJetRwt,iPlot,plotList[iPlot],category,region,isCategorized))
 		if 'TTJets' in bkg and len(ttFlvs)!=0:
 			for flv in ttFlvs: bkghists.update(analyze(tTreeBkg,bkg,bkg+flv,cutList,doAllSys,doJetRwt,iPlot,plotList[iPlot],category,region,isCategorized))
 		if catInd==nCats: del tFileBkg[bkg]
 		if doAllSys and catInd==nCats:
 			for syst in shapesFiles:
 				for ud in ['Up','Down']: del tFileBkg[bkg+syst+ud]
 	if doQ2sys: 
 		for q2 in q2List: 
 			bkghists.update(analyze(tTreeBkg,q2,q2,cutList,False,doJetRwt,iPlot,plotList[iPlot],category,region,isCategorized))
 			if catInd==nCats: del tFileBkg[q2]
	pickle.dump(bkghists,open(outDir+'/bkghists_'+iPlot+'.p','wb'))
 	catInd+=1

catInd = 1
for cat in catList:
 	if not runSigs: break
 	if skip(cat[4],cat[3]) and isCategorized: continue #DO YOU WANT TO HAVE THIS??
 	catDir = cat[0]+'_nT'+cat[1]+'_nW'+cat[2]+'_nB'+cat[3]+'_nJ'+cat[4]
 	sighists  = {}
 	if len(sys.argv)>1: outDir=sys.argv[1]
 	else: 
		outDir = os.getcwd()
		outDir+='/'+pfix
		if not os.path.exists(outDir): os.system('mkdir '+outDir)
		outDir+='/'+cutString
		if not os.path.exists(outDir): os.system('mkdir '+outDir)
		outDir+='/'+catDir
		if not os.path.exists(outDir): os.system('mkdir '+outDir)
 	category = {'isEM':cat[0],'nttag':cat[1],'nWtag':cat[2],'nbtag':cat[3],'njets':cat[4]}
 	for sig in sigList: 
 		for decay in decays: 
 			sighists.update(analyze(tTreeSig,sig+decay,sig+decay,cutList,doAllSys,doJetRwt,iPlot,plotList[iPlot],category,region,isCategorized))
 			if catInd==nCats: del tFileSig[sig+decay]
 			if doAllSys and catInd==nCats:
 				for syst in shapesFiles:
 					for ud in ['Up','Down']: del tFileSig[sig+decay+syst+ud]
	pickle.dump(sighists,open(outDir+'/sighists_'+iPlot+'.p','wb'))
 	catInd+=1

print("--- %s minutes ---" % (round((time.time() - start_time)/60,2)))


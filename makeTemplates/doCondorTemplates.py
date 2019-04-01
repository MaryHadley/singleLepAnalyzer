import os,sys,datetime,itertools

thisDir = os.getcwd()
outputDir = thisDir+'/'

region='PS' #PS,SR,TTCR,WJCR
categorize=0 #1==categorize into t/W/b/j, 0==only split into flavor # don't do this for PS

cTime=datetime.datetime.now()
date='%i_%i_%i'%(cTime.year,cTime.month,cTime.day)
time='%i_%i_%i'%(cTime.hour,cTime.minute,cTime.second)
if region=='TTCR': pfix='ttbar'
elif region=='WJCR': pfix='wjets'
else: pfix='templates'
if not categorize: pfix='kinematics_'+region
pfix+='_'+date#+'_'+time

iPlotList = [#distribution name as defined in "doHists.py"
			# 'lepPt',
# 			'lepEta',
# 			'deltaRjet1',
# 			'deltaRjet2',
# 			'deltaRjet3',
# 			'NPV',
# 			'JetEta',
# 			'JetPt',
# 			'Jet1Pt',
# 			'Jet2Pt',
# 			'Jet3Pt',
# 			'Jet4Pt',
# 			'MET',
# 			'NJets',
# 			'NBJets',
# 			'NWJets',
# 			'NTJets',
# 			'NJetsAK8',
# 			'JetPtAK8',
# 			'JetEtaAK8',
# 			'Tau21',
# 			'Tau21Nm1',
# 			'Tau32',
# 			'Tau32Nm1',
# 			'SoftDropMass', 
# 			'SoftDropMassNm1W',
# 			'SoftDropMassNm1t',
# 			'mindeltaR',
# 			'PtRel',
# 			
# 			'HT',
# 			'ST',
# 			'minMlb',
# # 			'minMlbSBins',
# 
# # 			'NJets_vs_NBJets',
# 
# 			'NBJetsNoSF',
# 			'nTrueInt',
# 	        'MTlmet',
# 			'minMlj',
# 			'lepIso',
# # 			'deltaRAK8',
# # 			'Bjet1Pt',
# # 			'Wjet1Pt',
# # 			'Tjet1Pt',
# # 			'deltaPhiLMET',	
#  			'Jet5Pt',
#  			'Jet6Pt',
# # 			'JetPtBins',
# # 			'Jet1PtBins',
# # 			'Jet2PtBins',
# # 			'Jet3PtBins',
# # 			'Jet4PtBins',
# # 			'Jet5PtBins',
# # 			'Jet6PtBins',
# # 			'JetPtBinsAK8',
# # 			'minMljDR',
# # 			'minMljDPhi',
# # 			'minMlbDR',
# # 			'minMlbDPhi',
# # 			'topPt',
# # 			'topMass',
# # 			'nLepGen',
# # 			'METphi',
# # 			'lepPhi',
# # 			'lepDxy',
# # 			'lepDz',
# # 			'lepCharge',
# # 			'Tau1',
# # 			'Tau2',
# # 			'Tau3',
# # 			'JetPhi',
# # 			'JetPhiAK8',
#                         'HT_b',
#                         'HT_ratio',
#                         'HT_2m',
#                         'Centrality',
#                         'thirdcsvb_bb',
#                         'fourthcsvb_bb',
#                         'csvJet3',
#                         'csvJet4',
#                         'HTx',
#                         'MHRE',
#                         'GD_Ttrijet_TopMass',
#                         'BD_Ttrijet_TopMass',
#                         'GD_DCSV_jetNotdijet',
#                         'GD_DR_Tridijet',
#                         'BD_DR_Tridijet',
#                         'GD_DR_Trijet_jetNotdijet',
#                         'BD_DR_Trijet_jetNotdijet',
#                         'GD_Mass_minDR_dijet',
#                         'BD_Mass_minDR_dijet',
#                         'GD_pTrat',
#                         'BD_pTrat',
#                         'BD_DCSV_jetNotdijet',
                           'Aplanarity',
                           'FW_momentum_0',
                           'FW_momentum_1',
                           'FW_momentum_2',
                           'FW_momentum_3',
                           'FW_momentum_4',
                           'FW_momentum_5',
                           'FW_momentum_6',
                           'HT_woBESTjet',
                           'MT_lepMet',
                           'MT_woBESTjet',
                           'M_allJet_W',
                           'M_woBESTjet',
                           'PT_woBESTjet',
                           'PtFifthJet',
                           'Sphericity',
                           'W_PtdM',
                           'aveBBdr',
                           'invM_jet34',
                           'invM_jet35',
                           'invM_jet36',
                           'invM_jet45',
                           'invM_jet46',
                           'invM_jet56',
                           'alphaT',
                           'corr_met_singleLepCalc',
                           'csvJet1',
                           'csvJet2',
                           'csvJet3',
                           'csvJet4',
                           'deltaEta_maxBB',
                           'deltaPhi_METjets',
                           'deltaPhi_j1j2', 
                           'deltaPhi_lepJetInMinMljet',
                           'deltaPhi_lepMET',
                           'deltaPhi_lepbJetInMinMlb',
                           'deltaR_lepBJet_maxpt',
                           'deltaR_lepBJets0',
                           'deltaR_lepBJets1',
                           'deltaR_lepBJets',
                           'deltaR_lepJetInMinMljet',
                           'deltaR_lepJets',
                           'deltaR_lepbJetInMinMlb',
                           'deltaR_lepbJetNotInMinMlb',
                           'deltaR_minBB', 
                           'firstcsvb_bb',
                           'fourthcsvb_bb',
                           'hemiout',
                           'lepDR_minBBdr',
                           'mass_lepBB_minBBdr',
                           'mass_lepBJet0',
                           'mass_lepBJet_mindr',
                           'mass_lepJJ_minJJdr',
                           'mass_lepJets0', 
                           'mass_lepJets1',
                           'mass_lepJets2',
                           'mass_maxBBmass',
                           'mass_maxBBpt',
                           'mass_maxJJJpt',
                           'mass_minBBdr',
                           'mass_minLLdr',
                           'mean_csv',
                           'minBBdr',
                           'minDR_lepBJet',
                           'minMleppBjet',
                           'min_deltaPhi_METjets',
                           'pT_3rdcsvJet',
                           'pT_4thcsvJet',
                           'pTjet5_6',
                           'pt3HT',
                           'pt4HT',
                           'ratio_HTdHT4leadjets',          
                           'thirdcsvb_bb',
                           'secondcsvb_bb',
                           'theJetLeadPt',
                           'MT2bb',
                           'TJetLeadPt',
                           'WJetLeadPt',
			]

isEMlist  = ['E','M']
nttaglist = ['0','1','2p']
nWtaglist = ['0','1','2p']
nbtaglist = ['2','3','4p']
njetslist = ['3','4','5','6','7','8','9','10p']
if not categorize: 	
	nttaglist = ['0p']
	nWtaglist = ['0p']
	nbtaglist = ['1p'] #to match what Sinan has
	njetslist = ['4p'] #4 to match what Sinan had in step 1 15 Feb. 2019 MHH
catList = list(itertools.product(isEMlist,nttaglist,nWtaglist,nbtaglist,njetslist))

outDir = outputDir+pfix
if not os.path.exists(outDir): os.system('mkdir '+outDir)
os.system('cp ../analyze.py doHists.py ../weights.py ../samples.py doCondorTemplates.py doCondorTemplates.sh '+outDir+'/')
os.chdir(outDir)

count=0
for iplot in iPlotList:
	for cat in catList:
		catDir = cat[0]+'_nT'+cat[1]+'_nW'+cat[2]+'_nB'+cat[3]+'_nJ'+cat[4]
		print "iPlot: "+iplot+", cat: "+catDir
		if not os.path.exists(outDir+'/'+catDir): os.system('mkdir '+catDir)
		os.chdir(catDir)
		os.system('cp '+outputDir+'/doCondorTemplates.sh '+outDir+'/'+catDir+'/'+cat[0]+'T'+cat[1]+'W'+cat[2]+'B'+cat[3]+'J'+cat[4]+iplot+'.sh')			
	
		dict={'dir':outputDir,'iPlot':iplot,'region':region,'isCategorized':categorize,
			  'isEM':cat[0],'nttag':cat[1],'nWtag':cat[2],'nbtag':cat[3],'njets':cat[4],
			  'exeDir':outDir+'/'+catDir}
	
		jdf=open('condor.job','w')
		jdf.write(
"""universe = vanilla
Executable = %(exeDir)s/%(isEM)sT%(nttag)sW%(nWtag)sB%(nbtag)sJ%(njets)s%(iPlot)s.sh
Should_Transfer_Files = YES
WhenToTransferOutput = ON_EXIT
request_memory = 3072
Output = condor_%(iPlot)s.out
Error = condor_%(iPlot)s.err
Log = condor_%(iPlot)s.log
Notification = Error
Arguments = %(dir)s %(iPlot)s %(region)s %(isCategorized)s %(isEM)s %(nttag)s %(nWtag)s %(nbtag)s %(njets)s
Queue 1"""%dict)
		jdf.close()

		os.system('condor_submit condor.job')
		os.chdir('..')
		count+=1

print "Total jobs submitted:", count
                  

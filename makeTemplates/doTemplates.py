#!/usr/bin/python

import os,sys,time,math,datetime,pickle,itertools,fnmatch
from ROOT import gROOT,TFile,TH1F
parent = os.path.dirname(os.getcwd())
sys.path.append(parent)
from weights import *
from modSyst import *
from utils import *

gROOT.SetBatch(1)
start_time = time.time()

lumiStr = str(targetlumi/1000).replace('.','p') # 1/fb

region='SR' #PS,SR
isCategorized=True
cutString=''#'lep50_MET30_DR0_1jet50_2jet40'
pfix='templates_'
if not isCategorized: pfix='kinematics_'+region+'_'
pfix+='2016_11_23'
outDir = os.getcwd()+'/'+pfix+'/'+cutString

scaleSignalXsecTo1pb = True # this has to be "True" if you are making templates for limit calculation!!!!!!!!
scaleLumi = False
lumiScaleCoeff = 33590./36000.
doAllSys = True
doQ2sys = True
if not doAllSys: doQ2sys = False
addCRsys = False
systematicList = ['pileup','jec','jer','toppt','muR','muF','muRFcorrd','btag','mistag','trigeff']
normalizeRENORM_PDF = False #normalize the renormalization/pdf uncertainties to nominal templates --> normalizes signal processes only !!!!
		       
bkgGrupList = ['ttbar','wjets','top','ewk','qcd']
bkgProcList = ['TTJets','T','TTV','WJets','ZJets','VV','qcd']
bkgProcs = {}
bkgProcs['WJets']  = ['WJetsMG'] 
bkgProcs['ZJets']  = ['DY']
bkgProcs['VV']     = ['WW','WZ','ZZ']
bkgProcs['TTV']    = ['TTWl','TTWq','TTZl','TTZq']
bkgProcs['TTJets'] = ['TTJetsPH0to700inc','TTJetsPH700to1000inc','TTJetsPH1000toINFinc','TTJetsPH700mtt','TTJetsPH1000mtt']
bkgProcs['T']      = ['Tt','Tbt','Ts','TtW','TbtW']
bkgProcs['qcd'] = ['QCDht300','QCDht500','QCDht700','QCDht1000','QCDht1500','QCDht2000']#'QCDht100','QCDht200',
bkgProcs['top'] = bkgProcs['TTV']+bkgProcs['T']
bkgProcs['ewk'] = bkgProcs['ZJets']+bkgProcs['VV'] 
bkgProcs['ttbar'] = bkgProcs['TTJets']
bkgProcs['wjets'] = bkgProcs['WJets']
dataList = ['DataEPRH','DataMPRH','DataERRBCDEFG','DataMRRBCDEFG']

topptProcs = ['ttbar','TTJets']
bkgProcs['ttbar_q2up'] = ['TTJetsPHQ2U']#,'TtWQ2U','TbtWQ2U']
bkgProcs['ttbar_q2dn'] = ['TTJetsPHQ2D']#,'TtWQ2D','TbtWQ2D']

whichSignal = 'HTB' #HTB, TT, BB, or X53X53
massList = range(180,220+1,20)+range(250,500+1,50)
sigList = [whichSignal+'M'+str(mass) for mass in massList]
if whichSignal=='X53X53': sigList = [whichSignal+'M'+str(mass)+chiral for mass in massList for chiral in ['left','right']]
if whichSignal=='TT': decays = ['BWBW','THTH','TZTZ','TZBW','THBW','TZTH'] #T' decays
if whichSignal=='BB': decays = ['TWTW','BHBH','BZBZ','BZTW','BHTW','BZBH'] #B' decays
if whichSignal=='X53X53': decays = [''] #decays to tWtW 100% of the time
if whichSignal=='HTB': decays = ['']

doBRScan = False
BRs={}
BRs['BW']=[0.0,0.50,0.0,0.0,0.0,0.0,0.0,0.0,0.2,0.2,0.2,0.2,0.2,0.4,0.4,0.4,0.4,0.6,0.6,0.6,0.8,0.8,1.0]
BRs['TH']=[0.5,0.25,0.0,0.2,0.4,0.6,0.8,1.0,0.0,0.2,0.4,0.6,0.8,0.0,0.2,0.4,0.6,0.0,0.2,0.4,0.0,0.2,0.0]
BRs['TZ']=[0.5,0.25,1.0,0.8,0.6,0.4,0.2,0.0,0.8,0.6,0.4,0.2,0.0,0.6,0.4,0.2,0.0,0.4,0.2,0.0,0.2,0.0,0.0]
nBRconf=len(BRs['BW'])
if not doBRScan: nBRconf=1

isEMlist =['E','M']
nttaglist = ['0p']
nWtaglist = ['0p']
nbtaglist = ['2','3','3p','4p']
njetslist = ['4','5','6p']
if not isCategorized: 
	nbtaglist = ['2p']
	njetslist = ['2p']
catList = ['is'+item[0]+'_nT'+item[1]+'_nW'+item[2]+'_nB'+item[3]+'_nJ'+item[4] for item in list(itertools.product(isEMlist,nttaglist,nWtaglist,nbtaglist,njetslist)) if not skip(item[4] ,item[3])]
tagList = ['nT'+item[0]+'_nW'+item[1]+'_nB'+item[2]+'_nJ'+item[3] for item in list(itertools.product(nttaglist,nWtaglist,nbtaglist,njetslist)) if not skip(item[3] ,item[2])]

lumiSys = 0.062 #lumi uncertainty
eltrigSys = 0.03 #electron trigger uncertainty
mutrigSys = 0.011 #muon trigger uncertainty
elIdSys = 0.01 #electron id uncertainty
muIdSys = 0.011 #muon id uncertainty
elIsoSys = 0.01 #electron isolation uncertainty
muIsoSys = 0.03 #muon isolation uncertainty

elcorrdSys = math.sqrt(lumiSys**2+eltrigSys**2+elIdSys**2+elIsoSys**2)
mucorrdSys = math.sqrt(lumiSys**2+mutrigSys**2+muIdSys**2+muIsoSys**2)

for tag in tagList:
	modTag = tag[tag.find('nT'):tag.find('nJ')-3]
	modelingSys['data_'+modTag] = 0.
	modelingSys['qcd_'+modTag] = 0.
	if not addCRsys: #else CR uncertainties are defined in modSyst.py module
		for proc in bkgProcs.keys():
			modelingSys[proc+'_'+modTag] = 0.
	
# if 'CR' in region: postTag = 'isCR_'
# else: postTag = 'isSR_'
###########################################################
#################### CATEGORIZATION #######################
###########################################################
def makeThetaCats(datahists,sighists,bkghists,discriminant):
	yieldTable = {}
	yieldStatErrTable = {}
	for cat in catList:
		histoPrefix=discriminant+'_'+lumiStr+'fb_'+cat
		yieldTable[histoPrefix]={}
		yieldStatErrTable[histoPrefix]={}
		if doAllSys:
			for syst in systematicList:
				for ud in ['Up','Down']:
					yieldTable[histoPrefix+syst+ud]={}
			
		if doQ2sys:
			yieldTable[histoPrefix+'q2Up']={}
			yieldTable[histoPrefix+'q2Down']={}

	for BRind in range(nBRconf):
		BRconfStr=''
		if doBRScan: BRconfStr='_bW'+str(BRs['BW'][BRind]).replace('.','p')+'_tZ'+str(BRs['TZ'][BRind]).replace('.','p')+'_tH'+str(BRs['TH'][BRind]).replace('.','p')
		print "       BR Configuration:"+BRconfStr
		#Initialize dictionaries for histograms
		hists={}
		for cat in catList:
			print "              processing cat: "+cat
			histoPrefix=discriminant+'_'+lumiStr+'fb_'+cat
			i=BRconfStr+cat

			#Group data processes
			hists['data'+i] = datahists[histoPrefix+'_'+dataList[0]].Clone(histoPrefix+'__DATA')
			for dat in dataList:
				if dat!=dataList[0]: hists['data'+i].Add(datahists[histoPrefix+'_'+dat])
			
			#Group processes
			for proc in bkgProcList+bkgGrupList:
				hists[proc+i] = bkghists[histoPrefix+'_'+bkgProcs[proc][0]].Clone(histoPrefix+'__'+proc)
				for bkg in bkgProcs[proc]:
					if bkg!=bkgProcs[proc][0]: hists[proc+i].Add(bkghists[histoPrefix+'_'+bkg])
	
			#get signal
			for signal in sigList:
				hists[signal+i] = sighists[histoPrefix+'_'+signal+decays[0]].Clone(histoPrefix+'__sig')
				if doBRScan: hists[signal+i].Scale(BRs[decays[0][:2]][BRind]*BRs[decays[0][2:]][BRind]/(BR[decays[0][:2]]*BR[decays[0][2:]]))
				for decay in decays:
					if decay!=decays[0]:
						htemp = sighists[histoPrefix+'_'+signal+decay].Clone()
						if doBRScan: htemp.Scale(BRs[decay[:2]][BRind]*BRs[decay[2:]][BRind]/(BR[decay[:2]]*BR[decay[2:]]))
						hists[signal+i].Add(htemp)

			#systematics
			if doAllSys:
				for syst in systematicList:
					for ud in ['Up','Down']:
						for proc in bkgProcList+bkgGrupList:
							if syst=='toppt' and proc not in topptProcs: continue
							hists[proc+i+syst+ud] = bkghists[histoPrefix.replace(discriminant,discriminant+syst+ud)+'_'+bkgProcs[proc][0]].Clone(histoPrefix+'__'+proc+'__'+syst+'__'+ud.replace('Up','plus').replace('Down','minus'))
							for bkg in bkgProcs[proc]:
								if bkg!=bkgProcs[proc][0]: hists[proc+i+syst+ud].Add(bkghists[histoPrefix.replace(discriminant,discriminant+syst+ud)+'_'+bkg])
						if syst=='toppt': continue
						for signal in sigList:
							hists[signal+i+syst+ud] = sighists[histoPrefix.replace(discriminant,discriminant+syst+ud)+'_'+signal+decays[0]].Clone(histoPrefix+'__sig__'+syst+'__'+ud.replace('Up','plus').replace('Down','minus'))
							if doBRScan: hists[signal+i+syst+ud].Scale(BRs[decays[0][:2]][BRind]*BRs[decays[0][2:]][BRind]/(BR[decays[0][:2]]*BR[decays[0][2:]]))
							for decay in decays:
								htemp = sighists[histoPrefix.replace(discriminant,discriminant+syst+ud)+'_'+signal+decay].Clone()
								if doBRScan: htemp.Scale(BRs[decay[:2]][BRind]*BRs[decay[2:]][BRind]/(BR[decay[:2]]*BR[decay[2:]]))
								if decay!=decays[0]: hists[signal+i+syst+ud].Add(htemp)
				for pdfInd in range(100):
					for proc in bkgProcList+bkgGrupList:
						hists[proc+i+'pdf'+str(pdfInd)] = bkghists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+bkgProcs[proc][0]].Clone(histoPrefix+'__'+proc+'__pdf'+str(pdfInd))
						for bkg in bkgProcs[proc]:
							if bkg!=bkgProcs[proc][0]: hists[proc+i+'pdf'+str(pdfInd)].Add(bkghists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+bkg])
					for signal in sigList:
						hists[signal+i+'pdf'+str(pdfInd)] = sighists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+signal+decays[0]].Clone(histoPrefix+'__sig__pdf'+str(pdfInd))
						if doBRScan: hists[signal+i+'pdf'+str(pdfInd)].Scale(BRs[decays[0][:2]][BRind]*BRs[decays[0][2:]][BRind]/(BR[decays[0][:2]]*BR[decays[0][2:]]))
						for decay in decays:
							htemp = sighists[histoPrefix.replace(discriminant,discriminant+'pdf'+str(pdfInd))+'_'+signal+decay].Clone()
							if doBRScan: htemp.Scale(BRs[decay[:2]][BRind]*BRs[decay[2:]][BRind]/(BR[decay[:2]]*BR[decay[2:]]))
							if decay!=decays[0]:hists[signal+i+'pdf'+str(pdfInd)].Add(htemp)
											
			if doQ2sys:
				for proc in bkgProcList+bkgGrupList:
					if proc+'_q2up' not in bkgProcs.keys(): continue
					hists[proc+i+'q2Up'] = bkghists[histoPrefix+'_'+bkgProcs[proc+'_q2up'][0]].Clone(histoPrefix+'__'+proc+'__q2__plus')
					hists[proc+i+'q2Down'] = bkghists[histoPrefix+'_'+bkgProcs[proc+'_q2dn'][0]].Clone(histoPrefix+'__'+proc+'__q2__minus')
					for bkg in bkgProcs[proc+'_q2up']:
						if bkg!=bkgProcs[proc+'_q2up'][0]: hists[proc+i+'q2Up'].Add(bkghists[histoPrefix+'_'+bkg])
					for bkg in bkgProcs[proc+'_q2dn']:
						if bkg!=bkgProcs[proc+'_q2dn'][0]: hists[proc+i+'q2Down'].Add(bkghists[histoPrefix+'_'+bkg])
		
			#+/- 1sigma variations of shape systematics
			if doAllSys:
				for syst in systematicList:
					for ud in ['Up','Down']:
						for proc in bkgGrupList+bkgProcList+sigList:
							if syst=='toppt' and proc not in topptProcs: continue
							yieldTable[histoPrefix+syst+ud][proc] = hists[proc+i+syst+ud].Integral()
			if doQ2sys:
				for proc in bkgProcList+bkgGrupList:
					if proc+'_q2up' not in bkgProcs.keys(): continue
					yieldTable[histoPrefix+'q2Up'][proc] = hists[proc+i+'q2Up'].Integral()
					yieldTable[histoPrefix+'q2Down'][proc] = hists[proc+i+'q2Down'].Integral()

			#prepare yield table
			for proc in bkgGrupList+bkgProcList+sigList+['data']: yieldTable[histoPrefix][proc] = hists[proc+i].Integral()
			yieldTable[histoPrefix]['totBkg'] = sum([hists[proc+i].Integral() for proc in bkgGrupList])
			yieldTable[histoPrefix]['dataOverBkg'] = yieldTable[histoPrefix]['data']/yieldTable[histoPrefix]['totBkg']

			#prepare MC yield error table
			for proc in bkgGrupList+bkgProcList+sigList+['data']: yieldStatErrTable[histoPrefix][proc] = 0.
			yieldStatErrTable[histoPrefix]['totBkg'] = 0.
			yieldStatErrTable[histoPrefix]['dataOverBkg']= 0.

			for ibin in range(1,hists[bkgGrupList[0]+i].GetXaxis().GetNbins()+1):
				for proc in bkgGrupList+bkgProcList+sigList+['data']: yieldStatErrTable[histoPrefix][proc] += hists[proc+i].GetBinError(ibin)**2
				yieldStatErrTable[histoPrefix]['totBkg'] += sum([hists[proc+i].GetBinError(ibin)**2 for proc in bkgGrupList])
			for key in yieldStatErrTable[histoPrefix].keys(): yieldStatErrTable[histoPrefix][key] = math.sqrt(yieldStatErrTable[histoPrefix][key])

		#scale signal cross section to 1pb
		if scaleSignalXsecTo1pb:
			print "       SCALING SIGNAL TEMPLATES TO 1pb ..."
			for signal in sigList:
				for cat in catList:
					i=BRconfStr+cat
					hists[signal+i].Scale(1./xsec[signal])
					if doAllSys:
						for syst in systematicList:
							if syst=='toppt': continue
							hists[signal+i+syst+'Up'].Scale(1./xsec[signal])
							hists[signal+i+syst+'Down'].Scale(1./xsec[signal])
							if normalizeRENORM_PDF and (syst.startswith('mu') or syst=='pdf'):
								hists[signal+i+syst+'Up'].Scale(hists[signal+i].Integral()/hists[signal+i+syst+'Up'].Integral())
								hists[signal+i+syst+'Down'].Scale(hsihistsg[signal+i].Integral()/hists[signal+i+syst+'Down'].Integral())
						for pdfInd in range(100): 
							hists[signal+i+'pdf'+str(pdfInd)].Scale(1./xsec[signal])

		#Theta templates:
		print "       WRITING THETA TEMPLATES: "
		for signal in sigList:
			print "              ... "+signal
			thetaRfileName = outDir+'/templates_'+discriminant+'_'+signal+BRconfStr+'_'+lumiStr+'fb'+'.root'
			thetaRfile = TFile(thetaRfileName,'RECREATE')
			for cat in catList:
				i=BRconfStr+cat
				for proc in bkgGrupList+[signal]:
					if hists[proc+i].Integral() > 0:
						hists[proc+i].Write()
						if doAllSys:
							for syst in systematicList:
								if syst=='toppt' and proc not in topptProcs: continue
								hists[proc+i+syst+'Up'].Write()
								hists[proc+i+syst+'Down'].Write()
							for pdfInd in range(100): hists[proc+i+'pdf'+str(pdfInd)].Write()
						if doQ2sys:
							if proc+'_q2up' not in bkgProcs.keys(): continue
							hists[proc+i+'q2Up'].Write()
							hists[proc+i+'q2Down'].Write()
				hists['data'+i].Write()
			thetaRfile.Close()

		#Combine templates:
		print "       WRITING COMBINE TEMPLATES: "
		combineRfileName = outDir+'/templates_'+discriminant+BRconfStr+'_'+lumiStr+'fb'+'.root'
		combineRfile = TFile(combineRfileName,'RECREATE')
		for cat in catList:
			print "              ... "+cat
			i=BRconfStr+cat
			if '_nB2_' in cat or '_nJ4' in cat: postTag = 'isCR_'
			else: postTag = 'isSR_'
			for signal in sigList:
				mass = [str(mass) for mass in massList if str(mass) in signal][0]
				hists[signal+i].SetName(hists[signal+i].GetName().replace('fb_','fb_'+postTag).replace('__sig','__'+signal.replace('M'+mass,'')+'M'+mass))
				hists[signal+i].Write()
				if doAllSys:
					for syst in systematicList:
						if syst=='toppt': continue
						hists[signal+i+syst+'Up'].SetName(hists[signal+i+syst+'Up'].GetName().replace('fb_','fb_'+postTag).replace('__sig','__'+signal.replace('M'+mass,'')+'M'+mass).replace('__plus','Up'))
						hists[signal+i+syst+'Down'].SetName(hists[signal+i+syst+'Down'].GetName().replace('fb_','fb_'+postTag).replace('__sig','__'+signal.replace('M'+mass,'')+'M'+mass).replace('__minus','Down'))
						hists[signal+i+syst+'Up'].Write()
						hists[signal+i+syst+'Down'].Write()
					for pdfInd in range(100): 
						hists[signal+i+'pdf'+str(pdfInd)].SetName(hists[signal+i+'pdf'+str(pdfInd)].GetName().replace('fb_','fb_'+postTag).replace('__sig','__'+signal.replace('M'+mass,'')+'M'+mass))
						hists[signal+i+'pdf'+str(pdfInd)].Write()
			for proc in bkgGrupList:
				hists[proc+i].SetName(hists[proc+i].GetName().replace('fb_','fb_'+postTag))
				hists[proc+i].Write()
				if doAllSys:
					for syst in systematicList:
						if syst=='toppt' and proc not in topptProcs: continue
						hists[proc+i+syst+'Up'].SetName(hists[proc+i+syst+'Up'].GetName().replace('fb_','fb_'+postTag).replace('__plus','Up'))
						hists[proc+i+syst+'Down'].SetName(hists[proc+i+syst+'Down'].GetName().replace('fb_','fb_'+postTag).replace('__minus','Down'))
						hists[proc+i+syst+'Up'].Write()
						hists[proc+i+syst+'Down'].Write()
					for pdfInd in range(100): 
						hists[proc+i+'pdf'+str(pdfInd)].SetName(hists[proc+i+'pdf'+str(pdfInd)].GetName().replace('fb_','fb_'+postTag))
						hists[proc+i+'pdf'+str(pdfInd)].Write()
				if doQ2sys:
					if proc+'_q2up' not in bkgProcs.keys(): continue
					hists[proc+i+'q2Up'].SetName(hists[proc+i+'q2Up'].GetName().replace('fb_','fb_'+postTag).replace('__plus','Up'))
					hists[proc+i+'q2Down'].SetName(hists[proc+i+'q2Down'].GetName().replace('fb_','fb_'+postTag).replace('__minus','Down'))
					hists[proc+i+'q2Up'].Write()
					hists[proc+i+'q2Down'].Write()
			hists['data'+i].SetName(hists['data'+i].GetName().replace('fb_','fb_'+postTag).replace('DATA','data_obs'))
			hists['data'+i].Write()
		combineRfile.Close()

		print "       WRITING SUMMARY TEMPLATES: "
		for signal in sigList:
			print "              ... "+signal
			yldRfileName = outDir+'/templates_YLD_'+signal+BRconfStr+'_'+lumiStr+'fb.root'
			yldRfile = TFile(yldRfileName,'RECREATE')
			for isEM in isEMlist:	
				for proc in bkgGrupList+['data',signal]:
					yldHists = {}
					yldHists[isEM+proc]=TH1F('YLD_'+lumiStr+'fb_is'+isEM+'_nT0p_nW0p_nB0p_nJ0p__'+proc.replace(signal,'sig').replace('data','DATA'),'',len(tagList),0,len(tagList))
					if doAllSys and proc!='data':
						for syst in systematicList:
							for ud in ['Up','Down']:
								if syst=='toppt' and proc not in topptProcs: continue
								yldHists[isEM+proc+syst+ud]=TH1F('YLD_'+lumiStr+'fb_is'+isEM+'_nT0p_nW0p_nB0p_nJ0p__'+proc.replace(signal,'sig').replace('data','DATA')+'__'+syst+'__'+ud.replace('Up','plus').replace('Down','minus'),'',len(tagList),0,len(tagList))
					if doQ2sys and proc+'_q2up' in bkgProcs.keys(): 
						yldHists[isEM+proc+'q2Up']  =TH1F('YLD_'+lumiStr+'fb_is'+isEM+'_nT0p_nW0p_nB0p_nJ0p__'+proc.replace(signal,'sig').replace('data','DATA')+'__q2__plus','',len(tagList),0,len(tagList))
						yldHists[isEM+proc+'q2Down']=TH1F('YLD_'+lumiStr+'fb_is'+isEM+'_nT0p_nW0p_nB0p_nJ0p__'+proc.replace(signal,'sig').replace('data','DATA')+'__q2__minus','',len(tagList),0,len(tagList))
					ibin = 1
					for cat in catList:
						if 'is'+isEM not in cat: continue
						nttag = cat.split('_')[-4][2:]
						nWtag = cat.split('_')[-3][2:]
						nbtag = cat.split('_')[-2][2:]
						njets = cat.split('_')[-1][2:]
						binStr = ''
						if nttag!='0p':
							if 'p' in nttag: binStr+='#geq'+nttag[:-1]+'t/'
							else: binStr+=nttag+'t/'
						if nWtag!='0p':
							if 'p' in nWtag: binStr+='#geq'+nWtag[:-1]+'W/'
							else: binStr+=nWtag+'W/'
						if nbtag!='0p':
							if 'p' in nbtag: binStr+='#geq'+nbtag[:-1]+'b/'
							else: binStr+=nbtag+'b/'
						if njets!='0p' and len(njetslist)>1:
							if 'p' in njets: binStr+='#geq'+njets[:-1]+'j'
							else: binStr+=njets+'j'
						if binStr.endswith('/'): binStr=binStr[:-1]
						histoPrefix=discriminant+'_'+lumiStr+'fb_'+cat
						yldHists[isEM+proc].SetBinContent(ibin,yieldTable[histoPrefix][proc])
						yldHists[isEM+proc].SetBinError(ibin,yieldStatErrTable[histoPrefix][proc])
						yldHists[isEM+proc].GetXaxis().SetBinLabel(ibin,binStr)
						if doAllSys and proc!='data':
							for syst in systematicList:
								for ud in ['Up','Down']:
									if syst=='toppt' and proc not in topptProcs: continue
									yldHists[isEM+proc+syst+ud].SetBinContent(ibin,yieldTable[histoPrefix+syst+ud][proc])
									yldHists[isEM+proc+syst+ud].GetXaxis().SetBinLabel(ibin,binStr)
						if doQ2sys and proc+'_q2up' in bkgProcs.keys(): 
							yldHists[isEM+proc+'q2Up'].SetBinContent(ibin,yieldTable[histoPrefix+'q2Up'][proc])
							yldHists[isEM+proc+'q2Up'].GetXaxis().SetBinLabel(ibin,binStr)
							yldHists[isEM+proc+'q2Down'].SetBinContent(ibin,yieldTable[histoPrefix+'q2Down'][proc])
							yldHists[isEM+proc+'q2Down'].GetXaxis().SetBinLabel(ibin,binStr)
						ibin+=1
					yldHists[isEM+proc].Write()
					if doAllSys and proc!='data':
						for syst in systematicList:
							for ud in ['Up','Down']:
								if syst=='toppt' and proc not in topptProcs: continue
								yldHists[isEM+proc+syst+ud].Write()
					if doQ2sys and proc+'_q2up' in bkgProcs.keys(): 
						yldHists[isEM+proc+'q2Up'].Write()
						yldHists[isEM+proc+'q2Down'].Write()
			yldRfile.Close()
				
		table = []
		table.append(['CUTS:',cutString])
		table.append(['break'])
		table.append(['break'])
		
		#yields without background grouping
		table.append(['YIELDS']+[proc for proc in bkgProcList+['data']])
		for cat in catList:
			row = [cat]
			histoPrefix=discriminant+'_'+lumiStr+'fb_'+cat
			for proc in bkgProcList+['data']:
				row.append(str(yieldTable[histoPrefix][proc])+' $\pm$ '+str(yieldStatErrTable[histoPrefix][proc]))
			table.append(row)			
		table.append(['break'])
		table.append(['break'])
		
		#yields with top,ewk,qcd grouping
		table.append(['YIELDS']+[proc for proc in bkgGrupList+['data']])
		for cat in catList:
			row = [cat]
			histoPrefix=discriminant+'_'+lumiStr+'fb_'+cat
			for proc in bkgGrupList+['data']:
				row.append(str(yieldTable[histoPrefix][proc])+' $\pm$ '+str(yieldStatErrTable[histoPrefix][proc]))
			table.append(row)
		table.append(['break'])
		table.append(['break'])
		
		#yields for signals
		table.append(['YIELDS']+[proc for proc in sigList])
		for cat in catList:
			row = [cat]
			histoPrefix=discriminant+'_'+lumiStr+'fb_'+cat
			for proc in sigList:
				row.append(str(yieldTable[histoPrefix][proc])+' $\pm$ '+str(yieldStatErrTable[histoPrefix][proc]))
			table.append(row)

		#yields for AN tables (yields in e/m channels)
		for isEM in isEMlist:
			if isEM=='E': corrdSys = elcorrdSys
			if isEM=='M': corrdSys = mucorrdSys
			for nttag in nttaglist:
				table.append(['break'])
				table.append(['','is'+isEM+'_nT'+nttag+'_yields'])
				table.append(['break'])
				table.append(['YIELDS']+[cat for cat in catList if 'is'+isEM in cat and 'nT'+nttag in cat]+['\\\\'])
				for proc in bkgGrupList+['totBkg','data','dataOverBkg']+sigList:
					row = [proc]
					for cat in catList:
						if not ('is'+isEM in cat and 'nT'+nttag in cat): continue
						modTag = cat[cat.find('nT'):cat.find('nJ')-3]
						histoPrefix=discriminant+'_'+lumiStr+'fb_'+cat
						yieldtemp = 0.
						yielderrtemp = 0.
						if proc=='totBkg' or proc=='dataOverBkg':
							for bkg in bkgGrupList:
								try:
									yieldtemp += yieldTable[histoPrefix][bkg]
									yielderrtemp += yieldStatErrTable[histoPrefix][bkg]**2
									yielderrtemp += (modelingSys[bkg+'_'+modTag]*yieldTable[histoPrefix][bkg])**2
								except:
									print "Missing",bkg,"for channel:",cat
									pass
							yielderrtemp += (corrdSys*yieldtemp)**2
							if proc=='dataOverBkg':
								dataTemp = yieldTable[histoPrefix]['data']+1e-20
								dataTempErr = yieldStatErrTable[histoPrefix]['data']**2
								yielderrtemp = ((dataTemp/yieldtemp)**2)*(dataTempErr/dataTemp**2+yielderrtemp/yieldtemp**2)
								yieldtemp = dataTemp/yieldtemp
						else:
							try:
								yieldtemp += yieldTable[histoPrefix][proc]
								yielderrtemp += yieldStatErrTable[histoPrefix][proc]**2
							except:
								print "Missing",proc,"for channel:",cat
								pass
							if proc not in sigList: yielderrtemp += (modelingSys[proc+'_'+modTag]*yieldtemp)**2
							yielderrtemp += (corrdSys*yieldtemp)**2
						yielderrtemp = math.sqrt(yielderrtemp)
						if proc=='data': row.append(' & '+str(int(yieldTable[histoPrefix][proc])))
						else: row.append(' & '+str(round_sig(yieldtemp,5))+' $\pm$ '+str(round_sig(yielderrtemp,2)))
					row.append('\\\\')
					table.append(row)
		
		#yields for PAS tables (yields in e/m channels combined)
		for nttag in nttaglist:
			table.append(['break'])
			table.append(['','isL_nT'+nttag+'_yields'])
			table.append(['break'])
			table.append(['YIELDS']+[cat.replace('isE','isL') for cat in catList if 'isE' in cat and 'nT'+nttag in cat]+['\\\\'])
			for proc in bkgGrupList+['totBkg','data','dataOverBkg']+sigList:
				row = [proc]
				for cat in catList:
					if not ('isE' in cat and 'nT'+nttag in cat): continue
					modTag = cat[cat.find('nT'):cat.find('nJ')-3]
					histoPrefixE = discriminant+'_'+lumiStr+'fb_'+cat
					histoPrefixM = histoPrefixE.replace('isE','isM')
					yieldtemp = 0.
					yieldtempE = 0.
					yieldtempM = 0.
					yielderrtemp = 0. 
					if proc=='totBkg' or proc=='dataOverBkg':
						for bkg in bkgGrupList:
							try:
								yieldtempE += yieldTable[histoPrefixE][bkg]
								yieldtempM += yieldTable[histoPrefixM][bkg]
								yieldtemp  += yieldTable[histoPrefixE][bkg]+yieldTable[histoPrefixM][bkg]
								yielderrtemp += yieldStatErrTable[histoPrefixE][bkg]**2+yieldStatErrTable[histoPrefixM][bkg]**2
								yielderrtemp += (modelingSys[bkg+'_'+modTag]*(yieldTable[histoPrefixE][bkg]+yieldTable[histoPrefixM][bkg]))**2 #(modelingSys*(Nelectron+Nmuon))**2 --> correlated across e/m
							except:
								print "Missing",bkg,"for channel:",cat
								pass
						yielderrtemp += (elcorrdSys*yieldtempE)**2+(mucorrdSys*yieldtempM)**2
						if proc=='dataOverBkg':
							dataTemp = yieldTable[histoPrefixE]['data']+yieldTable[histoPrefixM]['data']+1e-20
							dataTempErr = yieldStatErrTable[histoPrefixE]['data']**2+yieldStatErrTable[histoPrefixM]['data']**2
							yielderrtemp = ((dataTemp/yieldtemp)**2)*(dataTempErr/dataTemp**2+yielderrtemp/yieldtemp**2)
							yieldtemp = dataTemp/yieldtemp
					else:
						try:
							yieldtempE += yieldTable[histoPrefixE][proc]
							yieldtempM += yieldTable[histoPrefixM][proc]
							yieldtemp  += yieldTable[histoPrefixE][proc]+yieldTable[histoPrefixM][proc]
							yielderrtemp += yieldStatErrTable[histoPrefixE][proc]**2+yieldStatErrTable[histoPrefixM][proc]**2
						except:
							print "Missing",proc,"for channel:",cat
							pass
						if proc not in sigList: yielderrtemp += (modelingSys[proc+'_'+modTag]*yieldtemp)**2 #(modelingSys*(Nelectron+Nmuon))**2 --> correlated across e/m
						yielderrtemp += (elcorrdSys*yieldtempE)**2+(mucorrdSys*yieldtempM)**2
					yielderrtemp = math.sqrt(yielderrtemp)
					if proc=='data': row.append(' & '+str(int(yieldTable[histoPrefixE][proc]+yieldTable[histoPrefixM][proc])))
					else: row.append(' & '+str(round_sig(yieldtemp,5))+' $\pm$ '+str(round_sig(yielderrtemp,2)))
				row.append('\\\\')
				table.append(row)

		#systematics
		if doAllSys:
			table.append(['break'])
			table.append(['','Systematics'])
			table.append(['break'])
			for proc in bkgGrupList+sigList:
				table.append([proc]+[cat for cat in catList]+['\\\\'])
				for syst in sorted(systematicList+['q2']):
					for ud in ['Up','Down']:
						row = [syst+ud]
						for cat in catList:
							histoPrefix = discriminant+'_'+lumiStr+'fb_'+cat
							nomHist = histoPrefix
							shpHist = histoPrefix+syst+ud
							try: row.append(' & '+str(round(yieldTable[shpHist][proc]/(yieldTable[nomHist][proc]+1e-20),2)))
							except:
								if not ((syst=='toppt' and proc not in topptProcs) or (proc+'_q2up' not in bkgProcs.keys())):
									print "Missing",proc,"for channel:",cat,"and systematic:",syst
								pass
						row.append('\\\\')
						table.append(row)
				table.append(['break'])
			
		if not addCRsys: out=open(outDir+'/yields_noCRunc_'+discriminant+BRconfStr+'_'+lumiStr+'fb'+'.txt','w')
		else: out=open(outDir+'/yields_'+discriminant+BRconfStr+'_'+lumiStr+'fb'+'.txt','w')
		printTable(table,out)

def findfiles(path, filtre):
    for root, dirs, files in os.walk(path):
        for f in fnmatch.filter(files, filtre):
            yield os.path.join(root, f)

iPlotList = []
for file in findfiles(outDir+'/'+catList[0][2:]+'/', '*.p'):
    if 'bkghists' not in file: continue
    if not os.path.exists(file.replace('bkghists','datahists')): continue
    if not os.path.exists(file.replace('bkghists','sighists')): continue
    iPlotList.append(file.split('/')[-1].replace('bkghists_','')[:-2])

print "WORKING DIR:",outDir
for iPlot in iPlotList:
	datahists = {}
	bkghists  = {}
	sighists  = {}
	#if iPlot!='HT': continue
	print "LOADING DISTRIBUTION: "+iPlot
	for cat in catList:
		print "         ",cat[2:]
		datahists.update(pickle.load(open(outDir+'/'+cat[2:]+'/datahists_'+iPlot+'.p','rb')))
		bkghists.update(pickle.load(open(outDir+'/'+cat[2:]+'/bkghists_'+iPlot+'.p','rb')))
		sighists.update(pickle.load(open(outDir+'/'+cat[2:]+'/sighists_'+iPlot+'.p','rb')))
	if scaleLumi:
		for key in bkghists.keys(): bkghists[key].Scale(lumiScaleCoeff)
		for key in sighists.keys(): sighists[key].Scale(lumiScaleCoeff)

 	#Negative Bin Correction
 	for bkg in bkghists.keys(): negBinCorrection(bkghists[bkg])
 	for sig in sighists.keys(): negBinCorrection(sighists[sig])

 	#OverFlow Correction
 	for data in datahists.keys(): overflow(datahists[data])
 	for bkg in bkghists.keys():   overflow(bkghists[bkg])
 	for sig in sighists.keys():   overflow(sighists[sig])

	print "       MAKING CATEGORIES FOR TOTAL SIGNALS ..."
	makeThetaCats(datahists,sighists,bkghists,iPlot)

print("--- %s minutes ---" % (round((time.time() - start_time)/60,2)))



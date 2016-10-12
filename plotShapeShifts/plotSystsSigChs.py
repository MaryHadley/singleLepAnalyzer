import ROOT as R
import os,sys,math
from array import array

from tdrStyle import *
setTDRStyle()
R.gROOT.SetBatch(1)
outDir = os.getcwd()+'/'

lumi = 2.3
discriminant = 'minMlb'
rfilePostFix = '_rebinned_stat0p15'
tempVersion = 'templates_minMlb_noJSF_tau21Fix1_2016_10_8'
cutString = '/lep80_MET100_NJets4_DR1_1jet200_2jet90'
templateFile = '/home/ssagir/CMSSW_7_3_0/src/singleLepAnalyzer/x53x53_2015/makeTemplates/'+tempVersion+cutString+'/templates_'+discriminant+'_X53X53M900left_2p318fb'+rfilePostFix+'.root'
if not os.path.exists(outDir+tempVersion): os.system('mkdir '+outDir+tempVersion)
if not os.path.exists(outDir+tempVersion+'/signalIndChannels'): os.system('mkdir '+outDir+tempVersion+'/signalIndChannels')

bkgList = ['top','ewk','qcd']
channels = ['isE','isM']
ttags = ['nT0','nT1p']
wtags = ['nW0','nW1p']
btags = ['nB1','nB2p']
systematics = ['pileup','topsf','jmr','jms','tau21','btag','mistag','jer','jec','muRFcorrdNew','pdfNew']

signameList = [
# 		   'X53X53M700left',
		   'X53X53M800left',
# 		   'X53X53M900left',
# 		   'X53X53M1000left',
# 		   'X53X53M1100left',
# 		   'X53X53M1200left',
# 		   'X53X53M1300left',
# 		   'X53X53M1400left',
# 		   'X53X53M1500left',
# 		   'X53X53M1600left',
# 		   'X53X53M700right',
# 		   'X53X53M800right',
# 		   'X53X53M900right',
# 		   'X53X53M1000right',
# 		   'X53X53M1100right',
# 		   'X53X53M1200right',
# 		   'X53X53M1300right',
# 		   'X53X53M1400right',
# 		   'X53X53M1500right',
# 		   'X53X53M1600right',
		       ]

def normByBinWidth(result):
	result.SetBinContent(0,0)
	result.SetBinContent(result.GetNbinsX()+1,0)
	result.SetBinError(0,0)
	result.SetBinError(result.GetNbinsX()+1,0)
	
	for bin in range(1,result.GetNbinsX()+1):
		width=result.GetBinWidth(bin)
		content=result.GetBinContent(bin)
		error=result.GetBinError(bin)
		
		result.SetBinContent(bin, content/width)
		result.SetBinError(bin, error/width)

for signal in signameList:
	RFile = R.TFile(templateFile.replace('TTM900',signal))
	for syst in systematics:
		for ch in channels:
			for ttag in ttags:
				for wtag in wtags:
					for btag in btags:
						Prefix = discriminant+'_2p318fb_'+channels[0]+'_'+ttags[0]+'_'+wtags[0]+'_'+btags[0]+'__sig'
						print Prefix.replace(channels[0],ch).replace(ttags[0],ttag).replace(wtags[0],wtag).replace(btags[0],btag)
						hNm = RFile.Get(Prefix.replace(channels[0],ch).replace(ttags[0],ttag).replace(wtags[0],wtag).replace(btags[0],btag)).Clone()
						hUp = RFile.Get(Prefix.replace(channels[0],ch).replace(ttags[0],ttag).replace(wtags[0],wtag).replace(btags[0],btag)+'__'+syst+'__plus').Clone()
						hDn = RFile.Get(Prefix.replace(channels[0],ch).replace(ttags[0],ttag).replace(wtags[0],wtag).replace(btags[0],btag)+'__'+syst+'__minus').Clone()
						try: 
							print Prefix.replace(channels[0],ch).replace(ttags[0],ttag).replace(wtags[0],wtag).replace(btags[0],btag)
							htemp = RFile.Get(Prefix.replace(channels[0],ch).replace(ttags[0],ttag).replace(wtags[0],wtag).replace(btags[0],btag)).Clone()
							hNm.Add(htemp)
						except: pass
						try:
							if (syst=='q2' or syst=='toppt'):
								htempUp = RFile.Get(Prefix.replace(channels[0],ch).replace(ttags[0],ttag).replace(wtags[0],wtag).replace(btags[0],btag)).Clone()
								hUp.Add(htempUp)
							else:
								htempUp = RFile.Get(Prefix.replace(channels[0],ch).replace(ttags[0],ttag).replace(wtags[0],wtag).replace(btags[0],btag)+'__'+syst+'__plus').Clone()
								hUp.Add(htempUp)
						except:pass
						try: 
							if (syst=='q2' or syst=='toppt'):
								htempDown = RFile.Get(Prefix.replace(channels[0],ch).replace(ttags[0],ttag).replace(wtags[0],wtag).replace(btags[0],btag)).Clone()
								hDn.Add(htempDown)
							else:
								htempDown = RFile.Get(Prefix.replace(channels[0],ch).replace(ttags[0],ttag).replace(wtags[0],wtag).replace(btags[0],btag)+'__'+syst+'__minus').Clone()
								hDn.Add(htempDown)
						except:pass
						normByBinWidth(hNm)
						normByBinWidth(hUp)
						normByBinWidth(hDn)
						hNm.Draw()
						hUp.Draw()
						hDn.Draw()

						canv = R.TCanvas(Prefix+'__'+syst,Prefix+'__'+syst,1000,700)
						yDiv = 0.35
						uPad=R.TPad('uPad','',0,yDiv,1,1)
						uPad.SetTopMargin(0.07)
						uPad.SetBottomMargin(0)
						uPad.SetRightMargin(.05)
						uPad.SetLeftMargin(.18)
						#uPad.SetLogy()
						uPad.Draw()

						lPad=R.TPad("lPad","",0,0,1,yDiv) #for sigma runner
						lPad.SetTopMargin(0)
						lPad.SetBottomMargin(.4)
						lPad.SetRightMargin(.05)
						lPad.SetLeftMargin(.18)
						lPad.SetGridy()
						lPad.Draw()

						uPad.cd()

						R.gStyle.SetOptTitle(0)

						#canv.SetLogy()
						hNm.SetFillColor(R.kWhite)
						hUp.SetFillColor(R.kWhite)
						hDn.SetFillColor(R.kWhite)
						hNm.SetMarkerColor(R.kBlack)
						hUp.SetMarkerColor(R.kRed)
						hDn.SetMarkerColor(R.kBlue)
						hNm.SetLineColor(R.kBlack)
						hUp.SetLineColor(R.kRed)
						hDn.SetLineColor(R.kBlue)
						hNm.SetLineWidth(2)
						hNm.SetLineStyle(1)
						hUp.SetLineWidth(2)
						hUp.SetLineStyle(1)
						hDn.SetLineWidth(2)
						hDn.SetLineStyle(1)
						hNm.SetMarkerSize(.05)
						hUp.SetMarkerSize(.05)
						hDn.SetMarkerSize(.05)

						hUp.GetYaxis().SetTitle('Events / 1 GeV')
						hUp.GetYaxis().SetLabelSize(0.10)
						hUp.GetYaxis().SetTitleSize(0.1)
						hUp.GetYaxis().SetTitleOffset(.8)
		
						#hUp.SetMaximum(1.1*max(hUp.GetMaximum(),hNm.GetMaximum(),hDn.GetMaximum()))
						hUp.GetYaxis().SetRangeUser(0.0001,1.1*max(hUp.GetMaximum(),hNm.GetMaximum(),hDn.GetMaximum()))

						hUp.Draw()
						hNm.Draw('same')
						hDn.Draw('same')
						#uPad.RedrawAxis()

						lPad.cd()
						R.gStyle.SetOptTitle(0)
						pullUp = hUp.Clone()
						for iBin in range(0,pullUp.GetXaxis().GetNbins()+2):
							pullUp.SetBinContent(iBin,pullUp.GetBinContent(iBin)-hNm.GetBinContent(iBin))
							pullUp.SetBinError(iBin,math.sqrt(pullUp.GetBinError(iBin)**2+hNm.GetBinError(iBin)**2))
						pullUp.Divide(hNm)
						pullUp.SetTitle('')
						pullUp.SetFillColor(2)
						pullUp.SetLineColor(2)

						#pullUp.GetXaxis().SetTitle(histName)
						pullUp.GetXaxis().SetLabelSize(.15)
						pullUp.GetXaxis().SetTitleSize(0.18)
						pullUp.GetXaxis().SetTitleOffset(0.95)

						pullUp.GetYaxis().SetTitle('#frac{Up/Down-Nom}{Nom}')#'Python-C++'
						pullUp.GetYaxis().CenterTitle(1)
						pullUp.GetYaxis().SetLabelSize(0.125)
						pullUp.GetYaxis().SetTitleSize(0.1)
						pullUp.GetYaxis().SetTitleOffset(.55)
						pullUp.GetYaxis().SetNdivisions(506)
						#pullUp.SetMinimum(pullDown.GetMinimum())
						#pullUp.SetMaximum(pullUp.GetMaximum())

						pullDown = hDn.Clone()
						for iBin in range(0,pullDown.GetXaxis().GetNbins()+2):
							pullDown.SetBinContent(iBin,pullDown.GetBinContent(iBin)-hNm.GetBinContent(iBin))
							pullDown.SetBinError(iBin,math.sqrt(pullDown.GetBinError(iBin)**2+hNm.GetBinError(iBin)**2))
						pullDown.Divide(hNm)
						pullDown.SetTitle('')
						pullDown.SetFillColor(4)
						pullDown.SetLineColor(4)

						#pullDown.GetXaxis().SetTitle(histName)
						pullDown.GetXaxis().SetLabelSize(.15)
						pullDown.GetXaxis().SetTitleSize(0.18)
						pullDown.GetXaxis().SetTitleOffset(0.95)

						pullDown.GetYaxis().SetTitle('#frac{Up/Down-Nom}{Nom}')#'Python-C++'
						pullDown.GetYaxis().CenterTitle(1)
						pullDown.GetYaxis().SetLabelSize(0.125)
						pullDown.GetYaxis().SetTitleSize(0.1)
						pullDown.GetYaxis().SetTitleOffset(.55)
						pullDown.GetYaxis().SetNdivisions(506)
						pullUp.SetMinimum(-1.4)#min(pullDown.GetMinimum(),pullUp.GetMinimum()))
						pullUp.SetMaximum(1.4)#max(pullDown.GetMaximum(),pullUp.GetMaximum()))
						#pullDown.SetMinimum(pullDown.GetMinimum())
						#pullDown.SetMaximum(pullDown.GetMaximum())
						pullUp.Draw()
						pullDown.Draw('same')
						lPad.RedrawAxis()

						uPad.cd()

						legend = R.TLegend(0.7,0.65,0.9,0.90)
						legend.SetShadowColor(0);
						legend.SetFillColor(0);
						legend.SetLineColor(0);
						legend.AddEntry(hNm,signal,'l')
						legend.AddEntry(hUp,syst.replace('topsf','t tag').replace('muRFcorrdNew','muRF').replace('muRFdecorrdNew','muRF').replace('muRFcorrd','muRF').replace('muRFenv','muRF').replace('pdfNew','PDF').replace('toppt','Top Pt').replace('jsf','JSF').replace('jec','JEC').replace('q2','Q^{2}').replace('pileup','Pileup').replace('jer','JER').replace('btag','b tag').replace('pdf','PDF').replace('jmr','JMR').replace('jms','JMS').replace('tau21','#tau_{2}/#tau_{1}')+' Up','l')
						legend.AddEntry(hDn,syst.replace('topsf','t tag').replace('muRFcorrdNew','muRF').replace('muRFdecorrdNew','muRF').replace('muRFcorrd','muRF').replace('muRFenv','muRF').replace('pdfNew','PDF').replace('toppt','Top Pt').replace('jsf','JSF').replace('jec','JEC').replace('q2','Q^{2}').replace('pileup','Pileup').replace('jer','JER').replace('btag','b tag').replace('pdf','PDF').replace('jmr','JMR').replace('jms','JMS').replace('tau21','#tau_{2}/#tau_{1}')+' Down','l')

						legend.Draw('same')
	
						prelimTex=R.TLatex()
						prelimTex.SetNDC()
						prelimTex.SetTextAlign(31) # align right
						prelimTex.SetTextFont(42)
						prelimTex.SetTextSize(0.05)
						prelimTex.SetLineWidth(2)
						#lumi=round(lumi,2)
						prelimTex.DrawLatex(0.90,0.943,str(lumi)+" fb^{-1} (13 TeV)")
						#prelimTex.DrawLatex(0.88, 0.95, "CMS Preliminary, "+str(lumi)+" fb^{-1} at #sqrt{s} = 8 TeV");

						prelimTex2=R.TLatex()
						prelimTex2.SetNDC()
						prelimTex2.SetTextFont(61)
						prelimTex2.SetLineWidth(2)
						prelimTex2.SetTextSize(0.07)
						prelimTex2.DrawLatex(0.18,0.9364,"CMS")

						prelimTex3=R.TLatex()
						prelimTex3.SetNDC()
						prelimTex3.SetTextAlign(13)
						prelimTex3.SetTextFont(52)
						prelimTex3.SetTextSize(0.040)
						prelimTex3.SetLineWidth(2)
						prelimTex3.DrawLatex(0.25175,0.9664,"Preliminary")
						#if blind: prelimTex3.DrawLatex(0.29175,0.9664,"Preliminary")

						Tex1=R.TLatex()
						Tex1.SetNDC()
						Tex1.SetTextSize(0.05)
						Tex1.SetTextAlign(31) # align right
						#if i == 0: textx = 0.89
						#else: textx = 0.85
						textx = 0.5
						#Tex1.DrawLatex(textx, 0.86, 'test')
	
						Tex2 = R.TLatex()
						Tex2.SetNDC()
						Tex2.SetTextSize(0.06)
						Tex2.SetTextAlign(21)
						if ch=='isE': channelTxt = 'e+jets'
						if ch=='isM': channelTxt = '#mu+jets'
						tagTxt = ''
						if 'p' in ttag: tagTxt+='#geq'+ttag[2:-1]+' t, '
						else: tagTxt+=ttag[2:]+' t, '
						if 'p' in wtag: tagTxt+='#geq'+wtag[2:-1]+' W, '
						else: tagTxt+=wtag[2:]+' W, '
						if 'p' in btag: tagTxt+='#geq'+btag[2:-1]+' b'
						else: tagTxt+=btag[2:]+' b'
						Tex2.DrawLatex(textx, 0.85, channelTxt)
						Tex2.DrawLatex(textx, 0.77, tagTxt)
					
						canv.SaveAs(tempVersion+'/signalIndChannels/'+syst+'_'+signal+'_'+ch+'_'+ttag+'_'+wtag+'_'+btag+'.pdf')
						canv.SaveAs(tempVersion+'/signalIndChannels/'+syst+'_'+signal+'_'+ch+'_'+ttag+'_'+wtag+'_'+btag+'.png')
						canv.SaveAs(tempVersion+'/signalIndChannels/'+syst+'_'+signal+'_'+ch+'_'+ttag+'_'+wtag+'_'+btag+'.eps')
	RFile.Close()


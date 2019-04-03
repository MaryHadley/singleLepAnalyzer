#!/usr/bin/python

samples = {
'DataERRBCDEF':'SingleElectron_31Mar18',#MHH updated 2 April 2019 
'DataMRRBCDEF':'SingleMuon_31Mar18', #MHH updated 2 April 2019

'4TM690':'TTTT_TuneCP5_PSweights_13TeV-amcatnlo-pythia8', #MHH updated 2 April 2019

#'DY':'DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8',
'DYMG':'DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8', #MHH updated 2 April 2019
# 'DYMG100':'DYJetsToLL_M-50_HT-100to200_TuneCP5_13TeV-madgraph-pythia8',
# 'DYMG200':'DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraph-pythia8',
# 'DYMG400':'DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraph-pythia8',
# 'DYMG600':'DYJetsToLL_M-50_HT-600to800_TuneCP5_13TeV-madgraph-pythia8',
# 'DYMG800':'DYJetsToLL_M-50_HT-800to1200_TuneCP5_13TeV-madgraph-pythia8',
# 'DYMG1200':'DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraph-pythia8',
# 'DYMG2500':'DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraph-pythia8',

#'WJetsMG':'WJetsToLNu_TuneCP5_13TeV-madgraph-pythia8',
#'WJetsMG100':'WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8',
'WJetsMG200':'WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8',
'WJetsMG400':'WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8',
'WJetsMG600':'WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8',
'WJetsMG800':'WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8',
'WJetsMG1200':'WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8',
'WJetsMG2500':'WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8',
#'WJetsPt100':'WJetsToLNu_Pt-100To250_TuneCP5_13TeV-amcatnloFXFX-pythia8',
#'WJetsPt250':'WJetsToLNu_Pt-250To400_TuneCP5_13TeV-amcatnloFXFX-pythia8',
#'WJetsPt400':'WJetsToLNu_Pt-400To600_TuneCP5_13TeV-amcatnloFXFX-pythia8',
#'WJetsPt600':'WJetsToLNu_Pt-600ToInf_TuneCP5_13TeV-amcatnloFXFX-pythia8',

'WW':'WW_TuneCP5_13TeV-pythia8',
'WZ':'WZ_TuneCP5_13TeV-pythia8',
'ZZ':'ZZ_TuneCP5_13TeV-pythia8',

#'TTJets':'TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8',
#'WJets':'WJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-pythia8',

#'TTJetsMG':'TTJets_TuneCP5_13TeV-madgraphMLM-pythia8',
## new ttbar for 2017
'TTJetsHad0':'TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8_Mtt0to700',
'TTJetsHad700':'TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8_Mtt700to1000',
'TTJetsHad1000':'TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8_Mtt1000toInf',
'TTJetsSemiLep0':'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_Mtt0to700',
'TTJetsSemiLep700':'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_Mtt700to1000',
'TTJetsSemiLep1000':'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_Mtt1000toInf',
'TTJets2L2nu0':'TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8_Mtt0to700',
'TTJets2L2nu700':'TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8_Mtt700to1000',
'TTJets2L2nu1000':'TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8_Mtt1000toInf',
'TTJetsPH700mtt':'TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8',
'TTJetsPH1000mtt':'TT_Mtt-1000toInf_TuneCP5_PSweights_13TeV-powheg-pythia8',

'Ts':'ST_s-channel_top_leptonDecays_13TeV-PSweights_powheg-pythia8',
'Tbs':'ST_s-channel_antitop_leptonDecays_13TeV-PSweights_powheg-pythia8',#MHH add
'Tbt':'ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8',
'Tt':'ST_t-channel_top_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8',
'TbtW':'ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8',
'TtW':'ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8',

#'TTWl':'TTWJetsToLNu_TuneCP5_PSweights_13TeV-amcatnloFXFX-madspin-pythia8',
'TTW':'ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8',
#'TTZl':'TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8', ## need to fix this, wanted M 10-inf like below
#'TTZl':'TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8',
'TTZ':'ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8',
'TTH' :'ttH_M125_TuneCP5_13TeV-powheg-pythia8',

#'QCDht100':'QCD_HT100to200_TuneCP5_13TeV-madgraph-pythia8',
'QCDht200':'QCD_HT200to300_TuneCP5_13TeV-madgraph-pythia8',
'QCDht300':'QCD_HT300to500_TuneCP5_13TeV-madgraph-pythia8',
'QCDht500':'QCD_HT500to700_TuneCP5_13TeV-madgraph-pythia8',
'QCDht700':'QCD_HT700to1000_TuneCP5_13TeV-madgraph-pythia8',
'QCDht1000':'QCD_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8',
'QCDht1500':'QCD_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8',
'QCDht2000':'QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8',
}




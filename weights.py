#!/usr/bin/python

targetlumi = 35867. # 1/pb

genHTweight={}
genHTweight['WJetsMG100'] = 0.998056#https://github.com/jmhogan/GenHTweight/blob/master/WJetsToLNuSFs.txt
genHTweight['WJetsMG200'] = 0.978569
genHTweight['WJetsMG400'] = 0.928054
genHTweight['WJetsMG600'] = 0.856705
genHTweight['WJetsMG800'] = 0.757463
genHTweight['WJetsMG1200']= 0.608292
genHTweight['WJetsMG2500']= 0.454246

genHTweight['DYMG100'] = 1.007516#https://github.com/jmhogan/GenHTweight/blob/master/DYJetsToLLSFs.txt
genHTweight['DYMG200'] = 0.992853
genHTweight['DYMG400'] = 0.974071
genHTweight['DYMG600'] = 0.948367
genHTweight['DYMG800'] = 0.883340
genHTweight['DYMG1200']= 0.749894
genHTweight['DYMG2500']= 0.617254

BR={}
BR['BW'] = 0.5
BR['TZ'] = 0.25
BR['TH'] = 0.25
BR['TTBWBW'] = BR['BW']*BR['BW']
BR['TTTHBW'] = 2*BR['TH']*BR['BW']
BR['TTTZBW'] = 2*BR['TZ']*BR['BW']
BR['TTTZTZ'] = BR['TZ']*BR['TZ']
BR['TTTZTH'] = 2*BR['TZ']*BR['TH']
BR['TTTHTH'] = BR['TH']*BR['TH']

BR['TW'] = 0.5
BR['BZ'] = 0.25
BR['BH'] = 0.25
BR['BBTWTW'] = BR['TW']*BR['TW']
BR['BBBHTW'] = 2*BR['BH']*BR['TW']
BR['BBBZTW'] = 2*BR['BZ']*BR['TW']
BR['BBBZBZ'] = BR['BZ']*BR['BZ']
BR['BBBZBH'] = 2*BR['BZ']*BR['BH']
BR['BBBHBH'] = BR['BH']*BR['BH']

# Number of processed MC events (before selections)
nRun={}
nRun['TTJets'] = 14188545. #need negative counts
nRun['TTJetsPH'] = 77229341.+78006311. #original+backup
nRun['TTJetsPHorig'] = 77229341.-302860. #original-#event estimate from 4 missing files!
nRun['TTJetsPH0to700inc'] = nRun['TTJetsPH']
nRun['TTJetsPH700to1000inc'] = nRun['TTJetsPH']*0.0921 + 38578334.
nRun['TTJetsPH1000toINFinc'] = nRun['TTJetsPH']*0.02474 + 24561633.
nRun['TTJetsPH700mtt'] = nRun['TTJetsPH700to1000inc']
nRun['TTJetsPH1000mtt'] = nRun['TTJetsPH1000toINFinc']
nRun['Ts'] = 622990. #from 1000000
nRun['Tt'] = 67240808.
nRun['Tbt']= 38811017.
nRun['TtW'] = 6952830.
nRun['TbtW'] = 6933094.
nRun['WJets'] = 6776900. # from 9908534.
nRun['WJetsMG'] = 86731806. 
nRun['WJetsHT100'] = 79356685.
nRun['WJetsHT200'] = 39680891.
nRun['WJetsHT400'] = 7759701.
nRun['WJetsHT600'] = 18687480.
nRun['WJetsHT800'] = 7745467.
nRun['WJetsHT1200']= 6872441.
nRun['WJetsHT2500']= 2637821.
#Do NGen*[1-2X], where X is the neg event fraction calculated from the jobs completed! 
#A = P - N = F - 2*N   A/F = 1 - 2*(N/F)  N/F = (1 - A/F)/2
nRun['WJetsPt100'] = 120124110.*(1.-2.*0.32) #Full =120124110, neg frac 0.32
nRun['WJetsPt250'] = 12022587.*(1.-2.*0.31555) #Full = 12022587, neg frac 0.31555 
nRun['WJetsPt400'] = 1939947.*(1.-2.*0.30952) #Full = 1939947, neg frac 0.30952
nRun['WJetsPt600'] = 1974619.*(1.-2.*0.29876) #Full = 1974619, neg frac 0.29876
nRun['DY'] = 19223750. # from 28696958
nRun['DYMG'] = 96658943.
nRun['DYMG100'] = 10607207.
nRun['DYMG200'] = 9653731.
nRun['DYMG400'] = 10008776.
nRun['DYMG600'] = 8292957.
nRun['DYMG800'] = 2668730.
nRun['DYMG1200']= 596079.
nRun['DYMG2500']= 399492.
nRun['WW'] = 7981136. 
nRun['WZ'] = 3995828.
nRun['ZZ'] = 1988098.
nRun['QCDht100'] = 80684349.
nRun['QCDht200'] = 57580393.
nRun['QCDht300'] = 54537903.
nRun['QCDht500'] = 62271343.
nRun['QCDht700'] = 45412780.
nRun['QCDht1000'] = 15127293.
nRun['QCDht1500'] = 11826702.
nRun['QCDht2000'] = 6039005.
nRun['TTWl'] = 130275. #from 252673
nRun['TTWq'] = 430310. #from 833298
nRun['TTZl'] = 185232. #from 398600
nRun['TTZq'] = 351164. #from 749400
nRun['HTBM180'] = 415000. #6199394500. #1493830.* 4150.
nRun['HTBM200'] = 410000. #6124047000. #1493670.* 4100.
nRun['HTBM220'] = 1471367.   
nRun['HTBM250'] = 400000. #5896336000. #1474084.* 4000.
nRun['HTBM300'] = 395000. #5855329900. #1482362.* 3950.
nRun['HTBM350'] = 365000. #5437496250. #1489725.* 3650.
nRun['HTBM400'] = 410000. #6103887300. #1488753.* 4100.
nRun['HTBM450'] = 405000. #5994032400. #1480008.* 4050.
nRun['HTBM500'] = 415000. #5654752650. #1362591.* 4150.
nRun['TTM700BWBW'] = 798600.0*0.333*0.333 #not used
nRun['TTM800BWBW'] = 766000.0*0.333*0.333
nRun['TTM900BWBW'] = 828000.0*0.333*0.333
nRun['TTM1000BWBW'] = 832200.0*0.333*0.333
nRun['TTM1100BWBW'] = 816400.0*0.333*0.333
nRun['TTM1200BWBW'] = 828600.0*0.333*0.333
nRun['TTM1300BWBW'] = 824000.0*0.333*0.333
nRun['TTM1400BWBW'] = 810000.0*0.333*0.333
nRun['TTM1500BWBW'] = 828200.0*0.333*0.333
nRun['TTM1600BWBW'] = 111800.0*0.333*0.333
nRun['TTM1700BWBW'] = 795000.0*0.333*0.333
nRun['TTM1800BWBW'] = 812400.0*0.333*0.333
nRun['TTM700THBW'] = 798600.0*0.333*0.333*2 #not used
nRun['TTM800THBW'] = 766000.0*0.333*0.333*2
nRun['TTM900THBW'] = 828000.0*0.333*0.333*2
nRun['TTM1000THBW'] = 832200*0.333*0.333*2
nRun['TTM1100THBW'] = 816400.0*0.333*0.333*2
nRun['TTM1200THBW'] = 828600.0*0.333*0.333*2
nRun['TTM1300THBW'] = 824000.0*0.333*0.333*2
nRun['TTM1400THBW'] = 810000.0*0.333*0.333*2
nRun['TTM1500THBW'] = 828200.0*0.333*0.333*2
nRun['TTM1600THBW'] = 111800.0*0.333*0.333*2
nRun['TTM1700THBW'] = 795000.0*0.333*0.333*2
nRun['TTM1800THBW'] = 812400.0*0.333*0.333*2
nRun['TTM700TZBW'] = 798600.0*0.333*0.333*2 #not used
nRun['TTM800TZBW'] = 766000.0*0.333*0.333*2
nRun['TTM900TZBW'] = 828000.0*0.333*0.333*2
nRun['TTM1000TZBW'] = 832200*0.333*0.333*2
nRun['TTM1100TZBW'] = 816400.0*0.333*0.333*2
nRun['TTM1200TZBW'] = 828600.0*0.333*0.333*2
nRun['TTM1300TZBW'] = 824000.0*0.333*0.333*2
nRun['TTM1400TZBW'] = 810000.0*0.333*0.333*2
nRun['TTM1500TZBW'] = 828200.0*0.333*0.333*2
nRun['TTM1600TZBW'] = 111800.0*0.333*0.333*2
nRun['TTM1700TZBW'] = 795000.0*0.333*0.333*2
nRun['TTM1800TZBW'] = 812400.0*0.333*0.333*2
nRun['TTM700TZTZ'] = 798600.0*0.333*0.333 #not used
nRun['TTM800TZTZ'] = 766000.0*0.333*0.333
nRun['TTM900TZTZ'] = 828000.0*0.333*0.333
nRun['TTM1000TZTZ'] = 832200*0.333*0.333
nRun['TTM1100TZTZ'] = 816400.0*0.333*0.333
nRun['TTM1200TZTZ'] = 828600.0*0.333*0.333
nRun['TTM1300TZTZ'] = 824000.0*0.333*0.333
nRun['TTM1400TZTZ'] = 810000.0*0.333*0.333
nRun['TTM1500TZTZ'] = 828200.0*0.333*0.333
nRun['TTM1600TZTZ'] = 111800.0*0.333*0.333
nRun['TTM1700TZTZ'] = 795000.0*0.333*0.333
nRun['TTM1800TZTZ'] = 812400.0*0.333*0.333
nRun['TTM700TZTH'] = 798600.0*0.333*0.333*2 #not used
nRun['TTM800TZTH'] = 766000.0*0.333*0.333*2
nRun['TTM900TZTH'] = 828000.0*0.333*0.333*2
nRun['TTM1000TZTH'] = 832200*0.333*0.333*2
nRun['TTM1100TZTH'] = 816400.0*0.333*0.333*2
nRun['TTM1200TZTH'] = 828600.0*0.333*0.333*2
nRun['TTM1300TZTH'] = 824000.0*0.333*0.333*2
nRun['TTM1400TZTH'] = 810000.0*0.333*0.333*2
nRun['TTM1500TZTH'] = 828200.0*0.333*0.333*2
nRun['TTM1600TZTH'] = 111800.0*0.333*0.333*2
nRun['TTM1700TZTH'] = 795000.0*0.333*0.333*2
nRun['TTM1800TZTH'] = 812400.0*0.333*0.333*2
nRun['TTM700THTH'] = 798600.0*0.333*0.333 #not used
nRun['TTM800THTH'] = 766000.0*0.333*0.333
nRun['TTM900THTH'] = 828000.0*0.333*0.333
nRun['TTM1000THTH'] = 832200*0.333*0.333
nRun['TTM1100THTH'] = 816400.0*0.333*0.333
nRun['TTM1200THTH'] = 828600.0*0.333*0.333
nRun['TTM1300THTH'] = 824000.0*0.333*0.333
nRun['TTM1400THTH'] = 810000.0*0.333*0.333
nRun['TTM1500THTH'] = 828200.0*0.333*0.333
nRun['TTM1600THTH'] = 111800.0*0.333*0.333
nRun['TTM1700THTH'] = 795000.0*0.333*0.333
nRun['TTM1800THTH'] = 812400.0*0.333*0.333

nRun['BBM700TWTW'] = 814800.0*0.333*0.333
nRun['BBM800TWTW'] = 826200.0*0.333*0.333
nRun['BBM900TWTW'] = 799800.0*0.333*0.333
nRun['BBM1000TWTW'] = 825600.0*0.333*0.333
nRun['BBM1100TWTW'] = 832000.0*0.333*0.333
nRun['BBM1200TWTW'] = 832200.0*0.333*0.333
nRun['BBM1300TWTW'] = 807200.0*0.333*0.333
nRun['BBM1400TWTW'] = 816800.0*0.333*0.333
nRun['BBM1500TWTW'] = 831000.0*0.333*0.333
nRun['BBM1600TWTW'] = 696600.0*0.333*0.333
nRun['BBM1700TWTW'] = 832600.0*0.333*0.333
nRun['BBM1800TWTW'] = 795400.0*0.333*0.333
nRun['BBM700BHTW'] = 814800.0*0.333*0.333*2
nRun['BBM800BHTW'] = 826200.0*0.333*0.333*2
nRun['BBM900BHTW'] = 799800.0*0.333*0.333*2
nRun['BBM1000BHTW'] = 825600.0*0.333*0.333*2
nRun['BBM1100BHTW'] = 832000.0*0.333*0.333*2
nRun['BBM1200BHTW'] = 832200.0*0.333*0.333*2
nRun['BBM1300BHTW'] = 807200.0*0.333*0.333*2
nRun['BBM1400BHTW'] = 816800.0*0.333*0.333*2
nRun['BBM1500BHTW'] = 831000.0*0.333*0.333*2
nRun['BBM1600BHTW'] = 696600.0*0.333*0.333*2
nRun['BBM1700BHTW'] = 832600.0*0.333*0.333*2
nRun['BBM1800BHTW'] = 795400.0*0.333*0.333*2
nRun['BBM700BZTW'] = 814800.0*0.333*0.333*2
nRun['BBM800BZTW'] = 826200.0*0.333*0.333*2
nRun['BBM900BZTW'] = 799800.0*0.333*0.333*2
nRun['BBM1000BZTW'] = 825600.0*0.333*0.333*2
nRun['BBM1100BZTW'] = 832000.0*0.333*0.333*2
nRun['BBM1200BZTW'] = 832200.0*0.333*0.333*2
nRun['BBM1300BZTW'] = 807200.0*0.333*0.333*2
nRun['BBM1400BZTW'] = 816800.0*0.333*0.333*2
nRun['BBM1500BZTW'] = 831000.0*0.333*0.333*2
nRun['BBM1600BZTW'] = 696600.0*0.333*0.333*2
nRun['BBM1700BZTW'] = 832600.0*0.333*0.333*2
nRun['BBM1800BZTW'] = 795400.0*0.333*0.333*2
nRun['BBM700BZBZ'] = 814800.0*0.333*0.333
nRun['BBM800BZBZ'] = 826200.0*0.333*0.333
nRun['BBM900BZBZ'] = 799800.0*0.333*0.333
nRun['BBM1000BZBZ'] = 825600.0*0.333*0.333
nRun['BBM1100BZBZ'] = 832000.0*0.333*0.333
nRun['BBM1200BZBZ'] = 832200.0*0.333*0.333
nRun['BBM1300BZBZ'] = 807200.0*0.333*0.333
nRun['BBM1400BZBZ'] = 816800.0*0.333*0.333
nRun['BBM1500BZBZ'] = 831000.0*0.333*0.333
nRun['BBM1600BZBZ'] = 696600.0*0.333*0.333
nRun['BBM1700BZBZ'] = 832600.0*0.333*0.333
nRun['BBM1800BZBZ'] = 795400.0*0.333*0.333
nRun['BBM700BZBH'] = 814800.0*0.333*0.333*2
nRun['BBM800BZBH'] = 826200.0*0.333*0.333*2
nRun['BBM900BZBH'] = 799800.0*0.333*0.333*2
nRun['BBM1000BZBH'] = 825600.0*0.333*0.333*2
nRun['BBM1100BZBH'] = 832000.0*0.333*0.333*2
nRun['BBM1200BZBH'] = 832200.0*0.333*0.333*2
nRun['BBM1300BZBH'] = 807200.0*0.333*0.333*2
nRun['BBM1400BZBH'] = 816800.0*0.333*0.333*2
nRun['BBM1500BZBH'] = 831000.0*0.333*0.333*2
nRun['BBM1600BZBH'] = 696600.0*0.333*0.333*2
nRun['BBM1700BZBH'] = 832600.0*0.333*0.333*2
nRun['BBM1800BZBH'] = 795400.0*0.333*0.333*2
nRun['BBM700BHBH'] = 814800.0*0.333*0.333
nRun['BBM800BHBH'] = 826200.0*0.333*0.333
nRun['BBM900BHBH'] = 799800.0*0.333*0.333
nRun['BBM1000BHBH'] = 825600.0*0.333*0.333
nRun['BBM1100BHBH'] = 832000.0*0.333*0.333
nRun['BBM1200BHBH'] = 832200.0*0.333*0.333
nRun['BBM1300BHBH'] = 807200.0*0.333*0.333
nRun['BBM1400BHBH'] = 816800.0*0.333*0.333
nRun['BBM1500BHBH'] = 831000.0*0.333*0.333
nRun['BBM1600BHBH'] = 696600.0*0.333*0.333
nRun['BBM1700BHBH'] = 832600.0*0.333*0.333
nRun['BBM1800BHBH'] = 795400.0*0.333*0.333

nRun['X53X53M700left']  = 300000.
nRun['X53X53M700right'] = 299800.
nRun['X53X53M800left']  = 300000.
nRun['X53X53M800right'] = 300000.
nRun['X53X53M900left']  = 300000.
nRun['X53X53M900right'] = 300000.
nRun['X53X53M1000left']  = 300000.
nRun['X53X53M1000right'] = 300000.
nRun['X53X53M1100left']  = 300000.
nRun['X53X53M1100right'] = 300000.
nRun['X53X53M1200left']  = 300000.
nRun['X53X53M1200right'] = 299800.
nRun['X53X53M1300left']  = 299800.
nRun['X53X53M1300right'] = 300000.
nRun['X53X53M1400left']  = 300000.
nRun['X53X53M1400right'] = 299800.
nRun['X53X53M1500left']  = 296400.
nRun['X53X53M1500right'] = 300000.
nRun['X53X53M1600left']  = 300000.
nRun['X53X53M1600right'] = 300000.

#energy scale samples (Q^2)
nRun['TTJetsPHQ2U'] = 9933327.
nRun['TTJetsPHQ2D'] = 9942427.
nRun['TtWQ2U'] = 497600. #not used
nRun['TtWQ2D'] = 499200. #not used
nRun['TbtWQ2U'] = 500000. #not used
nRun['TbtWQ2D'] = 497600. #not used



# Cross sections for MC samples (in pb)
xsec={}
xsec['DY'] = 6025.2 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['DYMG'] = 1921.8*3. # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['DYMG100'] = 147.4*1.23 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['DYMG200'] = 40.99*1.23 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['DYMG400'] = 5.678*1.23 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['DYMG600'] = 1.367*1.23 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['DYMG800'] = 0.6304*1.23 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['DYMG1200'] = 0.1514*1.23 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['DYMG2500'] = 0.003565*1.23 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['TTJets'] = 831.76
xsec['WJets'] = 61526.7
xsec['WJetsMG'] = 61526.7
xsec['TTJetsPH'] = 831.76 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['TTJetsPHorig'] = 831.76
xsec['TTJetsPH0to700inc'] = 831.76
xsec['TTJetsPH700to1000inc'] = 831.76*0.0921 #(xsec*filtering coeff.)
xsec['TTJetsPH1000toINFinc'] = 831.76*0.02474 #(xsec*filtering coeff.)
xsec['TTJetsPH700mtt'] = xsec['TTJetsPH700to1000inc']
xsec['TTJetsPH1000mtt'] = xsec['TTJetsPH1000toINFinc']
xsec['WJetsHT100'] = 1345.*1.21 # (1.21 = k-factor )# https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsHT200'] = 359.7*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsHT400'] = 48.91*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsHT600'] = 12.05*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsHT800'] = 5.501*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsHT1200']= 1.329*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsHT2500']= 0.03216*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsPt100'] = 676.3 #B2G-17-010 / AN2016_480_v5
xsec['WJetsPt250'] = 23.94 #B2G-17-010 / AN2016_480_v5
xsec['WJetsPt400'] = 3.031 #B2G-17-010 / AN2016_480_v5
xsec['WJetsPt600'] = 0.4524 #B2G-17-010 / AN2016_480_v5
xsec['WW'] = 118.7 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSectionsat13TeVInclusive
xsec['WZ'] = 47.13 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#Diboson
xsec['ZZ'] = 16.523 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#Diboson
xsec['TTZl'] = 0.2529 # from McM
xsec['TTZq'] = 0.5297 # from McM
xsec['TTWl'] = 0.2043 # from McM
xsec['TTWq'] = 0.4062 # from McM
xsec['Tt'] = 136.02 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma
xsec['Tbt'] = 80.95 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma
xsec['Ts'] = 11.36/3 #(1/3 was suggested by Thomas Peiffer to account for the leptonic branching ratio)# https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma
xsec['TtW'] = 35.85 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma
xsec['TbtW'] = 35.85 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma

xsec['HTBM180'] = 0.919
xsec['HTBM200'] = 0.783951
xsec['HTBM220'] = 0.648629
xsec['HTBM250'] = 0.4982015
xsec['HTBM300'] = 0.324766
xsec['HTBM350'] = 0.2184385
xsec['HTBM400'] = 0.148574
xsec['HTBM450'] = 0.104141
xsec['HTBM500'] = 0.0735225

xsec['TTM700']   = 0.455 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM800']  = 0.196 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM900']   = 0.0903 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1000']  = 0.0440 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1100']  = 0.0224 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1200'] = 0.0118 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1300']  = 0.00639 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1400'] = 0.00354 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1500']  = 0.00200 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1600'] = 0.001148 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1700']  = 0.000666 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['TTM1800'] = 0.000391 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo

xsec['BBM700']   = 0.455 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['BBM800']  = 0.196 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['BBM900']   = 0.0903 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['BBM1000']  = 0.0440 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['BBM1100']  = 0.0224 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['BBM1200'] = 0.0118 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['BBM1300']  = 0.00639 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['BBM1400'] = 0.00354 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['BBM1500']  = 0.00200 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['BBM1600'] = 0.001148 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['BBM1700']  = 0.000666 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo
xsec['BBM1800'] = 0.000391 # from https://twiki.cern.ch/twiki/bin/view/CMS/B2GMonteCarlo

xsec['X53X53M700left']   = 0.455 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top
xsec['X53X53M700right']  = 0.455 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top
xsec['X53X53M800left']   = 0.196 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top
xsec['X53X53M800right']  = 0.196 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top
xsec['X53X53M900left']   = 0.0903 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top
xsec['X53X53M900right']  = 0.0903 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top
xsec['X53X53M1000left']  = 0.0440 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top
xsec['X53X53M1000right'] = 0.0440 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top
xsec['X53X53M1100left']  = 0.0224 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top
xsec['X53X53M1100right'] = 0.0224 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top
xsec['X53X53M1200left']  = 0.0118 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top
xsec['X53X53M1200right'] = 0.0118 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top
xsec['X53X53M1300left']  = 0.00639 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top
xsec['X53X53M1300right'] = 0.00639 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top
xsec['X53X53M1400left']  = 0.00354 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top
xsec['X53X53M1400right'] = 0.00354 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top
xsec['X53X53M1500left']  = 0.00200 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top
xsec['X53X53M1500right'] = 0.00200 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top
xsec['X53X53M1600left']  = 0.001148 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top
xsec['X53X53M1600right'] = 0.001148 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GVHF#Full_NNLO_cross_sections_for_top

xsec['QCDht100'] = 27990000. # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD
xsec['QCDht200'] = 1712000. # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD 
xsec['QCDht300'] = 347700. # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD 
xsec['QCDht500'] = 32100. # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD
xsec['QCDht700'] = 6831. # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD 
xsec['QCDht1000'] = 1207. # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD
xsec['QCDht1500'] = 119.9 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD 
xsec['QCDht2000'] = 25.24 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD

#energy scale samples (Q^2)
xsec['TTJetsPHQ2U'] = xsec['TTJetsPH']
xsec['TTJetsPHQ2D'] = xsec['TTJetsPH']
xsec['TtWQ2U'] = xsec['TtW']
xsec['TtWQ2D'] = xsec['TtW']
xsec['TbtWQ2U'] = xsec['TbtW']
xsec['TbtWQ2D'] = xsec['TbtW']

# Calculate lumi normalization weights
weight = {}
for sample in sorted(nRun.keys()): 
	if 'BBM' not in sample and 'TTM' not in sample: 
		weight[sample] = (targetlumi*xsec[sample]) / (nRun[sample])
		#print sample, (xsec[sample]) / (nRun[sample])
	else: weight[sample] = (targetlumi*BR[sample[:2]+sample[-4:]]*xsec[sample[:-4]]) / (nRun[sample])
# Samples for Jet reweighting (to be able to run w/ and w/o JSF together!):
for sample in sorted(nRun.keys()):
	if 'QCDht' in sample or 'WJetsHT' in sample: weight[sample+'JSF'] = weight[sample]

# for sample in sorted(weight.keys()): 
# 	if 'BBM' in sample or 'TTM' in sample or 'X53' in sample or 'JSF' in sample: continue
# 	print sample,xsec[sample] / nRun[sample]
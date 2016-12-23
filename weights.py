#!/usr/bin/python

#targetlumi = 12892. # 1/pb
targetlumi = 36400. # 1/pb

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
nRun['DY'] = 19223750. # from 28696958
nRun['DYMG'] = 92655205.
nRun['TTJets'] = 14188545. #need negative counts
nRun['WJets'] = 6776900. # from 9908534.
nRun['WJetsMG'] = 28210360. 
nRun['TTJetsPH'] = 182123200.
nRun['TTJetsPH0to700inc'] = nRun['TTJetsPH']
nRun['TTJetsPH700to1000inc'] = nRun['TTJetsPH']*0.0921 + 37838515.
nRun['TTJetsPH1000toINFinc'] = nRun['TTJetsPH']*0.02474 + 23546331.
nRun['TTJetsPH700mtt'] = nRun['TTJetsPH']*0.0921 + 37838515.
nRun['TTJetsPH1000mtt'] = nRun['TTJetsPH']*0.02474 + 23546331.
nRun['WW'] = 993214. 
nRun['WZ'] = 1000000.
nRun['ZZ'] = 989312.
nRun['TTWl'] = 130275. #from 252673
nRun['TTWq'] = 430310. #from 833298
nRun['TTZl'] = 185232. #from 398600
nRun['TTZq'] = 351164. #from 749400
nRun['WJetsMG100'] = 27546978.
nRun['WJetsMG200'] = 14888384.
nRun['WJetsMG400'] = 5469282.
nRun['WJetsMG600'] = 3722395. #ext = 14410862.
nRun['WJetsMG800'] = 6314257.
nRun['WJetsMG1200']= 6817172.
nRun['WJetsMG2500']= 2254248.
nRun['Ts'] = 622990. #from 1000000
nRun['Tt'] = 3279200.
nRun['Tbt']= 1682400.
nRun['TtW'] = 998400.
nRun['TbtW'] = 985000.
nRun['HTBM180'] = 403236. #Ngen=1493830
nRun['HTBM200'] = 405668. #Ngen=1493670
nRun['HTBM220'] = 395089. #Ngen=1471367  
nRun['HTBM250'] = 391074. #Ngen=1474084
nRun['HTBM300'] = 385324. #Ngen=1482362, problems with jobs, extrapolated from 549690 --> 142886
nRun['HTBM350'] = 388331. #Ngen=1489725
nRun['HTBM400'] = 385633. #Ngen=1488753
nRun['HTBM450'] = 379926. #Ngen=1480008
nRun['HTBM500'] = 363317. #Ngen=1362591
nRun['HTBM750'] = 377320. #Ngen=1497192
nRun['HTBM800'] = 377648. #Ngen=1500000
nRun['HTBM1000'] = 371654. #Ngen=1472160
nRun['HTBM2000'] = 372640. #Ngen=1497510
nRun['HTBM3000'] = 378143. #Ngen=1498565
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
nRun['X53X53M900right'] = 297756.
nRun['X53X53M1000left']  = 300000.
nRun['X53X53M1000right'] = 300000.
nRun['X53X53M1100left']  = 300000.
nRun['X53X53M1100right'] = 299457.
nRun['X53X53M1200left']  = 268878.
nRun['X53X53M1200right'] = 293410.
nRun['X53X53M1300left']  = 295800.
nRun['X53X53M1300right'] = 298000.
nRun['X53X53M1400left']  = 290111.
nRun['X53X53M1400right'] = 299600.
nRun['X53X53M1500left']  = 299200.
nRun['X53X53M1500right'] = 300000.
nRun['X53X53M1600left']  = 297200.
nRun['X53X53M1600right'] = 299000.

nRun['QCDht100'] = 82073090.
nRun['QCDht200'] = 18523829.
nRun['QCDht300'] =  37875602.
nRun['QCDht500'] = 44138665.
nRun['QCDht700'] = 29832311.
nRun['QCDht1000'] = 10335975.
nRun['QCDht1500'] = 7803965.
nRun['QCDht2000'] = 4047532.

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
xsec['DYMG'] = 6025.2 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['TTJets'] = 831.76
xsec['WJets'] = 61526.7
xsec['WJetsMG'] = 61526.7
xsec['TTJetsPH'] = 831.76 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['TTJetsPH0to700inc'] = 831.76
xsec['TTJetsPH700to1000inc'] = 831.76*0.0921 #(xsec*filtering coeff.)
xsec['TTJetsPH1000toINFinc'] = 831.76*0.02474 #(xsec*filtering coeff.)
xsec['TTJetsPH700mtt'] = 831.76*0.0921 #(xsec*filtering coeff.)
xsec['TTJetsPH1000mtt'] = 831.76*0.02474 #(xsec*filtering coeff.)
xsec['WJetsMG100'] = 1345.*1.21 # (1.21 = k-factor )# https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsMG200'] = 359.7*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsMG400'] = 48.91*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsMG600'] = 12.05*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsMG800'] = 5.501*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsMG1200'] = 1.329*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsMG2500'] = 0.03216*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns 
xsec['WW'] = 118.7 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSectionsat13TeVInclusive
xsec['WZ'] = 47.13 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#Diboson
xsec['ZZ'] = 16.523 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#Diboson
xsec['TTZl'] = 0.2529 # from McM
xsec['TTZq'] = 0.5297 # from McM
xsec['TTWl'] = 0.2043 # from McM
xsec['TTWq'] = 0.4062 # from McM
xsec['Tt'] = 44.33 #(1/3 was suggested by Thomas Peiffer to account for the leptonic branching ratio)# https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma
xsec['Tbt'] = 26.38 #(1/3 was suggested by Thomas Peiffer to account for the leptonic branching ratio)# https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma
xsec['Ts'] = 3.36 #(1/3 was suggested by Thomas Peiffer to account for the leptonic branching ratio)# https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma
xsec['TtW'] = 35.6 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma
xsec['TbtW'] = 35.6 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma

xsec['HTBM180'] = (0.824531)**2/0.683584 #extrapolation using the fact that xsec proportional to exp(-m) http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['HTBM200'] = 0.824531 #was 0.783951 http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['HTBM220'] = 0.683584 #was 0.648629 http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['HTBM250'] = 0.524247 #was 0.4982015 interpolation using the fact that xsec proportional to exp(-m) http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['HTBM300'] = 0.343796 #was 0.324766 http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['HTBM350'] = 0.231218 #was 0.2184385 interpolation using the fact that xsec proportuonal to exp(-m) http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['HTBM400'] = 0.158142 #was 0.148574 http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['HTBM450'] = 0.1106674 #was 0.104141 interpolation using the fact that xsec proportional to exp(-m) http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['HTBM500'] = 0.0785572 #was 0.0735225 http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['HTBM750'] = 0.0172205 #http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['HTBM800'] = 0.0130645 #http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['HTBM1000'] = 0.00474564 #http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['HTBM2000'] = 8.70916e-05 #http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['HTBM3000'] = (8.70916e-05)**2/0.00474564 #extrapolation using the fact that xsec proportional to exp(-m) http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt

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
for sample in nRun.keys(): 
	if 'BBM' not in sample and 'TTM' not in sample: weight[sample] = (targetlumi*xsec[sample]) / (nRun[sample])
	else: weight[sample] = (targetlumi*BR[sample[:2]+sample[-4:]]*xsec[sample[:-4]]) / (nRun[sample])

for smp in weight.keys():
	if 'WJetsMG' in smp:
		weight[smp+'_bflv']=weight[smp]
		weight[smp+'_cflv']=weight[smp]
		weight[smp+'_lflv']=weight[smp]	
	if 'TTJets' in smp:
		weight[smp+'_bbflv']=weight[smp]
		weight[smp+'_llflv']=weight[smp]			
#for iPlot in MTlmet lepPt lepEta mindeltaR PtRel deltaRjet1 deltaRjet2 deltaRjet3 lepIso deltaRAK8 NPV JetEta JetPt Jet1Pt Jet2Pt Jet3Pt Jet4Pt Jet5Pt Jet6Pt MET NJets NBJets NBJetsNoSF NWJets NTJets NJetsAK8 JetPtAK8 JetEtaAK8 Tau21 Tau21Nm1 Tau32 Tau32Nm1 PrunedSmeared PrunedSmearedNm1 SoftDropMass SoftDropMassNm1 Bjet1Pt Wjet1Pt Tjet1Pt HT ST minMlb minMlj topPt deltaPhiLMET; do
#for iPlot in mindeltaR PtRel lepPt lepEta deltaRjet1 deltaRjet2 deltaRjet3 NPV JetEta JetPt Jet1Pt Jet2Pt Jet3Pt Jet4Pt MET NJets NBJets NWJets NTJets NJetsAK8 JetPtAK8 JetEtaAK8 Tau21 Tau21Nm1 Tau32 Tau32Nm1 PrunedSmeared PrunedSmearedNm1 SoftDropMass SoftDropMassNm1 HT ST minMlb topPt; do
for iPlot in lepPt lepEta deltaRjet1 deltaRjet2 deltaRjet3 NPV JetEta JetPt Jet1Pt Jet2Pt Jet3Pt Jet4Pt Jet5Pt Jet6Pt MET NJets NBJets NWJets NTJets NJetsAK8 JetPtAK8 JetEtaAK8 Tau21 Tau21Nm1 Tau32 Tau32Nm1 SoftDropMass SoftDropMassNm1W SoftDropMassNm1t mindeltaR PtRel HT ST minMlb NBJetsNoSF nTrueInt MTlmet minMlj lepIso HT_b HT_ratio HT_2m Centrality thirdcsvb_bb fourthcsvb_bb csvJet3 csvJet4 HTx MHRE GD_Ttrijet_TopMass GD_DCSV_jetNotdijet GD_DR_Tridijet GD_DR_Trijet_jetNotdijet GD_Mass_minDR_dijet GD_pTrat BD_DR_Tridijet BD_Ttrijet_TopMass BD_DR_Trijet_jetNotdijet BD_Mass_minDR_dijet BD_pTrat BD_DCSV_jetNotdijet; do
    echo $iPlot
    #python modifyBinning.py $iPlot
    python plotTemplates.py $iPlot
done

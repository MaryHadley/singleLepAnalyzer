#for iPlot in MTlmet lepPt lepEta mindeltaR PtRel deltaRjet1 deltaRjet2 deltaRjet3 lepIso deltaRAK8 NPV JetEta JetPt Jet1Pt Jet2Pt Jet3Pt Jet4Pt Jet5Pt Jet6Pt MET NJets NBJets NBJetsNoSF NWJets NTJets NJetsAK8 JetPtAK8 JetEtaAK8 Tau21 Tau21Nm1 Tau32 Tau32Nm1 PrunedSmeared PrunedSmearedNm1 SoftDropMass SoftDropMassNm1 Bjet1Pt Wjet1Pt Tjet1Pt HT ST minMlb minMlj topPt deltaPhiLMET; do
#for iPlot in mindeltaR PtRel lepPt lepEta deltaRjet1 deltaRjet2 deltaRjet3 NPV JetEta JetPt Jet1Pt Jet2Pt Jet3Pt Jet4Pt MET NJets NBJets NWJets NTJets NJetsAK8 JetPtAK8 JetEtaAK8 Tau21 Tau21Nm1 Tau32 Tau32Nm1 PrunedSmeared PrunedSmearedNm1 SoftDropMass SoftDropMassNm1 HT ST minMlb topPt; do
#for iPlot in lepPt lepEta deltaRjet1 deltaRjet2 deltaRjet3 NPV JetEta JetPt Jet1Pt Jet2Pt Jet3Pt Jet4Pt Jet5Pt Jet6Pt MET NJets NBJets NWJets NTJets NJetsAK8 JetPtAK8 JetEtaAK8 Tau21 Tau21Nm1 Tau32 Tau32Nm1 SoftDropMass SoftDropMassNm1W SoftDropMassNm1t mindeltaR PtRel HT ST  NBJetsNoSF nTrueInt MTlmet minMlj lepIso HT_b HT_ratio HT_2m Centrality thirdcsvb_bb fourthcsvb_bb csvJet3 csvJet4 HTx MHRE GD_Ttrijet_TopMass GD_DCSV_jetNotdijet GD_DR_Tridijet GD_DR_Trijet_jetNotdijet GD_Mass_minDR_dijet GD_pTrat BD_DR_Tridijet BD_Ttrijet_TopMass BD_DR_Trijet_jetNotdijet BD_Mass_minDR_dijet BD_pTrat BD_DCSV_jetNotdijet; do
for iPlot in Aplanarity FW_momentum_0 FW_momentum_1 FW_momentum_2 FW_momentum_3 FW_momentum_4 FW_momentum_5 FW_momentum_6 HT_woBESTjet MT_lepMet MT_woBESTjet M_allJet_W M_woBESTjet PT_woBESTjet PtFifthJet Sphericity W_PtdM aveBBdr invM_jet34 invM_jet35 invM_jet36 invM_jet45 invM_jet46 invM_jet56 alphaT corr_met_singleLepCalc csvJet1 csvJet2 csvJet3 csvJet4 deltaEta_maxBB deltaPhi_lepMET deltaPhi_j1j2 deltaPhi_lepJetInMinMljet deltaPhi_METjets deltaPhi_lepbJetInMinMlb deltaR_lepBJet_maxpt deltaR_lepBJets0 deltaR_lepBJets1 deltaR_lepBJets deltaR_lepJetInMinMljet deltaR_lepJets deltaR_lepbJetInMinMlb deltaR_lepbJetNotInMinMlb deltaR_minBB firstcsvb_bb fourthcsvb_bb hemiout lepDR_minBBdr mass_lepBJet0 mass_lepBB_minBBdr mass_lepBJet_mindr mass_lepJJ_minJJdr mass_lepJets0 mass_lepJets1 mass_lepJets2 mass_maxBBmass mass_maxBBpt mass_maxJJJpt mass_minBBdr mass_minLLdr mean_csv minBBdr minDR_lepBJet minMleppBjet min_deltaPhi_METjets pT_3rdcsvJet pT_4thcsvJet pTjet5_6 pt3HT pt4HT ratio_HTdHT4leadjets secondcsvb_bb theJetLeadPt thirdcsvb_bb minMleppJet; do
    echo $iPlot
    #python modifyBinning.py $iPlot
    python plotTemplates.py $iPlot
done

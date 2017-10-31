# automatically generated by prepareDQM.py
import FWCore.ParameterSet.Config as cms
from PhysicsTools.NanoAOD.nanoDQM_tools_cff import *

nanoDQM = cms.EDAnalyzer("NanoAODDQM",
    vplots = cms.PSet(
        CaloMET = cms.PSet(
            sels = cms.PSet(),
            plots = cms.VPSet(
                Plot1D('phi', 'phi', 20, -3.14159, 3.14159, 'phi'),
                Plot1D('pt', 'pt', 20, 0, 400, 'pt'),
                Plot1D('sumEt', 'sumEt', 20, 200, 3000, 'scalar sum of Et'),
            )
        ),
        Electron = cms.PSet(
            sels = cms.PSet(
                Good = cms.string('pt > 15 && abs(dxy) < 0.2 && abs(dz) < 0.5 && cutBased >= 3 && miniPFRelIso_all < 0.4')
            ),
            plots = cms.VPSet(
                Count1D('_size', 8, -0.5, 7.5, 'slimmedElectrons after basic selection (pt > 5 )'),
                Plot1D('charge', 'charge', 3, -1.5, 1.5, 'electric charge'),
                Plot1D('cleanmask', 'cleanmask', 1, 0.5, 1.5, 'simple cleaning mask with priority to leptons'),
                Plot1D('convVeto', 'convVeto', 2, -0.5, 1.5, 'pass conversion veto'),
                Plot1D('cutBased', 'cutBased', 5, -0.5, 4.5, 'cut-based ID (0:fail, 1:veto, 2:loose, 3:medium, 4:tight)'),
                Plot1D('cutBased_HLTPreSel', 'cutBased_HLTPreSel', 2, -0.5, 1.5, 'cut-based HLT pre-selection ID'),
                Plot1D('deltaEtaSC', 'deltaEtaSC', 20, -0.2, 0.2, 'delta eta (SC,ele) with sign'),
                Plot1D('dr03EcalRecHitSumEt', 'dr03EcalRecHitSumEt', 20, 0, 30, 'Non-PF Ecal isolation within a delta R cone of 0.3 with electron pt > 35 GeV'),
                Plot1D('dr03HcalDepth1TowerSumEt', 'dr03HcalDepth1TowerSumEt', 20, 0, 20, 'Non-PF Hcal isolation within a delta R cone of 0.3 with electron pt > 35 GeV'),
                Plot1D('dr03TkSumPt', 'dr03TkSumPt', 20, 0, 40, 'Non-PF track isolation within a delta R cone of 0.3 with electron pt > 35 GeV'),
                Plot1D('dxy', 'dxy', 20, -0.1, 0.1, 'dxy (with sign) wrt first PV, in cm'),
                Plot1D('dxyErr', 'dxyErr', 20, 0, 0.2, 'dxy uncertainty, in cm'),
                Plot1D('dz', 'dz', 20, -0.3, 0.3, 'dz (with sign) wrt first PV, in cm'),
                Plot1D('dzErr', 'dzErr', 20, 0, 0.2, 'dz uncertainty, in cm'),
                Plot1D('eCorr', 'eCorr', 20, 0.6, 1.6, 'ratio of the calibrated energy/miniaod energy'),
                Plot1D('energyErr', 'energyErr', 20, 0, 90, 'energy error of the cluster-track combination'),
                Plot1D('eta', 'eta', 20, -3, 3, 'eta'),
                Plot1D('genPartFlav', 'genPartFlav', 20, 0, 30, 'Flavour of genParticle for MC matching to status==1 electrons or photons: 1 = prompt electron (including gamma*->mu mu), 15 = electron from prompt tau, 22 = prompt photon (likely conversion), 5 = electron from b, 4 = electron from c, 3 = electron from light or unknown, 0 = unmatched'),
                NoPlot('genPartIdx'),
                Plot1D('hoe', 'hoe', 20, 0, 1, 'H over E'),
                Plot1D('ip3d', 'ip3d', 20, 0, 0.2, '3D impact parameter wrt first PV, in cm'),
                Plot1D('isPFcand', 'isPFcand', 2, -0.5, 1.5, 'electron is PF candidate'),
                NoPlot('jetIdx'),
                Plot1D('lostHits', 'lostHits', 2, -0.5, 1.5, 'number of missing inner hits'),
                NoPlot('mass'),
                Plot1D('miniPFRelIso_all', 'miniPFRelIso_all', 20, 0, 1, 'mini PF relative isolation, total (with scaled rho*EA PU corrections)'),
                Plot1D('miniPFRelIso_chg', 'miniPFRelIso_chg', 20, 0, 1, 'mini PF relative isolation, charged component'),
                Plot1D('mvaSpring16GP', 'mvaSpring16GP', 20, -1, 1, 'MVA general-purpose ID score'),
                Plot1D('mvaSpring16GP_WP80', 'mvaSpring16GP_WP80', 2, -0.5, 1.5, 'MVA general-purpose ID WP80'),
                Plot1D('mvaSpring16GP_WP90', 'mvaSpring16GP_WP90', 2, -0.5, 1.5, 'MVA general-purpose ID WP90'),
                Plot1D('mvaSpring16HZZ', 'mvaSpring16HZZ', 20, -1, 1, 'MVA HZZ ID score'),
                Plot1D('mvaSpring16HZZ_WPL', 'mvaSpring16HZZ_WPL', 2, -0.5, 1.5, 'MVA HZZ ID loose WP'),
                Plot1D('mvaTTH', 'mvaTTH', 20, -1, 1, 'TTH MVA lepton ID score'),
                Plot1D('pdgId', 'pdgId', 27, -13.5, 13.5, 'PDG code assigned by the event reconstruction (not by MC truth)'),
                Plot1D('pfRelIso03_all', 'pfRelIso03_all', 20, 0, 2, 'PF relative isolation dR=0.3, total (with rho*EA PU corrections)'),
                Plot1D('pfRelIso03_chg', 'pfRelIso03_chg', 20, 0, 2, 'PF relative isolation dR=0.3, charged component'),
                Plot1D('phi', 'phi', 20, -3.14159, 3.14159, 'phi'),
                NoPlot('photonIdx'),
                Plot1D('pt', 'pt', 20, 0, 200, 'pt (corrected)'),
                Plot1D('r9', 'r9', 20, 0, 1.1, 'R9 of the supercluster, calculated with full 5x5 region'),
                Plot1D('sieie', 'sieie', 20, 0, 0.05, 'sigma_IetaIeta of the supercluster, calculated with full 5x5 region'),
                Plot1D('sip3d', 'sip3d', 20, 0, 20, '3D impact parameter significance wrt first PV, in cm'),
                Plot1D('tightCharge', 'tightCharge', 3, -0.5, 2.5, 'Tight charge criteria (0:none, 1:isGsfScPixChargeConsistent, 2:isGsfCtfScPixChargeConsistent)'),
                NoPlot('vidNestedWPBitmap'),
            )
        ),
        FatJet = cms.PSet(
            sels = cms.PSet(),
            plots = cms.VPSet(
                Count1D('_size', 6, -0.5, 5.5, 'slimmedJetsAK8, i.e. ak8 fat jets for boosted analysis'),
                Plot1D('area', 'area', 20, 2, 4, 'jet catchment area, for JECs'),
                Plot1D('btagCMVA', 'btagCMVA', 20, -1, 1, 'CMVA V2 btag discriminator'),
                Plot1D('btagDeepB', 'btagDeepB', 20, -1, 1, 'CMVA V2 btag discriminator'),
                Plot1D('btagDeepBB', 'btagDeepBB', 20, -1, 1, 'CMVA V2 btag discriminator'),
                Plot1D('btagHbb', 'btagHbb', 20, -1, 1, 'Higgs to BB tagger discriminator'),
                Plot1D('eta', 'eta', 20, -4, 4, 'eta'),
                Plot1D('mass', 'mass', 20, 0, 300, 'mass'),
                Plot1D('msoftdrop', 'msoftdrop', 20, -300, 300, 'Soft drop mass'),
                Plot1D('phi', 'phi', 20, -3.14159, 3.14159, 'phi'),
                Plot1D('pt', 'pt', 20, 0, 800, 'pt'),
                NoPlot('subJetIdx1'),
                NoPlot('subJetIdx2'),
                Plot1D('tau1', 'tau1', 20, 0.00, 1.0, 'Nsubjettiness (1 axis)'),
                Plot1D('tau2', 'tau2', 20, 0.00, 1.0, 'Nsubjettiness (2 axis)'),
                Plot1D('tau3', 'tau3', 20, 0.00, 1.0, 'Nsubjettiness (3 axis)'),
                Plot1D('tau4', 'tau4', 20, 0.00, 1.0, 'Nsubjettiness (4 axis)'),
                Plot1D('n2b1', 'n2b1', 20, 0.00, 1.0, 'N2 (beta=1)'),
                Plot1D('n3b1', 'n3b1', 20, 0.00, 5.0, 'N3 (beta=1)'),
            )
        ),
        Flag = cms.PSet(
            sels = cms.PSet(),
            plots = cms.VPSet(
                Plot1D('BadChargedCandidateFilter', 'BadChargedCandidateFilter', 2, -0.5, 1.5, 'Trigger/flag bit'),
                Plot1D('BadChargedCandidateSummer16Filter', 'BadChargedCandidateSummer16Filter', 2, -0.5, 1.5, 'Trigger/flag bit'),
                Plot1D('BadPFMuonFilter', 'BadPFMuonFilter', 2, -0.5, 1.5, 'Trigger/flag bit'),
                Plot1D('BadPFMuonSummer16Filter', 'BadPFMuonSummer16Filter', 2, -0.5, 1.5, 'Trigger/flag bit'),
                Plot1D('CSCTightHalo2015Filter', 'CSCTightHalo2015Filter', 2, -0.5, 1.5, 'Trigger/flag bit'),
                Plot1D('CSCTightHaloFilter', 'CSCTightHaloFilter', 2, -0.5, 1.5, 'Trigger/flag bit'),
                Plot1D('CSCTightHaloTrkMuUnvetoFilter', 'CSCTightHaloTrkMuUnvetoFilter', 2, -0.5, 1.5, 'Trigger/flag bit'),
                Plot1D('EcalDeadCellBoundaryEnergyFilter', 'EcalDeadCellBoundaryEnergyFilter', 2, -0.5, 1.5, 'Trigger/flag bit'),
                Plot1D('EcalDeadCellTriggerPrimitiveFilter', 'EcalDeadCellTriggerPrimitiveFilter', 2, -0.5, 1.5, 'Trigger/flag bit'),
                Plot1D('HBHENoiseFilter', 'HBHENoiseFilter', 2, -0.5, 1.5, 'Trigger/flag bit'),
                Plot1D('HBHENoiseIsoFilter', 'HBHENoiseIsoFilter', 2, -0.5, 1.5, 'Trigger/flag bit'),
                Plot1D('HcalStripHaloFilter', 'HcalStripHaloFilter', 2, -0.5, 1.5, 'Trigger/flag bit'),
                Plot1D('METFilters', 'METFilters', 2, -0.5, 1.5, 'Trigger/flag bit'),
                Plot1D('chargedHadronTrackResolutionFilter', 'chargedHadronTrackResolutionFilter', 2, -0.5, 1.5, 'Trigger/flag bit'),
                Plot1D('ecalLaserCorrFilter', 'ecalLaserCorrFilter', 2, -0.5, 1.5, 'Trigger/flag bit'),
                Plot1D('eeBadScFilter', 'eeBadScFilter', 2, -0.5, 1.5, 'Trigger/flag bit'),
                Plot1D('globalSuperTightHalo2016Filter', 'globalSuperTightHalo2016Filter', 2, -0.5, 1.5, 'Trigger/flag bit'),
                Plot1D('globalTightHalo2016Filter', 'globalTightHalo2016Filter', 2, -0.5, 1.5, 'Trigger/flag bit'),
                Plot1D('goodVertices', 'goodVertices', 2, -0.5, 1.5, 'Trigger/flag bit'),
                Plot1D('hcalLaserEventFilter', 'hcalLaserEventFilter', 2, -0.5, 1.5, 'Trigger/flag bit'),
                Plot1D('muonBadTrackFilter', 'muonBadTrackFilter', 2, -0.5, 1.5, 'Trigger/flag bit'),
                Plot1D('trkPOGFilters', 'trkPOGFilters', 2, -0.5, 1.5, 'Trigger/flag bit'),
                Plot1D('trkPOG_logErrorTooManyClusters', 'trkPOG_logErrorTooManyClusters', 2, -0.5, 1.5, 'Trigger/flag bit'),
                Plot1D('trkPOG_manystripclus53X', 'trkPOG_manystripclus53X', 2, -0.5, 1.5, 'Trigger/flag bit'),
                Plot1D('trkPOG_toomanystripclus53X', 'trkPOG_toomanystripclus53X', 2, -0.5, 1.5, 'Trigger/flag bit'),
            )
        ),
        GenJet = cms.PSet(
            sels = cms.PSet(),
            plots = cms.VPSet(
                Count1D('_size', 25, -0.5, 24.5, 'slimmedGenJets, i.e. ak4 Jets made with visible genparticles'),
                Plot1D('eta', 'eta', 20, -7, 7, 'eta'),
                Plot1D('mass', 'mass', 20, 0, 200, 'mass'),
                Plot1D('phi', 'phi', 20, -3.14159, 3.14159, 'phi'),
                Plot1D('pt', 'pt', 20, 0, 200, 'pt'),
            )
        ),
        GenMET = cms.PSet(
            sels = cms.PSet(),
            plots = cms.VPSet(
                Plot1D('phi', 'phi', 20, -3.14159, 3.14159, 'phi'),
                Plot1D('pt', 'pt', 20, 0, 400, 'pt'),
            )
        ),
        GenPart = cms.PSet(
            sels = cms.PSet(),
            plots = cms.VPSet(
                Count1D('_size', 40, -0.5, 124.5, 'interesting gen particles '),
                Plot1D('eta', 'eta', 20, -30000, 30000, 'eta'),
                NoPlot('genPartIdxMother'),
                Plot1D('mass', 'mass', 20, 0, 300, 'Mass stored for all particles with mass > 10 GeV and photons with mass > 1 GeV. For other particles you can lookup from PDGID'),
                Plot1D('pdgId', 'pdgId', 20, -6000, 6000, 'PDG id'),
                Plot1D('phi', 'phi', 20, -3.14159, 3.14159, 'phi'),
                Plot1D('pt', 'pt', 20, 0, 200, 'pt'),
                Plot1D('status', 'status', 20, 0, 100, 'Particle status. 1=stable'),
            )
        ),
        GenVisTau = cms.PSet(
            sels = cms.PSet(),
            plots = cms.VPSet(
                Count1D('_size', 4, -0.5, 3.5, 'gen hadronic taus '),
                Plot1D('charge', 'charge', 3, -1.5, 1.5, 'charge'),
                Plot1D('eta', 'eta', 20, -5, 5, 'eta'),
                NoPlot('genPartIdxMother'),
                Plot1D('mass', 'mass', 20, 0, 2, 'mass'),
                Plot1D('phi', 'phi', 20, -3.14159, 3.14159, 'phi'),
                Plot1D('pt', 'pt', 20, 0, 200, 'pt'),
                Plot1D('status', 'status', 16, -0.5, 15.5, 'Hadronic tau decay mode. 0=OneProng0PiZero, 1=OneProng1PiZero, 2=OneProng2PiZero, 10=ThreeProng0PiZero, 11=ThreeProng1PiZero, 15=Other'),
            )
        ),
        IsoTrack = cms.PSet(
            sels = cms.PSet(),
            plots = cms.VPSet(
                Count1D('_size', 5, -0.5, 4.5, 'isolated tracks after basic selection (pt > 10 && abs(dxy) < 0.02 && abs(dz) < 0.1 && isHighPurityTrack && miniPFIsolation.chargedHadronIso/pt < 0.2) and lepton veto'),
                Plot1D('dxy', 'dxy', 20, -0.02, 0.02, 'dxy (with sign) wrt first PV, in cm'),
                Plot1D('dz', 'dz', 20, -0.09, 0.09, 'dz (with sign) wrt first PV, in cm'),
                Plot1D('eta', 'eta', 20, -3, 3, 'eta'),
                Plot1D('isHighPurityTrack', 'isHighPurityTrack', 2, -0.5, 1.5, 'track is high purity'),
                Plot1D('isPFcand', 'isPFcand', 2, -0.5, 1.5, 'if isolated track is a PF candidate'),
                Plot1D('miniPFRelIso_all', 'miniPFRelIso_all', 20, 0, 2, 'mini PF relative isolation, total (with scaled rho*EA PU corrections)'),
                Plot1D('miniPFRelIso_chg', 'miniPFRelIso_chg', 20, 0, 2, 'mini PF relative isolation, charged component'),
                Plot1D('pdgId', 'pdgId', 20, -300, 300, 'PDG id of PF cand'),
                Plot1D('pfRelIso03_all', 'pfRelIso03_all', 20, 0, 2, 'PF relative isolation dR=0.3, total (deltaBeta corrections)'),
                Plot1D('pfRelIso03_chg', 'pfRelIso03_chg', 20, 0, 2, 'PF relative isolation dR=0.3, charged component'),
                Plot1D('phi', 'phi', 20, -3.14159, 3.14159, 'phi'),
                Plot1D('pt', 'pt', 20, 0, 200, 'pt'),
            )
        ),
        Jet = cms.PSet(
            sels = cms.PSet(
                CentralPt30 = cms.string('abs(eta) < 2.4 && pt > 30'),
                ForwardPt30 = cms.string('abs(eta) > 2.4 && pt > 30')
            ),
            plots = cms.VPSet(
                Count1D('_size', 20, -0.5, 19.5, 'slimmedJets, i.e. ak4 PFJets CHS with JECs applied, after basic selection (pt > 15)'),
                Plot1D('area', 'area', 20, 0.2, 0.8, 'jet catchment area, for JECs'),
                Plot1D('bReg', 'bReg', 20, 30, 500, 'pt corrected with b-jet regression'),
                Plot1D('btagCMVA', 'btagCMVA', 20, -1, 1, 'CMVA V2 btag discriminator'),
                Plot1D('btagDeepB', 'btagDeepB', 20, 0, 1, 'DeepCSV b tag discriminator'),
                Plot1D('btagDeepBB', 'btagDeepBB', 20, 0, 1, 'DeepCSV bb tag discriminator'),
                Plot1D('btagDeepC', 'btagDeepC', 20, 0, 1, 'DeepCSV charm btag discriminator'),
                Plot1D('chEmEF', 'chEmEF', 20, 0, 1, 'charged Electromagnetic Energy Fraction'),
                Plot1D('chHEF', 'chHEF', 20, 0, 2, 'charged Hadron Energy Fraction'),
                Plot1D('cleanmask', 'cleanmask', 2, -0.5, 1.5, 'simple cleaning mask with priority to leptons'),
                NoPlot('electronIdx1'),
                NoPlot('electronIdx2'),
                Plot1D('eta', 'eta', 20, -6, 6, 'eta'),
                NoPlot('genJetIdx'),
                Plot1D('hadronFlavour', 'hadronFlavour', 6, -0.5, 5.5, 'flavour from hadron ghost clustering'),
                Plot1D('jetId', 'jetId', 4, -0.5, 3.5, 'Jet ID flags bit1 is loose, bit2 is tight'),
                Plot1D('mass', 'mass', 20, 0, 200, 'mass'),
                NoPlot('muonIdx1'),
                NoPlot('muonIdx2'),
                Plot1D('nConstituents', 'nConstituents', 20, 0, 80, 'Number of particles in the jet'),
                Plot1D('nElectrons', 'nElectrons', 5, -0.5, 4.5, 'number of electrons in the jet'),
                Plot1D('nMuons', 'nMuons', 4, -0.5, 3.5, 'number of muons in the jet'),
                Plot1D('neEmEF', 'neEmEF', 20, 0, 1, 'charged Electromagnetic EnergyFraction'),
                Plot1D('neHEF', 'neHEF', 20, 0, 1, 'neutral Hadron Energy Fraction'),
                Plot1D('partonFlavour', 'partonFlavour', 40, -9.5, 30.5, 'flavour from parton matching'),
                Plot1D('phi', 'phi', 20, -3.14159, 3.14159, 'phi'),
                Plot1D('pt', 'pt', 20, 0, 400, 'pt'),
                Plot1D('puId', 'puId', 8, -0.5, 7.5, 'Pilup ID flags'),
                Plot1D('qgl', 'qgl', 20, 0, 1, 'Quark vs Gluon likelihood discriminator'),
                Plot1D('rawFactor', 'rawFactor', 20, 0.5, 1.5, '1 - Factor to get back to raw pT'),
            )
        ),
        MET = cms.PSet(
            sels = cms.PSet(),
            plots = cms.VPSet(
                Plot1D('MetUnclustEnUpDeltaX', 'MetUnclustEnUpDeltaX', 20, -20, 20, 'Delta (METx_mod-METx) Unclustered Energy Up'),
                Plot1D('MetUnclustEnUpDeltaY', 'MetUnclustEnUpDeltaY', 20, -10, 10, 'Delta (METy_mod-METy) Unclustered Energy Up'),
                Plot1D('covXX', 'covXX', 20, 0, 40000, 'xx element of met covariance matrix'),
                Plot1D('covXY', 'covXY', 20, -8000, 8000, 'xy element of met covariance matrix'),
                Plot1D('covYY', 'covYY', 20, 0, 50000, 'yy element of met covariance matrix'),
                Plot1D('phi', 'phi', 20, -3.14159, 3.14159, 'phi'),
                Plot1D('pt', 'pt', 20, 0, 400, 'pt'),
                Plot1D('significance', 'significance', 20, 0, 200, 'MET significance'),
                Plot1D('sumEt', 'sumEt', 20, 600, 5000, 'scalar sum of Et'),
            )
        ),
        Muon = cms.PSet(
            sels = cms.PSet(
                Good = cms.string('pt > 15 && abs(dxy) < 0.2 && abs(dz) < 0.5 && mediumId && miniPFRelIso_all < 0.4')
            ),
            plots = cms.VPSet(
                Count1D('_size', 5, -0.5, 4.5, 'slimmedMuons after basic selection (pt > 3 && track.isNonnull && isLooseMuon)'),
                Plot1D('charge', 'charge', 3, -1.5, 1.5, 'electric charge'),
                Plot1D('cleanmask', 'cleanmask', 2, -0.5, 1.5, 'simple cleaning mask with priority to leptons'),
                Plot1D('dxy', 'dxy', 20, -0.1, 0.1, 'dxy (with sign) wrt first PV, in cm'),
                Plot1D('dxyErr', 'dxyErr', 20, 0, 0.1, 'dxy uncertainty, in cm'),
                Plot1D('dz', 'dz', 20, -0.3, 0.3, 'dz (with sign) wrt first PV, in cm'),
                Plot1D('dzErr', 'dzErr', 20, 0, 0.2, 'dz uncertainty, in cm'),
                Plot1D('eta', 'eta', 20, -2.5, 2.5, 'eta'),
                Plot1D('genPartFlav', 'genPartFlav', 16, -0.5, 15.5, 'Flavour of genParticle for MC matching to status==1 muons: 1 = prompt muon (including gamma*->mu mu), 15 = muon from prompt tau, 5 = muon from b, 4 = muon from c, 3 = muon from light or unknown, 0 = unmatched'),
                NoPlot('genPartIdx'),
                Plot1D('highPtId', 'highPtId', 3, -0.5, 2.5, 'POG highPt muon ID (1 = tracker high pT, 2 = global high pT, which includes tracker high pT)'),
                Plot1D('ip3d', 'ip3d', 20, 0, 0.2, '3D impact parameter wrt first PV, in cm'),
                Plot1D('isPFcand', 'isPFcand', 2, -0.5, 1.5, 'muon is PF candidate'),
                NoPlot('jetIdx'),
                NoPlot('mass'),
                Profile1D('mediumId', 'mediumId', 'pt', 16, 0, 80, 'POG Medium muon ID (using the relaxed cuts in the data Run 2016 B-F periods, and standard cuts elsewhere)'),
                Plot1D('miniPFRelIso_all', 'miniPFRelIso_all', 20, 0, 1, 'mini PF relative isolation, total (with scaled rho*EA PU corrections)'),
                Plot1D('miniPFRelIso_chg', 'miniPFRelIso_chg', 20, 0, 1, 'mini PF relative isolation, charged component'),
                Plot1D('mvaTTH', 'mvaTTH', 20, -1, 1, 'TTH MVA lepton ID score'),
                Plot1D('nStations', 'nStations', 5, -0.5, 4.5, 'number of matched stations with default arbitration (segment & track)'),
                Plot1D('nTrackerLayers', 'nTrackerLayers', 15, 2.5, 17.5, 'number of layers in the tracker'),
                Plot1D('pdgId', 'pdgId', 27, -13.5, 13.5, 'PDG code assigned by the event reconstruction (not by MC truth)'),
                Plot1D('pfRelIso03_all', 'pfRelIso03_all', 20, 0, 2, 'PF relative isolation dR=0.3, total (deltaBeta corrections)'),
                Plot1D('pfRelIso03_chg', 'pfRelIso03_chg', 20, 0, 2, 'PF relative isolation dR=0.3, charged component'),
                Plot1D('pfRelIso04_all', 'pfRelIso04_all', 20, 0, 2, 'PF relative isolation dR=0.4, total (deltaBeta corrections)'),
                Plot1D('phi', 'phi', 20, -3.14159, 3.14159, 'phi'),
                Plot1D('pt', 'pt', 20, 0, 200, 'pt'),
                Plot1D('ptErr', 'ptErr', 20, 0, 20, 'ptError of the muon track'),
                Plot1D('segmentComp', 'segmentComp', 20, 0, 1, 'muon segment compatibility'),
                Plot1D('sip3d', 'sip3d', 20, 0, 20, '3D impact parameter significance wrt first PV'),
                Profile1D('softId', 'softId', 'pt', 20, 0, 40, 'POG Soft muon ID (using the relaxed cuts in the data Run 2016 B-F periods, and standard cuts elsewhere)'),
                Plot1D('tightCharge', 'tightCharge', 1, 1.5, 2.5, 'Tight charge criterion using pterr/pt of muonBestTrack (0:fail, 2:pass)'),
                Profile1D('tightId', 'tightId', 'pt', 16, 0, 80, 'POG Tight muon ID'),
            )
        ),
        OtherPV = cms.PSet(
            sels = cms.PSet(),
            plots = cms.VPSet(
                NoPlot('_size'),
                Plot1D('z', 'z', 20, -20, 20, 'Z position of other primary vertices, excluding the main PV'),
            )
        ),
        PV = cms.PSet(
            sels = cms.PSet(),
            plots = cms.VPSet(
                Plot1D('chi2', 'chi2', 20, 0.5, 3, 'main primary vertex reduced chi2'),
                Plot1D('ndof', 'ndof', 20, 0, 500, 'main primary vertex number of degree of freedom'),
                Plot1D('npvs', 'npvs', 20, 0, 60, 'total number of reconstructed primary vertices'),
                Plot1D('score', 'score', 20, 0, 300000, 'main primary vertex score, i.e. sum pt2 of clustered objects'),
                Plot1D('x', 'x', 20, -0.3, 0.3, 'main primary vertex position x coordinate'),
                Plot1D('y', 'y', 20, -0.3, 0.3, 'main primary vertex position y coordinate'),
                Plot1D('z', 'z', 20, -20, 20, 'main primary vertex position z coordinate'),
            )
        ),
        Photon = cms.PSet(
            sels = cms.PSet(),
            plots = cms.VPSet(
                Count1D('_size', 9, -0.5, 8.5, 'slimmedPhotons after basic selection (pt > 5 )'),
                Plot1D('charge', 'charge', 1, -0.5, 0.5, 'electric charge'),
                Plot1D('cleanmask', 'cleanmask', 1, 0.5, 1.5, 'simple cleaning mask with priority to leptons'),
                Plot1D('cutBased', 'cutBased', 4, -0.5, 3.5, 'cut-based ID (0:fail, 1::loose, 2:medium, 3:tight)'),
                Plot1D('eCorr', 'eCorr', 20, 0.6, 1.6, 'ratio of the calibrated energy/miniaod energy'),
                NoPlot('electronIdx'),
                Plot1D('electronVeto', 'electronVeto', 2, -0.5, 1.5, 'pass electron veto'),
                Plot1D('energyErr', 'energyErr', 20, 0, 300, 'energy error of the cluster from regression'),
                Plot1D('eta', 'eta', 20, -3, 3, 'eta'),
                Plot1D('genPartFlav', 'genPartFlav', 14, -0.5, 13.5, 'Flavour of genParticle for MC matching to status==1 photons or electrons: 1 = prompt photon, 13 = prompt electron, 0 = unknown or unmatched'),
                NoPlot('genPartIdx'),
                Plot1D('hoe', 'hoe', 20, 0, 0.6, 'H over E'),
                NoPlot('jetIdx'),
                NoPlot('mass'),
                Plot1D('mvaID', 'mvaID', 20, -1, 1, 'MVA ID score'),
                Plot1D('mvaID_WP80', 'mvaID_WP80', 2, -0.5, 1.5, 'MVA ID WP80'),
                Plot1D('mvaID_WP90', 'mvaID_WP90', 2, -0.5, 1.5, 'MVA ID WP90'),
                Plot1D('pdgId', 'pdgId', 1, 21.5, 22.5, 'PDG code assigned by the event reconstruction (not by MC truth)'),
                Plot1D('pfRelIso03_all', 'pfRelIso03_all', 20, 0, 2, 'PF relative isolation dR=0.3, total (with rho*EA PU corrections)'),
                Plot1D('pfRelIso03_chg', 'pfRelIso03_chg', 20, 0, 2, 'PF relative isolation dR=0.3, charged component (with rho*EA PU corrections)'),
                Plot1D('phi', 'phi', 20, -3.14159, 3.14159, 'phi'),
                Plot1D('pixelSeed', 'pixelSeed', 2, -0.5, 1.5, 'has pixel seed'),
                Plot1D('pt', 'pt', 20, 0, 200, 'pt (corrected)'),
                Plot1D('r9', 'r9', 20, 0, 1.1, 'R9 of the supercluster, calculated with full 5x5 region'),
                Plot1D('sieie', 'sieie', 20, 0, 0.05, 'sigma_IetaIeta of the supercluster, calculated with full 5x5 region'),
                NoPlot('vidNestedWPBitmap'),
            )
        ),
        Pileup = cms.PSet(
            sels = cms.PSet(),
            plots = cms.VPSet(
                Plot1D('nPU', 'nPU', 20, 0, 60, 'the number of pileup interactions that have been added to the event in the current bunch crossing'),
                Plot1D('nTrueInt', 'nTrueInt', 20, 0, 60, 'the true mean number of the poisson distribution for this event from which the number of interactions each bunch crossing has been sampled'),
            )
        ),
        PuppiMET = cms.PSet(
            sels = cms.PSet(),
            plots = cms.VPSet(
                Plot1D('phi', 'phi', 20, -3.14159, 3.14159, 'phi'),
                Plot1D('pt', 'pt', 20, 0, 400, 'pt'),
                Plot1D('sumEt', 'sumEt', 20, 200, 3000, 'scalar sum of Et'),
            )
        ),
        RawMET = cms.PSet(
            sels = cms.PSet(),
            plots = cms.VPSet(
                Plot1D('phi', 'phi', 20, -3.14159, 3.14159, 'phi'),
                Plot1D('pt', 'pt', 20, 0, 400, 'pt'),
                Plot1D('sumEt', 'sumEt', 20, 400, 4000, 'scalar sum of Et'),
            )
        ),
        SV = cms.PSet(
            sels = cms.PSet(),
            plots = cms.VPSet(
                Count1D('_size', 14, -0.5, 13.5),
                Plot1D('chi2', 'chi2', 20, -2000, 2000, 'reduced chi2, i.e. chi/ndof'),
                Plot1D('dlen', 'dlen', 20, 0, 4, 'decay length in cm'),
                Plot1D('dlenSig', 'dlenSig', 20, 0, 50, 'decay length significance'),
                Plot1D('eta', 'eta', 20, -3, 3, 'eta'),
                Plot1D('mass', 'mass', 20, 0, 8, 'mass'),
                Plot1D('ndof', 'ndof', 20, -1, 19, 'number of degrees of freedom'),
                Plot1D('phi', 'phi', 20, -3.14159, 3.14159, 'phi'),
                Plot1D('pt', 'pt', 20, 0, 200, 'pt'),
                Plot1D('x', 'x', 20, -0.5, 0.5, 'secondary vertex X position, in cm'),
                Plot1D('y', 'y', 20, -0.5, 0.5, 'secondary vertex Y position, in cm'),
                Plot1D('z', 'z', 20, -10, 10, 'secondary vertex Z position, in cm'),
            )
        ),
        SoftActivityJet = cms.PSet(
            sels = cms.PSet(),
            plots = cms.VPSet(
                Count1D('_size', 7, -0.5, 6.5, 'jets clustered from charged candidates compatible with primary vertex (charge()!=0 && pvAssociationQuality()>=5 && vertexRef().key()==0)'),
                Plot1D('eta', 'eta', 20, -3, 3, 'eta'),
                Plot1D('phi', 'phi', 20, -3.14159, 3.14159, 'phi'),
                Plot1D('pt', 'pt', 20, 0, 200, 'pt'),
            )
        ),
        SubJet = cms.PSet(
            sels = cms.PSet(),
            plots = cms.VPSet(
                Count1D('_size', 9, -0.5, 8.5, 'slimmedJetsAK8, i.e. ak8 fat jets for boosted analysis'),
                Plot1D('btagCMVA', 'btagCMVA', 20, -1, 1, 'CMVA V2 btag discriminator'),
                Plot1D('btagDeepB', 'btagDeepB', 20, -1, 1, 'CMVA V2 btag discriminator'),
                Plot1D('btagDeepBB', 'btagDeepBB', 20, -1, 1, 'CMVA V2 btag discriminator'),
                Plot1D('eta', 'eta', 20, -4, 4, 'eta'),
                Plot1D('mass', 'mass', 20, -200, 200, 'mass'),
                Plot1D('phi', 'phi', 20, -3.14159, 3.14159, 'phi'),
                Plot1D('pt', 'pt', 20, 0, 200, 'pt'),
            )
        ),
        Tau = cms.PSet(
            sels = cms.PSet(),
            plots = cms.VPSet(
                Count1D('_size', 7, -0.5, 6.5, "slimmedTaus after basic selection (pt > 18 && tauID('decayModeFindingNewDMs') && (tauID('byLooseCombinedIsolationDeltaBetaCorr3Hits') || tauID('byVLooseIsolationMVArun2v1DBoldDMwLT') || tauID('byVLooseIsolationMVArun2v1DBnewDMwLT') || tauID('byVLooseIsolationMVArun2v1DBdR03oldDMwLT')))"),
                Plot1D('charge', 'charge', 3, -1.5, 1.5, 'electric charge'),
                Plot1D('chargedIso', 'chargedIso', 20, 0, 200, 'charged isolation'),
                Plot1D('cleanmask', 'cleanmask', 1, 0.5, 1.5, 'simple cleaning mask with priority to leptons'),
                Plot1D('decayMode', 'decayMode', 12, -0.5, 11.5, 'decayMode()'),
                Plot1D('dxy', 'dxy', 20, -1000, 1000, 'd_{xy} of lead track with respect to PV, in cm (with sign)'),
                Plot1D('dz', 'dz', 20, -20, 20, 'd_{z} of lead track with respect to PV, in cm (with sign)'),
                Plot1D('eta', 'eta', 20, -3, 3, 'eta'),
                Plot1D('footprintCorr', 'footprintCorr', 20, 0, 30, 'footprint correction'),
                Plot1D('genPartFlav', 'genPartFlav', 6, -0.5, 5.5, 'Flavour of genParticle for MC matching to status==2 taus: 1 = prompt electron, 2 = prompt muon, 3 = tau->e decay, 4 = tau->mu decay, 5 = hadronic tau decay, 0 = unknown or unmatched'),
                NoPlot('genPartIdx'),
                Plot1D('idAntiEle', 'idAntiEle', 2, -0.5, 1.5, 'Anti-electron MVA discriminator V6: bitmask 1 = VLoose, 2 = Loose, 4 = Medium, 8 = Tight, 16 = VTight'),
                Plot1D('idAntiMu', 'idAntiMu', 2, -0.5, 1.5, 'Anti-muon discriminator V3: : bitmask 1 = Loose, 2 = Tight'),
                Plot1D('idDecayMode', 'idDecayMode', 2, -0.5, 1.5, "tauID('decayModeFinding')"),
                Plot1D('idDecayModeNewDMs', 'idDecayModeNewDMs', 2, -0.5, 1.5, "tauID('decayModeFindingNewDMs')"),
                Plot1D('idMVAnewDM', 'idMVAnewDM', 2, -0.5, 1.5, 'IsolationMVArun2v1DBnewDMwLT ID working point: bitmask 1 = VLoose, 2 = Loose, 4 = Medium, 8 = Tight, 16 = VTight, 32 = VVTight'),
                Plot1D('idMVAoldDM', 'idMVAoldDM', 2, -0.5, 1.5, 'IsolationMVArun2v1DBoldDMwLT ID working point: bitmask 1 = VLoose, 2 = Loose, 4 = Medium, 8 = Tight, 16 = VTight, 32 = VVTight'),
                Plot1D('idMVAoldDMdR03', 'idMVAoldDMdR03', 2, -0.5, 1.5, 'IsolationMVArun2v1DBdR03oldDMwLT ID working point: bitmask 1 = VLoose, 2 = Loose, 4 = Medium, 8 = Tight, 16 = VTight, 32 = VVTight'),
                NoPlot('jetIdx'),
                Plot1D('leadTkDeltaEta', 'leadTkDeltaEta', 20, -0.1, 0.1, 'eta of the leading track, minus tau eta'),
                Plot1D('leadTkDeltaPhi', 'leadTkDeltaPhi', 20, -0.1, 0.1, 'phi of the leading track, minus tau phi'),
                Plot1D('leadTkPtOverTauPt', 'leadTkPtOverTauPt', 20, 0, 2, 'pt of the leading track divided by tau pt'),
                Plot1D('mass', 'mass', 20, 0, 5, 'mass'),
                Plot1D('neutralIso', 'neutralIso', 20, 0, 200, 'neutral (photon) isolation'),
                Plot1D('phi', 'phi', 20, -3.14159, 3.14159, 'phi'),
                Plot1D('photonsOutsideSignalCone', 'photonsOutsideSignalCone', 20, 0, 30, 'sum of photons outside signal cone'),
                Plot1D('pt', 'pt', 20, 0, 200, 'pt'),
                Plot1D('puCorr', 'puCorr', 20, 0, 90, 'pileup correction'),
                Plot1D('rawAntiEle', 'rawAntiEle', 20, -100, 100, 'Anti-electron MVA discriminator V6 raw output discriminator'),
                Plot1D('rawAntiEleCat', 'rawAntiEleCat', 17, -1.5, 15.5, 'Anti-electron MVA discriminator V6 category'),
                Plot1D('rawIso', 'rawIso', 20, 0, 200, 'combined isolation (deltaBeta corrections)'),
                Plot1D('rawMVAnewDM', 'rawMVAnewDM', 20, -1, 1, 'byIsolationMVArun2v1DBnewDMwLT raw output discriminator'),
                Plot1D('rawMVAoldDM', 'rawMVAoldDM', 20, -1, 1, 'byIsolationMVArun2v1DBoldDMwLT raw output discriminator'),
                Plot1D('rawMVAoldDMdR03', 'rawMVAoldDMdR03', 20, -1, 1, 'byIsolationMVArun2v1DBdR03oldDMwLT raw output discriminator'),
            )
        ),
        TkMET = cms.PSet(
            sels = cms.PSet(),
            plots = cms.VPSet(
                Plot1D('phi', 'phi', 20, -3.14159, 3.14159, 'phi'),
                Plot1D('pt', 'pt', 20, 0, 400, 'pt'),
                Plot1D('sumEt', 'sumEt', 20, 0, 2000, 'scalar sum of Et'),
            )
        ),
        TrigObj = cms.PSet(
            sels = cms.PSet(
                Electron = cms.string('id == 11'),
                HT = cms.string('id == 3'),
                Jet = cms.string('id == 1'),
                MET = cms.string('id == 2'),
                MHT = cms.string('id == 4'),
                Muon = cms.string('id == 13'),
                Photon = cms.string('id == 22'),
                Tau = cms.string('id == 15')
            ),
            plots = cms.VPSet(
                Count1D('_size', 28, -0.5, 27.5),
                Plot1D('eta', 'eta', 20, -5, 5, 'eta'),
                Plot1D('filterBits', 'filterBits', 16, -0.5, 15.5, 'extra bits of associated information: 1 = CaloIdL_TrackIdL_IsoVL, 2 = WPLoose, 4 = WPTight for Electron (PixelMatched e/gamma); 1 = TrkIsoVVL, 2 = Iso for Muon; '),
                Plot1D('id', 'id', 20, 0, 30, 'ID of the object: 11 = Electron (PixelMatched e/gamma), 22 = Photon (PixelMatch-vetoed e/gamma), 13 = Muon, 14 = Tau, 1 = Jet, 2 = MET, 3 = HT, 4 = MHT'),
                Plot1D('l1pt', 'l1pt', 20, 0, 200, 'pt of associated L1 seed'),
                Plot1D('l2pt', 'l2pt', 20, 0, 200, "pt of associated 'L2' seed (i.e. HLT before tracking/PF)"),
                Plot1D('phi', 'phi', 20, -3.14159, 3.14159, 'phi'),
                Plot1D('pt', 'pt', 40, 0, 400, 'pt'),
            )
        ),
    )
)

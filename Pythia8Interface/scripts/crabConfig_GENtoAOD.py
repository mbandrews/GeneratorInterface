from CRABClient.UserUtilities import config#, getUsernameFromSiteDB
config = config()

#CFG = 'DoublePi0Pt10To200_m0To2600_Eta0To1p4'
#CFG = 'DoublePi0Pt10To200_m0To2600_Eta1p5To2p4'
#CFG = 'DoublePi0Pt1e2To1e3_m0To1600_Eta0To1p4'
#CFG = 'OctoPi0Pt15To1e2To1e3_m0To1p2To3p6_Eta0To1p4'
#CFG = 'OctoPi0Pt10To200_m0To1600_Eta1p6To2p4'
#CFG = 'OctoPi0Pt15To120_m0To3p6_Eta0To1p4'
#CFG = 'OctoPi0Pt120To1e3_m0To3p6_Eta0To1p4'
#CFG = 'OctoPi0Pt10To120_m0To1600flat_Eta1p6To2p4flat'
#CFG = 'OctoPi0_e60_m200_ctau2em5To1p1e2_eta0To1p4'
#CFG = 'OctoPi0_e60_m200_ctau2em5To12_eta0To1p4'
CFG = 'OctoPi0_e60_m200_ctau0To4_eta0To1p4'

PU = 'noPU'
PROC = 'GEN2AOD'
EVTCONT = 'AODSIM'

config.General.requestName = '%s_%s_%s'%(CFG,PU,PROC)
config.General.workArea = 'crab_MC'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '%s_%s_%s_cfg.py'%(CFG,PU,PROC)
config.JobType.maxMemoryMB = 2800
#config.JobType.numCores = 4

config.Data.outputPrimaryDataset = EVTCONT
config.Data.splitting = 'EventBased'

# pi0, var mass
#config.Data.unitsPerJob = 180
#config.Data.totalUnits = 1800000
#config.Data.unitsPerJob = 150
#config.Data.totalUnits = 1500000
# pho/ele, pi0 fixed mass
#config.Data.unitsPerJob = 100
#config.Data.totalUnits = 500000
# test
#config.Data.unitsPerJob = 100
#config.Data.totalUnits = 100000
config.Data.unitsPerJob = 250
config.Data.totalUnits = 1000000

config.Data.outLFNDirBase = '/store/group/lpcml/mandrews/'
config.Data.publication = False
config.Data.outputDatasetTag = '%s_%s_%s'%(CFG,PU,EVTCONT)

config.Site.storageSite = 'T3_US_FNALLPC'

from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

#CFG = 'DoublePi0Pt15To100_m0To1600_pythia8'
#CFG = 'DoublePhotonPt15To100_pythia8'
CFG = 'DoublePhotonPt10To100_pythia8'
#CFG = 'DoublePi0Pt15To100_m000_pythia8'
#CFG = 'DoubleElectronPt15To100_pythia8'
#CFG = 'DoublePi0Pt10To100_m0To1600_pythia8'

PU = 'PU2017'

EVTCONT = 'PREMIXRAW'

config.General.requestName = '%s_%s_%s'%(CFG,PU,EVTCONT)
#config.General.requestName = '%s_%s_%s_flat'%(CFG,PU,EVTCONT)
config.General.workArea = 'crab_MC'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = '%s_%s_%s_cfg.py'%(CFG,PU,EVTCONT)
config.JobType.maxMemoryMB = 2800
#config.JobType.numCores = 4

config.Data.outputPrimaryDataset = EVTCONT
config.Data.splitting = 'EventBased'

# pi0, var mass
#config.Data.unitsPerJob = 180
#config.Data.totalUnits = 1800000
config.Data.unitsPerJob = 150
config.Data.totalUnits = 1500000
# pho/ele, pi0 fixed mass
#config.Data.unitsPerJob = 100
#config.Data.totalUnits = 500000
# test
#config.Data.unitsPerJob = 100
#config.Data.totalUnits = 100000

config.Data.outLFNDirBase = '/store/group/lpcml/mandrews/'
config.Data.publication = False
config.Data.outputDatasetTag = '%s_%s_%s'%(CFG,PU,EVTCONT)
#config.Data.outputDatasetTag = '%s_%s_%s_flat'%(CFG,PU,EVTCONT)

config.Site.storageSite = 'T3_US_FNALLPC'

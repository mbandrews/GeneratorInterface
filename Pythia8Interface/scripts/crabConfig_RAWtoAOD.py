from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

#CFG = 'DoublePhotonPt15To100_pythia8'
CFG = 'DoublePhotonPt10To100_pythia8'
#CFG = 'DoublePi0Pt15To100_m0To1600_pythia8'
#CFG = 'DoublePi0Pt15To100_m000_pythia8'
#CFG = 'DoubleElectronPt15To100_pythia8'
#CFG = 'DoublePi0Pt10To100_m0To1600_pythia8_flat'
#CFG = 'DoublePi0Pt10To100_m0To1600_pythia8'

PU = 'PU2017'

EVTCONT = 'AODSIM'

config.General.requestName = '%s_%s_%s_ReAOD'%(CFG,PU,EVTCONT)
config.General.workArea = 'crab_MC'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'DoubleGunPt10To100_%s_PREMIXRAW2AOD_cfg.py'%PU
#config.JobType.psetName = 'DoubleGunPt5To100_%s_PREMIXRAW2AOD_cfg.py'%PU
config.JobType.maxMemoryMB = 2800
#config.JobType.numCores = 4

config.Data.outputPrimaryDataset = EVTCONT
config.Data.splitting = 'FileBased'
config.Data.userInputFiles = open('LISTS/%s_%s_%s_file_index.txt'%(CFG,PU,'PREMIXRAW')).readlines()
print '>> List file[0]:',config.Data.userInputFiles[0]
#config.Data.unitsPerJob = 5
config.Data.unitsPerJob = 3
config.Data.totalUnits = len(config.Data.userInputFiles)

config.Data.outLFNDirBase = '/store/group/lpcml/mandrews/'
config.Data.publication = False
config.Data.outputDatasetTag = '%s_%s_%s_ReAOD'%(CFG,PU,EVTCONT)

config.Site.storageSite = 'T3_US_FNALLPC'

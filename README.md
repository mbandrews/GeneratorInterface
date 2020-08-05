# GeneratorInterface

CMSSW files for generating particle guns

    $ export SCRAM_ARCH=slc6_amd64_gcc630
    $ cmsrel CMSSW_9_4_13
    $ cd CMSSW_9_4_13/src
    $ cmsenv
    $ git cms-init
    $ git cms-addpkg GeneratorInterface/Pythia8Interface
    $ scram b -j 24 # -j 4 if using slc7
    $ git clone git@github.com:mbandrews/GeneratorInterface.git tmp
    $ cp -r tmp/Pythia8Interface GeneratorInterface/
    $ rm -rf tmp
    $ scram b -j 24 # -j 4 if using slc7
    $ cd GeneratorInterface/Pythia8Interface/scripts/
    $ cmsRun OctoPi0_e60_m200_ctau0To4_eta0To1p4_noPU_GEN2AOD_cfg.py

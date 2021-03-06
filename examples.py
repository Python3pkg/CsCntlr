from CsCntlr import *

if __name__ == "__main__":
    #### Getting started
    # First, create a CsCntlr instance
    cs = CsCntlr()
    
    # Then, select the mode to be used
    cs.useFixedPeriodMode()
    cs.useManualSettingMode()
    
    # You can measure colors by using the code below
    cs.cntlr.auto()
    
    #### Examples for Fixed Period Mode
    cs.useFixedPeriodMode()
    
    # You can specify the gain and the integration time (tint)
    cs.cntlr.auto(gain='low', tint=2)
    
    # gain should be 'low' or 'high' (low:high = 1:10)
    cs.cntlr.auto(gain='lolo')
    cs.cntlr.auto(gain='hi')
    
    # tint should be from 0 to 3 (3: 179.2 ms, 2: 22.4 ms, 1: 1.4 ms, 0: 0.0875 ms)
    cs.cntlr.auto(tint=100)
    cs.cntlr.auto(tint='hi')
    
    #### Examples for Manual Setting Mode
    cs.useManualSettingMode()
    
    # You can specify the manual integration time (man_tint)
    cs.cntlr.auto(gain='high', man_tint=100, tint=0)
    cs.cntlr.auto(man_tint=1)
    
    # gain should be 'low' or 'high' (low:high = 1:10)
    cs.cntlr.auto(gain='lolo')
    cs.cntlr.auto(gain='hi')
    
    # tint should be from 0 to 3 (3: 358.4 ms, 2: 44.8 ms, 1: 2.8 ms, 0: 0.175 ms)
    cs.cntlr.auto(tint=100)
    cs.cntlr.auto(tint='hi')
    
    # man_tint should be from 0 to 65535 (measurement_time = tint * man_tint)
    cs.cntlr.auto(gain='high', man_tint=70000, tint=1)
    cs.cntlr.auto(man_tint='hi')
    
    # Note that CsCntlr is Singleton
    cs1 = CsCntlr()
    cs1.useFixedPeriodMode()
    # So now, cs is changed to the Fixed Period Mode
    cs.cntlr.auto()

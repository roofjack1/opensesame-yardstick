from rflib import *
import sys

def init(device):
    device.setMdmModulation(MOD_ASK_OOK)
    device.setFreq(390e6) # or 315e6 etc.
    device.setMdmSyncMode(0x00)
    # device.setMdmSyncWord(0xEEEE)
    device.setMdmDRate(1000)
    device.makePktFLEN(0)
    device.setMdmNumPreamble(0)
    device.setPktPQT(0)
    device.setMaxPower()


    #device.printRadioConfig()
    #device.RFlisten()

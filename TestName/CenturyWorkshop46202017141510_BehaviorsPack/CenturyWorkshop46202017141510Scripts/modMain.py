# -*- coding: utf-8 -*-

from mod.common.mod import Mod
import CenturyWorkshop46202017141510Scripts.AddonConfig as modConfig
import server.extraServerApi as serverApi
import mod.client.extraClientApi as clientApi


@Mod.Binding(name=modConfig.ModName, version=modConfig.ModVersion)
class CenturyWorkshop46202017141510(object):

    def __init__(self):
        print "[CenturyWorkshop]===== init  mod ====="

    @Mod.InitServer()
    def ServerInit(self):
        print "[CenturyWorkshop]===== init addon server ====="
        serverApi.RegisterSystem(modConfig.ModName, modConfig.ServerSystemName, modConfig.ServerSystemClsPath)
    @Mod.DestroyServer()
    def ServerDestroy(self):
        print "===== destroy addon server ====="

    @Mod.InitClient()
    def ClientInit(self):
        print "[CenturyWorkshop]===== init addon client ====="
        clientApi.RegisterSystem(modConfig.ModName, modConfig.ClientSystemName, modConfig.ClientSystemClsPath)

    @Mod.DestroyClient()
    def ClientDestroy(self):
        print "===== destroy addon client ====="

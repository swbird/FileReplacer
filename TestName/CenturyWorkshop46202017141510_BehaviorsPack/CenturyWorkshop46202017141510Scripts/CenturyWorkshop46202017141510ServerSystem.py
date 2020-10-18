# -*- coding: utf-8 -*-

import server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()

class CenturyWorkshop46202017141510ServerSystem(ServerSystem):

    def __init__(self, namespace, systemName):
        super(CenturyWorkshop46202017141510ServerSystem, self).__init__(namespace, systemName)
        print "[CenturyWorkshop]===== Addon Server init ====="
        self.playerId = ""
        self.LevelId = serverApi.GetLevelId()
        self.ListenEvent()

    def ListenEvent(self):
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "AddServerPlayerEvent", self, self.OnAddServerPlayer)

    def OnAddServerPlayer(self, args):
        print "[CenturyWorkshop]Player ID:",args['id']#Player Join the game
        self.playerId = args['id']

    def Destroy(self):
        print "===== ServerSystem Destroy ====="
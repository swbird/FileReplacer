# -*- coding: utf-8 -*-
#

import client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls() 

class CenturyWorkshop46202017141510ClientSystem(clientApi.GetClientSystemCls()):
	def __init__(self, namespace, name):
		super(CenturyWorkshop46202017141510ClientSystem, self).__init__(namespace, name)
		print '[CenturyWorkshop]Addon Client Init!'
		self.ListenEvent()
		self.PlayerId = clientApi.GetLocalPlayerId()
		self.LevelId = clientApi.GetLevelId()

	def ListenEvent(self):
		self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "AddPlayerEvent", self, self.AddPlayerEventE)


	def AddPlayerEventE(self, args):
		print 'Player Get Into The world'

	def Destroy(self):
		print 'Destroy Client'
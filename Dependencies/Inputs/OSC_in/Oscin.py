from TDStoreTools import StorageManager
import TDFunctions as TDF



class Oscin:

	def __init__(self, ownerComp):
		return
		
	def Triggeraction(self, key, value):

		# FLASH COLLECTIVE: Video wird über alle Lats abgespielt
		
		if key == "/Tetraeder/ramp/left":
			op.Clipgun_flash.op("clips/video5").par.Trigger.pulse()

		elif key == "/Tetraeder/ramp/right":
			op.Clipgun_flash.op("clips/video5").par.Trigger.pulse()

		# Base Anim
		elif key == "/Tetraeder/Baseanim":
			op.Clipgun_base.op("clips/video11").par.Trigger.pulse()
		
#	def OnParamChanged(self, par):
#		if par.name == "Active":
#			return

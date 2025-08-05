from TDStoreTools import StorageManager
import TDFunctions as TDF



class Oscin:

	def __init__(self, ownerComp):
		return
		
	def Triggeraction(self, key, value):

		# FLASH COLLECTIVE: Video wird über alle Tetraeder abgespielt, aber nur, wenn individual mode eingestellt ist.
		
		if key == "/Tetraeder/ramp/left":
			op.ScenePlayer.Anim_collective_ramp("left")

		elif key == "/Tetraeder/ramp/right":
			op.ScenePlayer.Anim_collective_ramp("right")

		# Base Anim
		elif key == "/Tetraeder/Baseanim":
			op.Clipgun_base.op("clips/video11").par.Trigger.pulse()
		
	def OnParamChanged(self, par):
		if par.name == "Active":
			op.MQTT_out.SendMQTT_retained( op.MQTT_in.par.Topicprefix + "udpin/active", int(par))
			op.Logger.Debug(f"[OSC_in]: OSC IN ative: {int(par)}")
			
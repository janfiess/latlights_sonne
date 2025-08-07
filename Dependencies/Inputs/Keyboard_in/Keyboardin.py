from TDStoreTools import StorageManager
import TDFunctions as TDF



class Keyboardin:

	def __init__(self, ownerComp):
		return
		
	def Triggeraction(self, key):

		# print(f"key: {key}")

		# Flash Anims in Foreground Layer


		if key == "kr":
			# print(f"key: {key}")
			op.Clipgun_flash.op("clips/video5").par.Trigger.pulse()
			
			
			
		# Base Anims in Background Layer
			
		if key == "kt":
			# print(f"key: {key}")
			op.Clipgun_base.op("clips/video10").par.Trigger.pulse()
			



	def OnParamChanged(self, par):
		if par.name == "Active":
			op.MQTT_out.SendMQTT_retained( op.MQTT_in.par.Topicprefix + "udpin/active", int(par))
			op.Logger.Debug(f"[OSC_in]: OSC IN ative: {int(par)}")
			
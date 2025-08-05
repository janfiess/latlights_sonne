from TDStoreTools import StorageManager
import TDFunctions as TDF



class Midiin:

	def __init__(self, ownerComp):
		return
		
	def Triggeraction(self, key):

		# print(f"key: {key}")

		# Base / Background anims

		if key == "ch1n40":
			op.Clipgun_base.op("clips/video10").par.Trigger.pulse()

		# Foreground anims: collective flashes

		elif key == "ch1n25":
			op.Clipgun_flash.op("clips/video5").par.Trigger.pulse()
		elif key == "ch1n26":
			op.Clipgun_flash.op("clips/video4").par.Trigger.pulse()
		elif key == "ch1n27":
			op.Clipgun_flash.op("clips/video2").par.Trigger.pulse()
		elif key == "ch1n28":
			op.Clipgun_flash.op("clips/video3").par.Trigger.pulse()

		elif key == "ch1n29":
			op.Clipgun_flash.op("clips/video8").par.Trigger.pulse()
		elif key == "ch1n30":
			op.Clipgun_flash.op("clips/video9").par.Trigger.pulse()
		elif key == "ch1n31":
			op.Clipgun_flash.op("clips/video16").par.Trigger.pulse()
		elif key == "ch1n32":
			op.Clipgun_flash.op("clips/video10").par.Trigger.pulse()


		

#	def OnParamChanged(self, par):
#		if par.name == "Active":
#			op.MQTT_out.SendMQTT_retained( op.MQTT_in.par.Topicprefix + "udpin/active", int(par))
#			op.Logger.Debug(f"[OSC_in]: OSC IN ative: {int(par)}")
			
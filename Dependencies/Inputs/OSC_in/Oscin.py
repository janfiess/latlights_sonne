from TDStoreTools import StorageManager
import TDFunctions as TDF



class Oscin:

	def __init__(self, ownerComp):
		return
		
	def Triggeraction(self, key, value):
		
		# print(f"Key: {key}, Value: {value}")

		# FLASH COLLECTIVE: Video wird über alle Lats abgespielt
		
		if key == "/flash":
			if value == "z1s1":
				op.Clipgun_flash.op("clips/video1").par.Trigger.pulse()
			elif value == "z1s2":
				op.Clipgun_flash.op("clips/video2").par.Trigger.pulse()
			elif value == "z1s3":
				op.Clipgun_flash.op("clips/video3").par.Trigger.pulse()
			elif value == "z1s4":
				op.Clipgun_flash.op("clips/video4").par.Trigger.pulse()
			elif value == "z1s5":
				op.Clipgun_flash.op("clips/video5").par.Trigger.pulse()
			elif value == "z1s6":
				op.Clipgun_flash.op("clips/video6").par.Trigger.pulse()
			elif value == "z1s7":
				op.Clipgun_flash.op("clips/video7").par.Trigger.pulse()
			elif value == "z1s8":
				op.Clipgun_flash.op("clips/video8").par.Trigger.pulse()

			elif value == "z2s1":
				op.Clipgun_flash.op("clips/video9").par.Trigger.pulse()
			elif value == "z2s2":
				op.Clipgun_flash.op("clips/video10").par.Trigger.pulse()
			elif value == "z2s3":
				op.Clipgun_flash.op("clips/video11").par.Trigger.pulse()
			elif value == "z2s4":
				op.Clipgun_flash.op("clips/video12").par.Trigger.pulse()
			elif value == "z2s5":
				op.Clipgun_flash.op("clips/video13").par.Trigger.pulse()
			elif value == "z2s6":
				op.Clipgun_flash.op("clips/video14").par.Trigger.pulse()
			elif value == "z2s7":
				op.Clipgun_flash.op("clips/video15").par.Trigger.pulse()
			elif value == "z2s8":
				op.Clipgun_flash.op("clips/video16").par.Trigger.pulse()

			elif value == "z3s1":
				op.Clipgun_flash.op("clips/video17").par.Trigger.pulse()
			elif value == "z3s2":
				op.Clipgun_flash.op("clips/video18").par.Trigger.pulse()
			elif value == "z3s3":
				op.Clipgun_flash.op("clips/video19").par.Trigger.pulse()
			elif value == "z3s4":
				op.Clipgun_flash.op("clips/video20").par.Trigger.pulse()
			elif value == "z3s5":
				op.Clipgun_flash.op("clips/video21").par.Trigger.pulse()
			elif value == "z3s6":
				op.Clipgun_flash.op("clips/video22").par.Trigger.pulse()
			elif value == "z3s7":
				op.Clipgun_flash.op("clips/video23").par.Trigger.pulse()
			elif value == "z3s8":
				op.Clipgun_flash.op("clips/video24").par.Trigger.pulse()

			elif value == "z4s1":
				op.Clipgun_flash.op("clips/video25").par.Trigger.pulse()
			elif value == "z4s2":
				op.Clipgun_flash.op("clips/video26").par.Trigger.pulse()
			elif value == "z4s3":
				op.Clipgun_flash.op("clips/video27").par.Trigger.pulse()
			elif value == "z4s4":
				op.Clipgun_flash.op("clips/video28").par.Trigger.pulse()
			elif value == "z4s5":
				op.Clipgun_flash.op("clips/video29").par.Trigger.pulse()
			elif value == "z4s6":
				op.Clipgun_flash.op("clips/video30").par.Trigger.pulse()
			elif value == "z4s7":
				op.Clipgun_flash.op("clips/video31").par.Trigger.pulse()
			elif value == "z4s8":
				op.Clipgun_flash.op("clips/video32").par.Trigger.pulse()

			



		
	def OnParamChanged(self, par):
		return
#		if par.name == "Active":
#			return

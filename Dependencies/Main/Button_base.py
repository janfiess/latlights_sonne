from TDStoreTools import StorageManager
import TDFunctions as TDF

class Buttonbase:
	def __init__(self, ownerComp):
		return

	def Play(self):
		# print("button base")
		op.Clipgun_base.par.Latestkeypressed = parent().name
		
		moviefile_rgb = op.Clipgun_base.op("moviefilein_rgb")
		moviefile_rgb.par.cuepoint = 0
		moviefile_rgb.par.cuepulse.pulse()
		moviefile_rgb.par.play = 1

		moviefile_cwww = op.Clipgun_base.op("moviefilein_cwww")
		moviefile_cwww.par.cuepoint = 0
		moviefile_cwww.par.cuepulse.pulse()
		moviefile_cwww.par.play = 1



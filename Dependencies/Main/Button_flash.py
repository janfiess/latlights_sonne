# Buttonflash collective

from TDStoreTools import StorageManager
import TDFunctions as TDF

class Buttonflash:
	def __init__(self, ownerComp):
		return

	# wird von innerhalb der einzelnen Video-Button-Container 
	# und von Play_individual_clip() in op.Clipgun_flash_individual getriggert
	
	def Play(self):
		op.Clipgun_flash.par.Nextplayerid = (op.Clipgun_flash.par.Nextplayerid + 1) % 2
		next_player_id = parent(3).par.Nextplayerid
		clipname = parent().name
		# print(f"clip to play: {clipname}")
		
		op.Clipgun_flash.pars(f"Latestkeypressed{next_player_id}")[0].val = clipname
		

		# print("tetraeder not muted")
	
		moviefile_cwww = op.Clipgun_flash.op(f"moviefilein_cwww_{int(next_player_id)}")
		# print(f"Clipgun_flash: {moviefile_cwww}")
		self.startVideo(moviefile_cwww)
			
		moviefile_rgb = op.Clipgun_flash.op(f"moviefilein_rgb_{int(next_player_id)}")
		# print(f"Clipgun_flash: {moviefile_rgb}")
		self.startVideo(moviefile_rgb)


	
	def startVideo(self, moviefile):
		# print(f"moviefile: {moviefile}")
		moviefile.par.cuepoint = 0
		moviefile.par.cuepulse.pulse()
		moviefile.par.play = 1
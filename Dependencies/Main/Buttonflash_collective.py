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
	
		moviefile_cwww_zone0 = op.Clipgun_flash.op(f"moviefilein_zone0_cwww_{int(next_player_id)}")
		# print(f"moviefile_cwww_zone0: {moviefile_cwww_zone0}")
		self.startVideo(moviefile_cwww_zone0)
			
		moviefile_rgb_zone0 = op.Clipgun_flash.op(f"moviefilein_zone0_rgb_{int(next_player_id)}")
		# print(f"moviefile_rgb_zone0: {moviefile_rgb_zone0}")
		self.startVideo(moviefile_rgb_zone0)


	
	def startVideo(self, moviefile):
		#print(f"moviefile: {moviefile}")
		moviefile.par.cuepoint = 0
		moviefile.par.cuepulse.pulse()
		moviefile.par.play = 1
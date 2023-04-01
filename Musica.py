# Music Player	

import os

print('\n------------------|> 	Phantom Musica <|------------------')

#-------------------------------------------------------------------------------------------------------

def category(streamm): # Function - FOr Filtering the Input as Hollywood or Bollywood...and opening the specified directory

	global music
	global stream

	stream = streamm

	if stream in ['M1','Music 1']:
		stream = 'Music 1'

	if stream in ['M2','Music 2']:
		stream = 'Music 2'

	music = os.listdir('music/' + stream) # Store the songs of the Folder named "Music 1" or "Music 2" in variable 'music'

#------------------------------------------------------------------------------------------------------

# Starting the INTERFACE

stream = input('\nMusic 1  o  Music 2 ?\n\n').lower() # Take Input and save in variable 'stream'

category(stream) # Call function 'category'

print('\n------------------------------------------\n')
print('\n' + stream.upper() + ' MUSIC :\n') # Print the type of Music - 'Music 1 MUSIC' or 'Music 2 MUSIC'

#Print the songs of the Music Folder [We have stored songs list in variable 'music']
for i in range(len(music)):
	print('    ' + (str(i+1) + ') ' + music[i]).replace('.mp3',''))

print('\n------------------------------------------\n')


#-------------- ////////////// I will not explain the Below Stuff. It will be too complex to explain \\\\\\\\\\\\\\\\ -----------------------#

global track
track = 5 #'track' Variable - Universal Access in Program

# Function to play song as the user inputs ----------------------------------------------------------------------------------------------------
def play(track = 0):

	try:

		track_copy = track

		track = input('\nIngresa el numero de cancion : ')

		if track.lower() in ['Music 1','Music 2','M1','M2']:
			category(track.lower())

			print('\n------------------------------------------\n')
			print('\n' + stream.upper() + ' MUSIC :\n')

			for i in range(len(music)):
				print('    ' + (str(i+1) + ') ' + music[i]).replace('.mp3',''))

			print('\n------------------------------------------\n')

			return(track)

		elif track.lower() == 'list':

			print('\n------------------------------------------\n')
			print('\n' + stream.upper() + ' MUSIC :\n')

			for i in range(len(music)):
				print('    ' + (str(i+1) + ') ' + music[i]).replace('.mp3',''))

			print('\n------------------------------------------\n')

			return(track)

		elif track.lower() in ['next','n']:
			track = int(track_copy)+1

		elif track.lower() in ['previous','p']:
			track = int(track_copy)-1


		elif track.lower() in ['exit','stop','cls']:
			print('\n--------------- Saliendo del reproductor ---------------\n')
			return((track))

		track = int(track)

		os.startfile('music\\' + str(stream) + '\\' + str((music[track-1])))

		print('\n    --------------------------------------\n')
		print('  |  Playing ---> ' + music[track-1] + '      |')
		print('\n    --------------------------------------')

		return(str(track))

	except:

		print('\nMessage : Este numero de cancion no existe,intentalo de nuevo!')

		return(str(track))

# -------------------------------------------------------------------------------------------------------------------------------------p

# This WHILE Loop keeps taking input and play songs accordingly.. unless 'exit or stop or cls' is entered!
while True:

	check = play(track)

	track = check

	if check.lower() in ['exit','stop','cls']:
		break
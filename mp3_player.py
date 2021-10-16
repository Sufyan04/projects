from pygame import mixer
mixer.init()
mixer.music.load("Song_name.mp3")
mixer.music.set_volume(0.7)
mixer.music.play()
while True:
    print("enter p for pause , r for resume.")
    print("press s to stop and exit the program")
    query= (input("enter here: "))
    if(query == 'p'):
        mixer.music.pause()
        print("music paused.")
    elif(query == 'r'):
        mixer.music.unpause()
        print("music resumed.")
    elif(query=='s'):
        mixer.music.stop()
        print("music stopped.")
        break
    else:
        print("wrong choice.")
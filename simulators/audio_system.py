from domotic.simulators.audio_video_base import AudioVideoBase

class AudioSystem(AudioVideoBase):
    def __init__(self):
        super().__init__()
        self.key = 'audio_status'
        self.list = {1: 'Music-1', 2: 'Music-2', 3: 'Music-3', 4: 'Music-4', 5: 'Music-5'}
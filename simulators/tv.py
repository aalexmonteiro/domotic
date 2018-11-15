from domotic.simulators.audio_video_base import AudioVideoBase

class TV(AudioVideoBase):
    def __init__(self):
        super().__init__()
        self.key = 'tv_status'
        self.list = {1: 'Channel-1', 2: 'Channel-2', 3: 'Channel-3', 4: 'Channel-4', 5: 'Channel-5'}
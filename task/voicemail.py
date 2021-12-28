class VoicemailAction:
    def __init__(self, voice):
        self.voice = voice
        if not self.voice:
            print(f'no voice instance, exit')
            exit()

    @property
    def voice(self):
        return self._voice

    @voice.setter
    def voice(self, value):
        self._voice = value

    def delete_messages(self, message_criteria):
        pass

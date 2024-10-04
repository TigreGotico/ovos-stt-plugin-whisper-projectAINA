from ovos_plugin_manager.templates.stt import STT
from ovos_stt_plugin_whisper import WhisperSTT


class ProjectAINAWhisperSTT(STT):
    def __init__(self, config=None):
        super().__init__(config)
        model_id = "projecte-aina/whisper-large-v3-ca-3catparla"
        self.config["model"] = model_id
        self.config["lang"] = "ca"
        self.config["ignore_warnings"] = True
        self.stt = WhisperSTT(self.config)

    def execute(self, audio, language=None):
        return self.stt.execute(audio, language)

    @property
    def available_languages(self) -> set:
        return {"ca"}

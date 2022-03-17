import pathlib
from abc import ABC, abstractmethod

class VideoExporter(ABC):
    @abstractmethod
    def prepare_export(self, video_data):
        """Prepares video data for exporting"""


    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Exports video data to a folder"""

class LosslessVideoExporter(VideoExporter):
    def prepare_export(self, video_data):
        print("Preparing video data for lossless export.")
    
    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in lossless format to {folder}.")

class H264BPVideoExporter(VideoExporter):
    def prepare_export(self, video_data):
        print("Preparing video data for H.264 (Baseline) export.")
    
    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H.264 (Baseline) format to {folder}.")
    
class H264Hi422PVideoExporter(VideoExporter):
    def prepare_export(self, video_data):
        print("Preparing video data for H.264 (Hi422P) export.")
    
    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H.264 (Hi422P) format to {folder}.")

class AudioExporter(ABC):
    @abstractmethod
    def prepare_export(self, audio_data):
        """Prepares audio data for exporting"""
    
    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Exports audio data to a folder"""

class AACAudioExporter(AudioExporter):
    def prepare_export(self, audio_data):
        print("Preparing audio data for AAC export.")
    
    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in AAC format to {folder}.")

class WAVAudioExporter(AudioExporter):
    def prepare_export(self, audio_data):
        print("Preparing audio data for WAV export.")
    
    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in WAV format to {folder}.")

class ExporterFactory(ABC):
    #Represents a combination of video and audio codecs, factory does not maintain instances it creates
    def get_video_exporter(self) -> VideoExporter:
        """Returns a new instance of video exporter"""

    def get_audio_exporter(self) -> AudioExporter:
        """Returns a new instance of audio exporter"""

class FastExporter(ExporterFactory):
    def get_video_exporter(self) -> VideoExporter:
        return H264BPVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()
        
class HighQualityExporter(ExporterFactory):
    def get_video_exporter(self) -> VideoExporter:
        return H264Hi422PVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()

class MasterQualityExporter(ExporterFactory):
    def get_video_exporter(self) -> VideoExporter:
        return LosslessVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return WAVAudioExporter()

def read_exporter() -> ExporterFactory:
    #Creates exporter factory based on user preference
    factories = {
        "low": FastExporter(),
        "high": HighQualityExporter(),
        "master": MasterQualityExporter()
    }
    while True:
        export_quality = input("Enter desired output quality (low, high, master): ")
        if export_quality in factories:
            return factories[export_quality]
        print(f"Unknown output quality option: {export_quality}.")

def main(factory: ExporterFactory) -> None:
    video_exporter = factory.get_video_exporter()
    audio_exporter = factory.get_audio_exporter()

    video_exporter.prepare_export("Video Data")
    audio_exporter.prepare_export("Audio Data")

    folder = pathlib.Path("/usr/tmp/video")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)

if __name__ == '__main__':
    factory = read_exporter()
    main(factory)
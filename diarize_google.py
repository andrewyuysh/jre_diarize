# coding: utf-8
from google.cloud import speech_v1p1beta1 as speech
from google.cloud import storage as storage
from google.cloud.speech_v1p1beta1 import types
from google.cloud.speech_v1p1beta1 import enums
gcs_uri = 'gs://jre_episodes/p1219_nointro_snippet_mono.flac'

client = speech.SpeechClient() 

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
    sample_rate_hertz=44100,
    enable_speaker_diarization=True,
    diarization_speaker_count=3,
    language_code='en-US',
    enable_word_time_offsets=True,
    enable_word_confidence=True)

audio = types.RecognitionAudio(uri=gcs_uri)
operation = client.long_running_recognize(config, audio)
response = operation.result()

# Printing out the output:
result = response.results[-1]
words_info = result.alternatives[0].words
for word_info in words_info:
    print("word: '{}', speaker_tag: {}".format(word_info.word, word_info.speaker_tag))
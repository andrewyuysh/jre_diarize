from google.cloud import speech_v1p1beta1 as speech
from google.cloud.speech import enums
from google.cloud.speech import types

gcs_uri = "gs://jre_episodes/p1219_nointro.mp3"

audio = types.RecognitionAudio(uri=gcs_uri)

client = speech.SpeechClient()
config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=16000,
        enable_speaker_diarization=True,
        diarization_speaker_count=3,
        language_code='en-US',
        enable_word_time_offsets=True,
        enable_word_confidence=True)
        
operation = client.long_running_recognize(config, audio)
print('Waiting for operation to complete...')
response = operation.result(timeout=90)






for result in response.results:
    # The first alternative is the most likely one for this portion.
    print(u'Transcript: {}'.format(result.alternatives[0].transcript))
    print('Confidence: {}'.format(result.alternatives[0].confidence))
    
    words_info = result.alternatives[0].words

    # Printing out the output:
    for word_info in words_info:
        print("word: '{}', speaker_tag: {}".format(word_info.word, word_info.speaker_tag))
        
    # alternative = result.alternatives[0]
    # print(u'Transcript: {}'.format(alternative.transcript))
    # print('Confidence: {}'.format(alternative.confidence))

    # for word_info in alternative.words:
        # word = word_info.word
        # start_time = word_info.start_time
        # end_time = word_info.end_time
        # print('Word: {}, start_time: {}, end_time: {}'.format(
            # word,
            # start_time.seconds + start_time.nanos * 1e-9,
            # end_time.seconds + end_time.nanos * 1e-9))
    
    # # word confidence
    # alternative = result.alternatives[0]
    # print('-' * 20)
    # print('First alternative of result {}'.format(i))
    # print(u'Transcript: {}'.format(alternative.transcript))
    # print(u'First Word and Confidence: ({}, {})'.format(
        # alternative.words[0].word, alternative.words[0].confidence))
        
        

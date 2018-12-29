# Joe Rogan Experience (JRE) Speaker Diarization
In a [reddit thread](https://redd.it/26dwif) lamenting the declining quality of JRE podcasts, [/u/lulz](https://www.reddit.com/user/lulz) describes how he judges whether an episode is worth listening to:
>There's a simple test I do on Rogan episodes these days. I skip forward 2 minutes at a time about ten times in a row. If most of the time Joe is talking, it's probably a shit episode.

Thus, the hypothesis: **the quality of a JRE episode is directly correlated to the ratio of the time spoken by Joe Rogan and that of his guest(s)**.

Verdict: TBD

## Methodology
* Download JRE episodes
* Preprocess the episodes
  * Remove irrelevant parts of the episode (including ads & intro song)
  * Transcode to mono FLAC files (if feeding into Google Cloud Speech-to-Text)
* Label some episodes (if not using Google)
* Train the speaker diarization algorithm (if not using Google)
* Use speaker diarization to determine duration spoken by Joe Rogan and guest(s)
* Compare the ratio of the durations to some measure of episode quality
  * YouTube like/dislike ratio
  * iTunes ratings (?)
  * Downloads/views/listens/etc.
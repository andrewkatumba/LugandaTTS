import os

from TTS.config import BaseAudioConfig, BaseDatasetConfig
from TTS.trainer import Trainer, TrainingArgs
from TTS.tts.configs.speedy_speech_config import SpeedySpeechConfig
from TTS.tts.datasets import load_tts_samples
from TTS.tts.models.forward_tts import ForwardTTS
from TTS.utils.audio import AudioProcessor


output_path = "/content/drive/MyDrive/Emergent/train/Day19"
dataset_config = BaseDatasetConfig(
    name="ljspeech", meta_file_train="metadata.csv", path="/content/data/"
)

audio_config = BaseAudioConfig(
    sample_rate=22050,
    do_trim_silence=True,
    trim_db=60.0,
    signal_norm=False,
    mel_fmin=0.0,
    mel_fmax=8000,
    spec_gain=1.0,
    log_func="np.log",
    ref_level_db=20,
    preemphasis=0.98,
)

config = SpeedySpeechConfig(
    run_name="speedy_speech_ljspeech",
    audio=audio_config,
    batch_size=16,
    eval_batch_size=16,
    num_loader_workers=4,
    num_eval_loader_workers=4,
    compute_input_seq_cache=True,
    run_eval=True,
    test_delay_epochs=100,
    epochs=1000,
    text_cleaner="english_cleaners",
    use_phonemes=False,
    use_espeak_phonemes=False,
    phoneme_language="en-us",
    phoneme_cache_path=os.path.join(output_path, "phoneme_cache"),
    print_step=50,
    print_eval=False,
    mixed_precision=False,
    sort_by_audio_len=True,
    min_seq_len=0,
    max_seq_len=500000.0,
    output_path=output_path,
    datasets=[dataset_config],
)

# # compute alignments
if not config.model_args.use_aligner:
  manager = ModelManager()
  model_path, config_path, _ = manager.download_model("/content/drive/MyDrive/Emergent/train/Day15_24dB/coqui_tts-December-22-2021_07+06PM-7f1a2378")
  # TODO: make compute_attention python callable
  os.system(
    f"python TTS/bin/compute_attention_masks.py --model_path {model_path} --config_path {config_path} --dataset ljspeech --dataset_metafile metadata.csv --data_path /content/data  --use_cuda true"
  )

# init audio processor
ap = AudioProcessor(**config.audio.to_dict())

# load training samples
train_samples, eval_samples = load_tts_samples(dataset_config, eval_split=True)

# init model
model = ForwardTTS(config)

# init the trainer and 🚀
trainer = Trainer(
    TrainingArgs(),
    config,
    output_path,
    model=model,
    train_samples=train_samples,
    eval_samples=eval_samples,
    training_assets={"audio_processor": ap},
)
trainer.fit()

import os

from TTS.config.shared_configs import BaseAudioConfig
from TTS.trainer import Trainer, TrainingArgs
from TTS.tts.configs.shared_configs import BaseDatasetConfig
from TTS.tts.configs.vits_config import VitsConfig
from TTS.tts.datasets import load_tts_samples
from TTS.tts.models.vits import Vits, VitsArgs
from TTS.utils.audio import AudioProcessor

output_path = "/content/drive/MyDrive/Emergent/train/Day23/"
# init configs
dataset_config = BaseDatasetConfig(
    name="ljspeech", meta_file_train="metadata.csv", path="/content/data/"
)

audio_config = BaseAudioConfig(
    sample_rate=44100,
    fft_size= 2048,
    win_length=2048,
    hop_length=512,
    num_mels=80,
    preemphasis=0.98,
    ref_level_db=20,
    log_func="np.log",
    do_trim_silence=True,
    trim_db=45,
    mel_fmin=0,
    mel_fmax=None,
    spec_gain=1.0,
    signal_norm=False,
    do_amp_to_db_linear=False,
)

vitsArgs = VitsArgs(
    upsample_rates_decoder=[8,8,2,2,2],
    upsample_kernel_sizes_decoder=[16,16,4,4,4],
    out_channels = 1025,
)

config = VitsConfig(
    model_args=vitsArgs,
    audio=audio_config,
    run_name="44k_vits_train",
    batch_size=32,
    eval_batch_size=16,
    batch_group_size=5,
    num_loader_workers=4,
    num_eval_loader_workers=4,
    run_eval=True,
    test_delay_epochs=-1,
    epochs=10000,
    text_cleaner="basic_cleaners",
    use_phonemes=False,
    phoneme_language="en-us",
    phoneme_cache_path="/content/drive/MyDrive/Emergent/train/Day11_newData/phoneme_cache",
    compute_input_seq_cache=True,
    print_step=25,
    print_eval=True,
    mixed_precision=False,
    save_step=1000,
    characters={
        "pad": "_",
        "eos": "~",
        "bos": "^",
        "characters": "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzŋ!'(),-.:;? ",
        "punctuations": "!'(),-.:;? ",
        "phonemes": "iy\u0268\u0289\u026fu\u026a\u028f\u028ae\u00f8\u0258\u0259\u0275\u0264o\u025b\u0153\u025c\u025e\u028c\u0254\u00e6\u0250a\u0276\u0251\u0252\u1d7b\u0298\u0253\u01c0\u0257\u01c3\u0284\u01c2\u0260\u01c1\u029bpbtd\u0288\u0256c\u025fk\u0261q\u0262\u0294\u0274\u014b\u0272\u0273n\u0271m\u0299r\u0280\u2c71\u027e\u027d\u0278\u03b2fv\u03b8\u00f0sz\u0283\u0292\u0282\u0290\u00e7\u029dx\u0263\u03c7\u0281\u0127\u0295h\u0266\u026c\u026e\u028b\u0279\u027bj\u0270l\u026d\u028e\u029f\u02c8\u02cc\u02d0\u02d1\u028dw\u0265\u029c\u02a2\u02a1\u0255\u0291\u027a\u0267\u02b2\u025a\u02de\u026b",
        "unique": True
    },
    test_sentences=[
        ["Abaaliwo bonna baasooka ne basiriikirira nga beewuunya omulanga oguvudde mu musajja ayogereza mwannyinaabwe."],
        ["Wuuno eyakubye bbomu mu bbaasi."],
        ["Engeri omupangisa gy’atutte omugagga nabukeera mu kkomera."],
        ["Pulezidenti awadde ekiragiro ku takisi."],
        ["Aba bodaboda abasse ow’emmotoka babalina."]
    ],
    min_seq_len=10000,
    max_seq_len=500000,
    output_path=output_path,
    datasets=[dataset_config],
)

# init audio processor
ap = AudioProcessor(**config.audio.to_dict())

# load training samples
train_samples, eval_samples = load_tts_samples(dataset_config, eval_split=True)

# init model
model = Vits(config)

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

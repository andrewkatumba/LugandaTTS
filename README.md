# LugandaTTS
TTS model for Luganda

## Phases

- Data Collection
- Data Validation
- Model Training

### Data Collection
Below are the 2 tracks that can be used for collecting data
#### Using defined Luganda text corpus
In this track, we work from text to speech collection, first we have to obtain a rich Luganda text corpus that we can use. 
##### Pre-Data Collection
Before we collect our data, we have to identify which sites to attain it from, the protocols needed.This is to be done with a Luganda linguist to advise on language topology and fieldwork and best corpus building methods.
##### Corpus building
With the attained  corpus, the rules below have to be doublechecked to get the best results in our model.Identify the text and break it down into one sentence per line in either `.tsv` or `.csv` file formats.
##### Guidelines for Luganda sentences to be read out loud
- Compute grapheme and phoneme coverage of the resulting sentences to ensure most sounds are covered
- Compile into `.tsv/.csv` files in a sentence per line
- “Clean” text to exclude numbers, integers or abbreviations just as in the LJ speech dataset and label this as normalized text.
- Check the License of where the data was attained if we plan to release the dataset & make one for our data.  
- Ensure canonical(most basic form) sentences.

Once a rich corpus is attained and validated with the above guidelines,it is ready to be read out by an orator.Below are guidelines for a narrator.
##### Guidelines for the individual recording audio
- Record in intervals of 30 minutes the take breaks.
- Have a maximum recording time of 4 hours a day to avoid burnout
- Rerecord sentence if 
    - There is noticeable noise in the background(always use same location) , make an anechoic studio
    - A pronunciation problem(shuttering, laughing)
    - Speaker finds prosody unnatural (Read neutral but “natural”)
- Use a good microphone
- Always keep same distance between mouth and microphone
- No random noise (computer fans, air conditioning, …)
- Do not swallow up letters
- Adjust tone and pitch with different punctuations
- Use constant recording speed and volume
- Start with sentences in average length (not just one/two words)
- If you can hear it (eg. barking dog outside), the mic can hear it too”
- Do not record when having a cold or voice is not optimal
- Read mistake free. If unsure record phrase again
- Use a good microphone
- Keep the angle at which the microphone is pointed to the speaker as constant as possible record the date and time of recording


#### Using pre-recorded audio 


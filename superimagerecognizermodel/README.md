## Steps for user (No! I am not giving you a model, you have to generate it yourself!)
* Use ollama to download your own desired image recognizing models (hint: start with gemma3, and go on from there)
* Use OllamaToGGUF to convert those models to accessible GGUF files
* Copy (or preferably if possible, as a measure to save space symolically link the gguf files into this folder)
* Create a ModelFile With something similar to following (You may use different models of your choosing, but make sure the FROM Model knows how to talk):
```
FROM gemma3-27.4B-Q4_K_M.gguf # Good baseline model to use from Google (gemma3:27b from Ollama reassembled)
ADAPTER llava-34B-Q4_0.gguf
ADAPTER mistral-small3.2-24.0B-Q4_K_M.gguf
ADAPTER minicpm-v-7.6B-Q4_0.gguf
ADAPTER Moondream-1B-Q4_0.gguf
```
* Run the following `ollama create superimagerecognizermodel` while you are in the superimagerecognizermodel directory

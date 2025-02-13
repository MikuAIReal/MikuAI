import ollama
import websockets
import json
import numpy as np
import sounddevice as sd
from transformers import pipeline
from scipy.io.wavfile import write
import librosa
import threading

# Initialize components
emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

class VTubeController:
    def __init__(self):
        self.ws_connection = None
        self.current_audio = None
        
    async def connect(self):
        self.ws_connection = await websockets.connect("ws://localhost:8001")
        
    async def send_parameters(self, params):
        await self.ws_connection.send(json.dumps({
            "apiName": "InjectParameterDataRequest",
            "data": {
                "parameters": [
                    {"id": "MouthOpen", "value": params.get("mouth_open", 0.5)},
                    {"id": "VoiceA", "value": params.get("A", 0)},
                    {"id": "VoiceI", "value": params.get("I", 0)},
                    {"id": "MouthSmile", "value": params.get("smile", 0.5)}
                ]
            }
        }))

class MikuVoice:
    def __init__(self):
        self.sample_rate = 22050
        self.vowel_threshold = 0.3
        
    def generate_audio(self, text):
        """Replace with actual Miku TTS API call"""
        # Placeholder: Generate test tone with varying vowels
        duration = 1.0
        t = np.linspace(0, duration, int(self.sample_rate * duration))
        audio = np.sin(2 * np.pi * 440 * t)  # Basic sine wave
        return audio.astype(np.float32)
        
    def analyze_audio(self, audio):
        """Extract lip sync parameters from audio"""
        # Get volume-based mouth openness
        rms = librosa.feature.rms(y=audio)[0]
        mouth_open = np.mean(rms) * 2
        
        # Simple vowel detection (replace with proper phoneme analysis)
        spectral_centroid = librosa.feature.spectral_centroid(y=audio, sr=self.sample_rate)[0]
        A = 1 if np.mean(spectral_centroid) > 2000 else 0
        I = 1 if 1500 < np.mean(spectral_centroid) < 2500 else 0
        
        return {"mouth_open": float(mouth_open), "A": A, "I": I}

async def main_flow(user_input):
    vtube = VTubeController()
    voice = MikuVoice()
    await vtube.connect()
    
    # Generate LLM response
    system_prompt = "You are Hatsune Miku. Respond in English but use Japanese cute suffixes like ~nya! Keep responses short."
    response = ollama.generate(
        model='deepseek-r1:1.5b',
        prompt=user_input,
        system=system_prompt,
        options={'temperature': 0.7}
    )
    text_response = response['choices'][0]['text'].strip()
    
    # Generate voice audio
    audio = voice.generate_audio(text_response)
    
    # Real-time lip sync
    def audio_callback():
        chunk_size = 1024
        for i in range(0, len(audio), chunk_size):
            chunk = audio[i:i+chunk_size]
            params = voice.analyze_audio(chunk)
            
            # Add emotion-based parameters
            emotion = emotion_classifier(text_response)[0]['label'].lower()
            params["smile"] = 0.9 if emotion == "joy" else 0.5
            
            # Send to VTube Studio
            asyncio.run_coroutine_threadsafe(vtube.send_parameters(params), loop)
            
            # Play audio
            if len(chunk) > 0:
                sd.play(chunk, voice.sample_rate)
                sd.wait()
    
    # Start audio/lip sync thread
    loop = asyncio.get_event_loop()
    threading.Thread(target=audio_callback).start()
    
    return text_response

# Run example
async def run_example():
    response = await main_flow("What's your favorite food?")
    print(f"Miku: {response}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(run_example())

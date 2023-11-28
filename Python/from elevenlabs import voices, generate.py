from elevenlabs import play, generate, clone, set_api_key
import cwd
from gtts import GTTS as gt

cwd.cwd(".mp3")
set_api_key("6d9e54011df457f0cb1135e1fb4240c7")

# voice = clone(name = "Sofia",
#                description = " a young german female voice with russian qualities",
#                files = ["./sofia_voice_recording.wav"])
 
# audio = generate(text="Mihail, du bist der beste!", voice = voice)

# play(audio)
 
# print("Hahuhuhagagagaga")

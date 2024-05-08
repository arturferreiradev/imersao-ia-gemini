"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

from pathlib import Path
import hashlib
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 0.95,
  "top_k": 32,
  "max_output_tokens": 1024,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro-vision-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

uploaded_files = []
def upload_if_needed(pathname: str) -> list[str]:
  path = Path(pathname)
  hash_id = hashlib.sha256(path.read_bytes()).hexdigest()
  try:
    existing_file = genai.get_file(name=hash_id)
    return [existing_file]
  except:
    pass
  uploaded_files.append(genai.upload_file(path=path, display_name=hash_id))
  return [uploaded_files[-1]]

prompt_parts = [
  "What object is this? Describe how it might be used",
  "Object: ",
  *upload_if_needed("assets/image0.jpeg"),
  "Description: This is a pipe organ. It is a large musical instrument that is used in churches, concert halls, and other large buildings. It is made up of a series of pipes that are arranged in different sizes and shapes. The pipes are played by pressing keys on a keyboard. When a key is pressed, air is forced through the pipe, which produces a sound. The sound of a pipe organ is very powerful and can be used to create a wide variety of music.",
  "Object: ",
  *upload_if_needed("assets/image1.jpeg"),
  "Description: This is a sundial. It is a device that uses the sun's position in the sky to tell the time. The sundial has a flat surface with a hole in the center. A metal rod is placed through the hole and is pointed at the North Star. The shadow of the rod falls on the flat surface and indicates the time.",
  "Object: ",
  *upload_if_needed("assets/image2.jpeg"),
  "Description: ",
]

response = model.generate_content(prompt_parts)
print(response.text)
for uploaded_file in uploaded_files:
  genai.delete_file(name=uploaded_file.name)

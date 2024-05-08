"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

# Set up the model
generation_config = {
  "temperature": 2,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
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

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

prompt_parts = [
  "Write a character design in a pirate-themed game set in the Joseon era.",
  "input: Main Character (Female)",
  "output: **Name:** Haenyeo\n\n**Appearance:**\n\n* **Age:** Mid-twenties\n* **Height:** 5'7\"\n* **Weight:** 130 lbs\n* **Build:** Athletic and agile\n* **Hair:** Long, black hair worn in a practical braid\n* **Eyes:** Piercing hazel eyes that reflect the sea's depths\n* **Clothing:**\n    * Loose, dark-colored pants tucked into sturdy leather boots\n    * A lightweight cotton shirt with a low neckline, trimmed with intricate embroidery\n    * A leather vest with multiple pockets for tools and supplies\n* **Accessories:**\n    * A broad-brimmed hat to shield her face from the sun\n    * A pair of silver earrings in the shape of anchors\n    * A leather belt with a small pouch for valuables\n\n**Personality:**\n\n* **Determined:** Haenyeo is a fearless and tenacious pirate, driven by a strong sense of justice and a desire for adventure.\n* **Resourceful:** Her time spent as a haenyeo (Korean female diver) has honed her survival instincts and adaptability.\n* **Empathetic:** Despite her pirate lifestyle, Haenyeo has a compassionate heart and a soft spot for those in need.\n* **Intelligent:** She is quick-witted and observant, able to assess situations and make decisions swiftly.\n* **Independent:** Haenyeo values her freedom and relies on her own abilities rather than seeking help from others.\n\n**Skills:**\n\n* **Diving:** Haenyeo is an expert diver, capable of holding her breath for extended periods and navigating underwater with ease.\n* **Swimming:** Her exceptional swimming abilities allow her to navigate the treacherous ocean currents and avoid danger.\n* **Spearfishing:** She is a skilled spearfisher, using her knowledge of marine life to locate and catch prey underwater.\n* **Seamanship:** As a pirate, Haenyeo is familiar with the basics of sailing and ship navigation.\n* **Hand-to-Hand Combat:** While not an expert fighter, she is proficient in basic self-defense techniques, using her agility and knowledge of pressure points to subdue opponents.\n\n**Background:**\n\nHaenyeo was raised on a coastal village and learned the ways of the haenyeo from a young age. However, when her village was attacked by bandits, she witnessed firsthand the brutality of war and decided to fight back.\n\nJoining a pirate crew, Haenyeo has proven herself as a valuable member, using her diving skills to scout for enemy ships and gather underwater resources. Her determination and compassion have also earned her the respect of her crewmates.",
  "input: Main Character (Male)",
  "output: ",
]

response = model.generate_content(prompt_parts)
print(response.text)

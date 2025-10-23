# 🎶 Trending Py Lyrics Generator

A fun and colorful trending Python project that types out any specific given song lyrics in **neon-style animated text** right in your terminal!  

## Features

- Neon colored text that cycles smoothly line by line  
- Custom typing speed and delay for each lyric  
- Modular design – you can easily change the song or add your own  
- Simple two-file structure (`main.py` + `lyrics.py`)

## Project Structure

Trending-Lyrics-Generator/


├── main.py # Core script that handles display and animation

├── lyrics.py # Song data (name, lyrics, speed/delay)

└── requirements.txt

## Getting Started

### 1️⃣ Clone the Repository

    ```bash     
    git clone https://github.com/<your-username>/Trending-Lyrics-Generator.git
    cd Trending-Lyrics-Generator
    
### 2️⃣ Install Requirements

    ```bash
    pip install -r requirements.txt

### 3️⃣ Run the Program

    ```bash
    pip run Main.py

### Customize Your Own Lyrics   

Open lyrics.py and replace the contents with your favorite song’s lyrics:

Song_Name = "Your Song Title"

lyrics = {'line': "First line...", 'typing_speed': 0.1, 'delay_after': 0.5},
    {'line': "Next line...", 'typing_speed': 0.08, 'delay_after': 0.6}
]

    

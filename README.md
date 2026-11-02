# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works
Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.


Real-world recommendation systems use content-based filtering and collaborative filtering. They also use signals such as plays, skips, likes, and saves to better determin how people in general like the song and how the user themself  enjoys it(ie, if they skip or replay it a lot). This project will compare each song's attributes with a user's stated preferences, score each song, and rank songs by that score. `Song` uses `id`, `title`, `artist`, `genre`, `mood`, `energy`, `tempo_bpm`, `valence`, `danceability`, and `acousticness`. with each thing a number, we can just compare the numbers.
'UserProfile` stores `favorite_genre`, `favorite_mood`, `target_energy`, and `likes_acoustic`. These preferences are once again just numbers we can compare to other numbers.
The recommender scores candidate songs against the user's preferences and ranks them, returning the highest-scoring songs.

Algorythm Stuff------------

For each song, the recommender will calculate a score using the user's preferred genre, preferred mood, and target energy. A genre match is 2 points, a mood match is 1 point, and an energy rating goes up to 2 points. Said points are calculated with: 2.0 x 1(-song energy - target energy). The recommender will add these for each song, sort them, and then return the top 3. Should songs tie energy ratings are the tiebreaker. There is a bias, genre can have more influence since its worth twice as much. The recommender will add these points for each song, sort songs from highest to lowest score, and return the top three. If songs tie, the song with energy closest to the user's target will rank higher.




## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

aded songs: 17

Top recommendations for genre='pop', mood='happy':
================================================
1. Sunrise City - Neon Echo
   Score: 4.96
   Reasons:
   - genre match (+2.0)
   - mood match (+1.0)
   - energy similarity (+1.96)

2. Gym Hero - Max Pulse
   Score: 3.74
   Reasons:
   - genre match (+2.0)
   - energy similarity (+1.74)

3. Rooftop Lights - Indigo Parade
   Score: 2.92
   Reasons:
   - mood match (+1.0)
   - energy similarity (+1.92)

4. Night Drive Loop - Neon Echo
   Score: 1.90
   Reasons:
   - energy similarity (+1.90)

5. Level Up - Northside Verse
   Score: 1.88
   Reasons:
   - energy similarity (+1.88)

---

## System Evaluation: Profile Recommendations

The following are the terminal results for the three representative profiles and five edge-case profiles. The edge cases test conflicting mood and energy preferences, an out-of-range energy target, missing preferences, the lower energy boundary, and precedence between preference-key aliases.

### High-Energy Pop

```text
Top recommendations for profile: High-Energy Pop
Preferences: {'genre': 'pop', 'mood': 'happy', 'energy': 0.9}
================================================
1. Sunrise City - Neon Echo
   Score: 4.84
   Reasons:
   - genre match (+2.0)
   - mood match (+1.0)
   - energy similarity (+1.84)

2. Gym Hero - Max Pulse
   Score: 3.94
   Reasons:
   - genre match (+2.0)
   - energy similarity (+1.94)

3. Rooftop Lights - Indigo Parade
   Score: 2.72
   Reasons:
   - mood match (+1.0)
   - energy similarity (+1.72)

4. Storm Runner - Voltline
   Score: 1.98
   Reasons:
   - energy similarity (+1.98)

5. Afterglow Signal - Club Meridian
   Score: 1.98
   Reasons:
   - energy similarity (+1.98)
```

### Chill Lofi

```text
Top recommendations for profile: Chill Lofi
Preferences: {'genre': 'lofi', 'mood': 'chill', 'energy': 0.4}
================================================
1. Midnight Coding - LoRoom
   Score: 4.96
   Reasons:
   - genre match (+2.0)
   - mood match (+1.0)
   - energy similarity (+1.96)

2. Library Rain - Paper Lanterns
   Score: 4.90
   Reasons:
   - genre match (+2.0)
   - mood match (+1.0)
   - energy similarity (+1.90)

3. Focus Flow - LoRoom
   Score: 4.00
   Reasons:
   - genre match (+2.0)
   - energy similarity (+2.00)

4. Spacewalk Thoughts - Orbit Bloom
   Score: 2.76
   Reasons:
   - mood match (+1.0)
   - energy similarity (+1.76)

5. Coffee Shop Stories - Slow Stereo
   Score: 1.94
   Reasons:
   - energy similarity (+1.94)
```

### Deep Intense Rock

```text
Top recommendations for profile: Deep Intense Rock
Preferences: {'genre': 'rock', 'mood': 'intense', 'energy': 0.95}
================================================
1. Storm Runner - Voltline
   Score: 4.92
   Reasons:
   - genre match (+2.0)
   - mood match (+1.0)
   - energy similarity (+1.92)

2. Gym Hero - Max Pulse
   Score: 2.96
   Reasons:
   - mood match (+1.0)
   - energy similarity (+1.96)

3. Afterglow Signal - Club Meridian
   Score: 1.88
   Reasons:
   - energy similarity (+1.88)

4. Level Up - Northside Verse
   Score: 1.82
   Reasons:
   - energy similarity (+1.82)

5. Sunrise City - Neon Echo
   Score: 1.74
   Reasons:
   - energy similarity (+1.74)
```

### High Energy, Sad Mood (Conflicting)

```text
Top recommendations for profile: High Energy, Sad Mood (conflicting)
Preferences: {'genre': 'pop', 'mood': 'sad', 'energy': 0.95}
================================================
1. Gym Hero - Max Pulse
   Score: 3.96
   Reasons:
   - genre match (+2.0)
   - energy similarity (+1.96)

2. Sunrise City - Neon Echo
   Score: 3.74
   Reasons:
   - genre match (+2.0)
   - energy similarity (+1.74)

3. Blue Hour Train - Harbor Street Blues
   Score: 2.02
   Reasons:
   - mood match (+1.0)
   - energy similarity (+1.02)

4. Storm Runner - Voltline
   Score: 1.92
   Reasons:
   - energy similarity (+1.92)

5. Afterglow Signal - Club Meridian
   Score: 1.88
   Reasons:
   - energy similarity (+1.88)
```

### Out-of-Range Energy

```text
Top recommendations for profile: Out-of-Range Energy
Preferences: {'favorite_genre': 'classical', 'target_energy': 2.0}
================================================
1. Glass Cathedral - Elian Voss
   Score: 0.48
   Reasons:
   - genre match (+2.0)
   - energy similarity (+-1.52)

2. Gym Hero - Max Pulse
   Score: -0.14
   Reasons:
   - energy similarity (+-0.14)

3. Storm Runner - Voltline
   Score: -0.18
   Reasons:
   - energy similarity (+-0.18)

4. Afterglow Signal - Club Meridian
   Score: -0.22
   Reasons:
   - energy similarity (+-0.22)

5. Level Up - Northside Verse
   Score: -0.28
   Reasons:
   - energy similarity (+-0.28)
```

### No Preferences

```text
Top recommendations for profile: No Preferences (edge case)
Preferences: {}
================================================
1. Sunrise City - Neon Echo
   Score: 0.00
   Reasons:
   - No matching preferences

2. Midnight Coding - LoRoom
   Score: 0.00
   Reasons:
   - No matching preferences

3. Storm Runner - Voltline
   Score: 0.00
   Reasons:
   - No matching preferences

4. Library Rain - Paper Lanterns
   Score: 0.00
   Reasons:
   - No matching preferences

5. Gym Hero - Max Pulse
   Score: 0.00
   Reasons:
   - No matching preferences
```

### Minimum Energy Boundary

```text
Top recommendations for profile: Minimum Energy Boundary
Preferences: {'energy': 0.0}
================================================
1. Glass Cathedral - Elian Voss
   Score: 1.52
   Reasons:
   - energy similarity (+1.52)

2. Spacewalk Thoughts - Orbit Bloom
   Score: 1.44
   Reasons:
   - energy similarity (+1.44)

3. Library Rain - Paper Lanterns
   Score: 1.30
   Reasons:
   - energy similarity (+1.30)

4. Coffee Shop Stories - Slow Stereo
   Score: 1.26
   Reasons:
   - energy similarity (+1.26)

5. Focus Flow - LoRoom
   Score: 1.20
   Reasons:
   - energy similarity (+1.20)
```

### Conflicting Key Aliases

```text
Top recommendations for profile: Conflicting Key Aliases
Preferences: {'genre': 'pop', 'favorite_genre': 'classical', 'mood': 'happy', 'favorite_mood': 'sad', 'energy': 0.1, 'target_energy': 0.9}
================================================
1. Sunrise City - Neon Echo
   Score: 3.56
   Reasons:
   - genre match (+2.0)
   - mood match (+1.0)
   - energy similarity (+0.56)

2. Gym Hero - Max Pulse
   Score: 2.34
   Reasons:
   - genre match (+2.0)
   - energy similarity (+0.34)

3. Glass Cathedral - Elian Voss
   Score: 1.72
   Reasons:
   - energy similarity (+1.72)

4. Rooftop Lights - Indigo Parade
   Score: 1.68
   Reasons:
   - mood match (+1.0)
   - energy similarity (+0.68)

5. Spacewalk Thoughts - Orbit Bloom
   Score: 1.64
   Reasons:
   - energy similarity (+1.64)
```

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


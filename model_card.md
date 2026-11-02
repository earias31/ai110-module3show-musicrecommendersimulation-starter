# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  
VibeMaster 1.0
---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

It generates recomendations and assumes a rough estimate of a persons likes thorugh the data provided. Its mainly for a classroom.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

The model compares a user's preferred genre, mood, and energy level with each song's genre, mood, and energy. A matching genre adds 2 points, a matching mood adds 1 point, and songs with energy closer to the user's target earn more energy points. It ranks songs from highest score to lowest and explains which preferences contributed to each score. Compared with the starter example, it now runs several different profiles, including conflicting preferences and edge cases.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The catalog contains 17 songs across 14 genres, including pop, lofi, rock, jazz, country, classical, and hip-hop, with moods such as happy, chill, intense, sad, and relaxed. I added seven songs to the original ten-song dataset. This small, fictional catalog cannot represent every genre, mood, artist, or factor that shapes musical taste.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

The recommender works well when users have clear genre, mood, and energy preferences that match songs in the catalog. For example, a high-energy pop profile should rank energetic pop songs highly, while a chill lofi profile should favor calmer lofi songs. These results feel intuitive because matching genre and mood earns points, and energy closer to the user's target is rewarded.
---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

The scoring formula assumes energy preferences are between 0 and 1, but it does not validate them. In the out-of-range energy experiment, a target of 2.0 gave songs negative energy-similarity points. Genre matches add twice as many points as mood matches, so a genre match can outweigh a mood preference that conflicts with it, as in the high-energy/sad profile. The recommender also ranks only by score and preserves catalog order when scores tie, so users with no preferences receive the same catalog-first results rather than personalized or diverse recommendations.

---

## 7. Evaluation  

I tested High-Energy Pop, Chill Lofi, and Deep Intense Rock, plus five edge cases: High Energy, Sad Mood; Out-of-Range Energy; No Preferences; Minimum Energy Boundary; and Conflicting Key Aliases. I compared their top-five lists and the score explanations. The biggest surprise was that Gym Hero appears for a happy-pop listener even though its mood is “intense”: it earns two points for matching pop and nearly two more for its high energy, enough to rank above songs without the pop match. This shows that the system follows its point weights consistently, but a genre-and-energy match can matter more than a listener's mood.

Each row below compares one pair of tested profiles. It describes what changed in their results and why that change follows from the preferences and scoring.

| Profile pair | What changed and why |
|---|---|
| High-Energy Pop / Chill Lofi | The lists do not overlap: pop favors Sunrise City and Gym Hero, while lofi favors Midnight Coding and Library Rain. The genre, mood, and energy preferences all point to different songs. |
| High-Energy Pop / Deep Intense Rock | Both include Gym Hero, Sunrise City, and Afterglow Signal, but pop puts Sunrise City first while rock puts Storm Runner first. Rock and intense matches lift Storm Runner; pop and happy matches lift Sunrise City. |
| High-Energy Pop / High Energy, Sad Mood | Gym Hero and Sunrise City stay near the top, while sad Blue Hour Train enters at number three. The pop preference and high energy still outweigh the single sad-mood point. |
| High-Energy Pop / Out-of-Range Energy | Gym Hero, Storm Runner, and Afterglow Signal appear in both lists, but the out-of-range profile ranks classical Glass Cathedral first and gives negative energy points. Its target of 2.0 is beyond the songs' 0–1 scale. |
| High-Energy Pop / No Preferences | Both lists include Sunrise City and Gym Hero, but the no-preferences list is just the catalog order because every song ties at zero. Those shared songs are not personalized matches in that list. |
| High-Energy Pop / Minimum Energy Boundary | Their top-five lists have no songs in common: high energy favors energetic tracks, while an energy target of 0.0 favors the quietest tracks, such as Glass Cathedral. |
| High-Energy Pop / Conflicting Key Aliases | Both include Sunrise City and Gym Hero, but the alias profile also promotes low-energy Glass Cathedral. When both key names are provided, the shorter `genre`, `mood`, and `energy` keys take precedence over their aliases. |
| Chill Lofi / Deep Intense Rock | Their top-five lists do not overlap. Lofi and chill preferences favor mellow lofi songs; rock and intense preferences favor Storm Runner and Gym Hero. |
| Chill Lofi / High Energy, Sad Mood | Their top-five lists do not overlap. The conflicting profile rewards pop and high energy and includes the only sad song, while the lofi profile rewards lofi and chill. |
| Chill Lofi / Out-of-Range Energy | There is no overlap in the top five. The out-of-range target yields negative energy points and the classical bonus puts Glass Cathedral first, unlike the lofi and chill matches. |
| Chill Lofi / No Preferences | Midnight Coding and Library Rain appear in both, but the no-preferences list follows catalog order and gives them no points. The lofi profile ranks them highly for their actual genre, mood, and energy matches. |
| Chill Lofi / Minimum Energy Boundary | Library Rain, Spacewalk Thoughts, Coffee Shop Stories, and Focus Flow appear in both. Their relatively low energy suits the boundary profile, and several also match the lofi profile's calm sound or genre. |
| Chill Lofi / Conflicting Key Aliases | The lists share Spacewalk Thoughts, but the alias profile instead favors pop/happy songs and Glass Cathedral. Its explicit `genre`, `mood`, and `energy` values override the conflicting aliases. |
| Deep Intense Rock / High Energy, Sad Mood | Storm Runner, Gym Hero, Afterglow Signal, and Sunrise City appear in both, but rock puts Storm Runner first and the conflicting profile puts Gym Hero first. Rock/intense matches favor Storm Runner; pop plus high energy favors Gym Hero. |
| Deep Intense Rock / Out-of-Range Energy | Gym Hero, Storm Runner, Afterglow Signal, and Level Up appear in both. The rock profile rewards rock and intense, while the out-of-range profile's target of 2.0 produces negative energy scores and a classical genre bonus. |
| Deep Intense Rock / No Preferences | Storm Runner, Gym Hero, and Sunrise City appear in both, but the no-preferences results are simply the first songs in the catalog. The rock profile ranks by rock/intense matches and high energy. |
| Deep Intense Rock / Minimum Energy Boundary | Their top-five lists do not overlap. The rock profile wants high energy and intensity, while the boundary profile favors the least energetic songs. |
| Deep Intense Rock / Conflicting Key Aliases | Gym Hero and Sunrise City appear in both, but the alias profile promotes pop and happy while the rock profile puts rock/intense Storm Runner first. The conflicting profile uses its explicit `genre`, `mood`, and `energy` keys. |
| High Energy, Sad Mood / Out-of-Range Energy | Both include Gym Hero, Storm Runner, and Afterglow Signal, but the conflicting profile also ranks sad Blue Hour Train, while the out-of-range profile ranks classical Glass Cathedral first. Mood/genre matches and the very different energy targets explain the change. |
| High Energy, Sad Mood / No Preferences | Gym Hero, Sunrise City, and Storm Runner appear in both, but the no-preferences list is catalog order with tied zero scores. The conflicting profile's high-energy and pop preferences give its results meaningful scores. |
| High Energy, Sad Mood / Minimum Energy Boundary | There is no overlap in the top five: a 0.95 target favors high-energy songs, while 0.0 favors the quietest songs. |
| High Energy, Sad Mood / Conflicting Key Aliases | Gym Hero and Sunrise City appear in both, but the alias profile also ranks Glass Cathedral and Rooftop Lights. Its lower energy target and happy mood differ from the high-energy/sad profile; explicit keys override aliases. |
| Out-of-Range Energy / No Preferences | Gym Hero and Storm Runner appear in both, but the no-preferences list keeps catalog order while the out-of-range list sorts by energy scores that are negative for every song. The classical match gives Glass Cathedral extra points. |
| Out-of-Range Energy / Minimum Energy Boundary | Both include Glass Cathedral, but the out-of-range profile also promotes high-energy Gym Hero and Storm Runner, whereas the 0.0 profile favors low-energy Spacewalk Thoughts and Library Rain. Glass Cathedral stays high for the out-of-range profile because it matches classical. |
| Out-of-Range Energy / Conflicting Key Aliases | Both include Glass Cathedral and Gym Hero, but the out-of-range profile rewards classical while the alias profile rewards pop and happy. Their energy targets (2.0 and 0.1) also pull the other results in different directions. |
| No Preferences / Minimum Energy Boundary | Library Rain appears in both, but no preferences simply returns catalog order while the boundary profile ranks by closeness to zero energy. The overlap is not evidence that the baseline list is personalized. |
| No Preferences / Conflicting Key Aliases | Sunrise City and Gym Hero appear in both, but they are early in the catalog for the no-preferences profile and earn pop/happy points for the alias profile. The alias profile's explicit keys take precedence over the conflicting values. |
| Minimum Energy Boundary / Conflicting Key Aliases | Glass Cathedral and Spacewalk Thoughts appear in both, but the alias profile also boosts pop/happy songs. Its explicit energy value of 0.1 still favors calmer tracks, while the genre and mood points change the ranking. |

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

I think just enhancing everything is best for future work. Make it less numbers based and more general feel of the song based on user recomendation.
---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

It said or the read me, so im doing this here.

I learned a lot about how youtube music recomends my songs. It really was interseting working with the Ai to come up with some way to do it ourselves.
It has changed the way I see recomendations. In the end I'm just some numbers so that an ai can give me other numbers to imrpove the number of users.
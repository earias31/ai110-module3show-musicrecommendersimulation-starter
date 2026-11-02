import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


TASTE_PROFILE: Dict[str, object] = {
    "favorite_genre": "pop",
    "favorite_mood": "happy",
    "target_energy": 0.8,
    "likes_acoustic": False,
}


class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load song records from a CSV file and convert numeric values."""
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            row["id"] = int(row["id"])
            row["tempo_bpm"] = int(row["tempo_bpm"])
            for field in ("energy", "valence", "danceability", "acousticness"):
                row[field] = float(row[field])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song against user preferences and explain the points."""
    score = 0.0
    reasons = []

    preferred_genre = user_prefs.get("genre", user_prefs.get("favorite_genre"))
    if preferred_genre == song.get("genre"):
        score += 2.0
        reasons.append("genre match (+2.0)")

    preferred_mood = user_prefs.get("mood", user_prefs.get("favorite_mood"))
    if preferred_mood == song.get("mood"):
        score += 1.0
        reasons.append("mood match (+1.0)")

    target_energy = user_prefs.get("energy", user_prefs.get("target_energy"))
    song_energy = song.get("energy")
    if target_energy is not None and song_energy is not None:
        energy_points = 2.0 * (1.0 - abs(float(song_energy) - float(target_energy)))
        score += energy_points
        reasons.append(f"energy similarity (+{energy_points:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return the top k songs ranked by score with explanations."""
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons) if reasons else "No matching preferences"
        scored_songs.append((song, score, explanation))

    scored_songs.sort(key=lambda result: result[1], reverse=True)
    return scored_songs[:max(k, 0)]

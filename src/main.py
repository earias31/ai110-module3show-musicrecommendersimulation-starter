"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

if __package__:
    from .recommender import load_songs, recommend_songs
else:
    from recommender import load_songs, recommend_songs


USER_PROFILES = {
    "High-Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.9},
    "Chill Lofi": {"genre": "lofi", "mood": "chill", "energy": 0.4},
    "Deep Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.95},
    "High Energy, Sad Mood (conflicting)": {
        "genre": "pop",
        "mood": "sad",
        "energy": 0.95,
    },
    "Out-of-Range Energy": {"favorite_genre": "classical", "target_energy": 2.0},
    "No Preferences (edge case)": {},
    "Minimum Energy Boundary": {"energy": 0.0},
    "Conflicting Key Aliases": {
        "genre": "pop",
        "favorite_genre": "classical",
        "mood": "happy",
        "favorite_mood": "sad",
        "energy": 0.1,
        "target_energy": 0.9,
    },
}


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    for profile_name, user_prefs in USER_PROFILES.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print(f"\nTop recommendations for profile: {profile_name}")
        print(f"Preferences: {user_prefs}")
        print("=" * 48)
        for rank, (song, score, explanation) in enumerate(recommendations, start=1):
            print(f"{rank}. {song['title']} - {song['artist']}")
            print(f"   Score: {score:.2f}")
            print("   Reasons:")
            for reason in explanation.split("; "):
                print(f"   - {reason}")
            print()


if __name__ == "__main__":
    main()

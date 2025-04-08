# --- Singleton Pattern for Leaderboard Management ---
class LeaderboardManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LeaderboardManager, cls).__new__(cls)
            cls._instance.initialize()
        return cls._instance

    def initialize(self):
        self.leaderboard = {}

    def update_score(self, user_id: str, score: int):
        self.leaderboard[user_id] = score

    def get_leaderboard(self):
        return sorted(self.leaderboard.items(), key=lambda x: x[1], reverse=True)

# Example usage (for testing purposes):
if __name__ == "__main__":
    lm = LeaderboardManager()
    lm.update_score("user1", 150)
    lm.update_score("user2", 200)
    print(lm.get_leaderboard())

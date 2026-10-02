from pathlib import Path

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # High score should never be reset.
        self.high_score = 0
        self.level = 1

        # Read in saved stats.
        self.saved_stats()


    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0

    def saved_stats(self):
        """Read and write stats to file."""
        path = Path('saved_stats.txt')

        # Check for saved stats file, create one if not exist
        #       - Read in and set high score
        if path.is_file():
            self.saved_high_score = int(path.read_text())
        else:
            self.saved_high_score = 0
            path.write_text("0")

        # Save current high score if higher than saved high score.
        if self.saved_high_score < self.high_score:
            path.write_text(str(self.high_score))
        else:
            self.high_score = self.saved_high_score            
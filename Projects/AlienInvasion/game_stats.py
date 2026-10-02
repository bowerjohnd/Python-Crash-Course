import json
import hashlib
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
        path = Path('saved_stats.json')

        # Check for saved stats file, create one if not exist
        if path.is_file():
            self.loaded_in_dict = json.loads(path.read_text(encoding="utf-8"))
            self.saved_high_score = self.loaded_in_dict['high_score']
        else:
            self.saved_high_score = 0
            empty_stats = {'high_score': 0}
            path.write_text(json.dumps(empty_stats, indent=4), encoding="utf-8")

        # Save current high score if higher than saved high score.
        if self.saved_high_score < self.high_score:
            #path.write_text(str(self.high_score))
            self.loaded_in_dict['high_score'] = self.high_score
            path.write_text(json.dumps(self.loaded_in_dict, indent=4), encoding="utf-8")
        else:
            self.high_score = self.saved_high_score            
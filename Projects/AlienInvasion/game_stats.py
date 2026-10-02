import json
import base64
import hashlib
from pathlib import Path

class GameStats:
    """Track statistics for Alien Invasion."""

    SECRET_KEY = 72
    SECRET_HASH = b"MySuperSecretGameKeyDefinitelyNot72"

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
        """Read and write hashed stats to file."""
        path = Path('saved_stats.json')

        # Check for saved stats file, create one if not exist
        if path.is_file():
            self.loaded_in_dict = json.loads(path.read_text(encoding="utf-8"))
            self.saved_high_score = self._decrypt_number_value(self.loaded_in_dict['high_score'])
            print(self.saved_high_score)
        else:
            self.saved_high_score = 0
            empty_stats = {'high_score': self._encrypt_number_value(0)}
            path.write_text(json.dumps(empty_stats, indent=4), encoding="utf-8")

        # Save current high score if higher than saved high score.
        if self.saved_high_score < self.high_score:
            hash_high_score = self._encrypt_number_value(self.high_score)
            self.loaded_in_dict['high_score'] = hash_high_score
            path.write_text(json.dumps(self.loaded_in_dict, indent=4), encoding="utf-8")
        else:
            self.high_score = self.saved_high_score

    def _encrypt_number_value(self, value: int) -> str:
        # Scramble the value using SECRET KEY
        scrambled = value ^ self.SECRET_KEY
        value_bytes = scrambled.to_bytes((value.bit_length() + 7) // 8 or 1, "big")

        # Generate a "tamper-proof" signature
        hasher = hashlib.sha256(self.SECRET_HASH + value_bytes)
        signature_bytes = hasher.digest()[:4]

        # Return encoded scrambled and hash combined
        combined_bytes = value_bytes + signature_bytes
        return base64.b64encode(combined_bytes).decode('utf-8')

    def _decrypt_number_value(self, scrambled_value: str) -> int:

        try:
            # Decode text back to bytes            
            combined_bytes = base64.b64decode(scrambled_value.encode('utf-8'))

            # Separate the scrambled from signature
            value_bytes = combined_bytes[:-4]
            signature_bytes = combined_bytes[-4:]

            # Check the signature for tampering
            expected_signature = hashlib.sha256(self.SECRET_HASH + value_bytes).digest()[:4]

            if signature_bytes != expected_signature:
                raise ValueError("Save file may be corrupted, signatures don't match.")

            # Unscramble and return value
            scrambled = int.from_bytes(value_bytes, "big")
            return scrambled ^ self.SECRET_KEY

        except Exception as e:
            # game_stats may have been tampered with, return 0
            print("add to non-existant log:", e)
            return 0
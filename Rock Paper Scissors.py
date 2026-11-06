import random

CHOICES = ("rock", "paper", "scissors")
SHORTCUTS = {
    "r": "rock",
    "p": "paper",
    "s": "scissors",
}
WINNING_MOVES = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock",
}
DEFAULT_WINNING_SCORE = 2


def get_winning_score(default: int = DEFAULT_WINNING_SCORE) -> int:
    """Solicita la cantidad de puntos necesarios para ganar la partida."""
    while True:
        raw = input(
            f"Points needed to win (press Enter for {default}): "
        ).strip()
        if not raw:
            return default
        if raw.isdigit() and int(raw) > 0:
            return int(raw)
        print("Invalid number. Please enter a positive integer (e.g., 2 or 3).")


def get_player_choice() -> str:
    """Solicita y valida la jugada del usuario (acepta nombre completo o r/p/s)."""
    while True:
        choice = input(
            "\nChoose (r)ock, (p)aper, or (s)cissors: "
        ).strip().lower()
        choice = SHORTCUTS.get(choice, choice)
        if choice in CHOICES:
            return choice
        print(
            f"Invalid choice '{choice}'. Please enter rock, paper, scissors (or r, p, s)."
        )


def play_game() -> None:
    """Ejecuta la partida con marcador configurable y validación de entradas."""
    player_wins = 0
    computer_wins = 0

    print("Let's play rock, paper, or scissors!")

    try:
        winning_score = get_winning_score()
    except (EOFError, KeyboardInterrupt):
        print("\nGame aborted by user.")
        return

    while player_wins < winning_score and computer_wins < winning_score:
        try:
            player_choice = get_player_choice()
        except (EOFError, KeyboardInterrupt):
            print("\nGame aborted by user.")
            return

        computer_choice = random.choice(CHOICES)
        print(f"You chose: {player_choice} | Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif WINNING_MOVES[player_choice] == computer_choice:
            player_wins += 1
            print("You won this round and scored a point!")
        else:
            computer_wins += 1
            print("Computer won this round and scored a point!")

        print(f"Current Score - Player: {player_wins}, Computer: {computer_wins}")

    print("\n=== Final Score ===")
    print(f"Player: {player_wins} | Computer: {computer_wins}")
    if player_wins > computer_wins:
        print("Congratulations! You won the game!")
    else:
        print("Computer won the game!")


if __name__ == "__main__":
    play_game()
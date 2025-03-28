from src.datagen import get_decks, store_decks
from src.processing import calculate_all_results, store_results, create_dataframe
from src.visualizing import make_heatmap

def run_project_penney(half_deck_size: int = 26, n_decks: int = 10000, seed: int = 42) -> None:
    """
    Runs Project Penney, automatically running each function.
    
    Parameters:
        n_decks (int): Number of decks to generate.
        half_deck_size (int): Size of half a deck. Default is 26.
        seed (int): Seed for random number generation for reproducibility. Default is 42.
    
    Returns:
        None.
    """
    # Create and store decks
    decks = get_decks(n_decks = n_decks, half_deck_size = half_deck_size, seed = seed)
    store_decks(decks, f'{n_decks}_Decks')

    # Play Penney's Game with the decks, record player 2 win percentages for every choice in every deck
    results = calculate_all_results(decks)

    # Save results, specify number of decks and scoring type
    tricks = results[0]
    cards = results[1]
    store_results(tricks, f'{n_decks}_Tricks_Result')
    store_results(cards, f'{n_decks}_Cards_Result')
    
    # Create and save heatmaps
    trick_data = create_dataframe(tricks)
    make_heatmap(trick_data, "Tricks", n_decks, seed)
    card_data = create_dataframe(cards)
    make_heatmap(card_data, "Cards", n_decks, seed)
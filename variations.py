def get_case_variations(word):
    variations = [
        word.lower(),
        word.upper(),
        word.capitalize(),
        word.title(),
    ]

    if len(word) > 1:
        variations.append(word[0].upper() + word[1:].lower())

    if len(word) > 1:
        variations.append(word[0].lower() + word[1:].upper())

    seen = set()
    unique_variations = []
    for var in variations:
        if var not in seen:
            seen.add(var)
            unique_variations.append(var)

    return unique_variations


def generate_variations():
    try:
        with open("numbers.txt", "r", encoding="utf-8") as f:
            years = f.read().splitlines()
        with open("separators.txt", "r", encoding="utf-8") as f:
                separators = f.read().splitlines()
        with open("base_words.txt", "r", encoding="utf-8") as f:
            base_words = f.read().splitlines()
    except FileNotFoundError:
        print("Error: Files numbers.txt, separators.txt and base_words.txt not found")
        return []

    variations = []

    for word in base_words:
        word_variations = get_case_variations(word)

        for word_var in word_variations:
            for year in years:
                for separator in separators:
                    variations.append(f"{separator}{word_var}{year}")

    for word in base_words:
        word_variations = get_case_variations(word)

        for word_var in word_variations:
            for year in years:
                for separator in separators:
                    variations.append(f"{word_var}{separator}{year}")

    for year in years:
        for word in base_words:
            word_variations = get_case_variations(word)

            for word_var in word_variations:
                for separator in separators:
                    variations.append(f"{year}{separator}{word_var}")

    for word in base_words:
        word_variations = get_case_variations(word)

        for word_var in word_variations:
            for year in years:
                for separator in separators:
                    variations.append(f"{word_var}{year}{separator}")

    for year in years:
        for word in base_words:
            word_variations = get_case_variations(word)

            for word_var in word_variations:
                for separator in separators:
                    variations.append(f"{year}{word_var}{separator}")

    for year in years:
        for word in base_words:
            word_variations = get_case_variations(word)

            for word_var in word_variations:
                for separator in separators:
                    variations.append(f"{separator}{year}{word_var}")

    for word in base_words:
        word_variations = get_case_variations(word)

        for word_var in word_variations:
            for year in years:
                variations.append(f"{word_var}{year}")

    for year in years:
        for word in base_words:
            word_variations = get_case_variations(word)

            for word_var in word_variations:
                variations.append(f"{year}{word_var}")

    for word in base_words:
        word_variations = get_case_variations(word)

        for word_var in word_variations:
            variations.append(word_var)

    for year in years:
        variations.append(year)

    variations_unique = []
    seen = set()
    for var in variations:
        if var not in seen:
            seen.add(var)
            variations_unique.append(var)

    return variations_unique


def save_variations(file="variations.txt"):
    variations = generate_variations()

    with open(file, "w", encoding="utf-8") as f:
        for var in variations:
            f.write(var + "\n")

    print(f"✓ Generated {len(variations)} unique variations")
    print(f"✓ Saved in: {file}")
    print("\nFirst 20 variations:")
    for i, var in enumerate(variations[:20], 1):
        print(f"  {i}. {var}")

    if len(variations) > 20:
        print(f"\n... and more {len(variations) - 20} variations")


if __name__ == "__main__":
    save_variations()

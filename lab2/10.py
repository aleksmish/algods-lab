def eastern_calendar(year: int) -> str:
    colors = ["зеленой", "красной", "желтой", "белой", "черной"]
    colors_masc = ["зеленого", "красного", "желтого", "белого", "черного"]
    
    animals = [
        "крысы", "коровы", "тигра", "зайца", "дракона", "змеи",
        "лошади", "овцы", "обезьяны", "курицы", "собаки", "свиньи"
    ]
    
    masc_indices = {2, 3, 4}
    
    offset = (year - 1984) % 60
    color_idx = offset // 12
    animal_idx = offset % 12
    
    color_word = colors_masc[color_idx] if animal_idx in masc_indices else colors[color_idx]
    
    return f"год {color_word} {animals[animal_idx]}"

year = int(input())
print(eastern_calendar(year))

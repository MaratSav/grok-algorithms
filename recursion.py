def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile:  # Проверяем, не пуст ли pile
        box = pile.grab_a_box()  # Получаем коробку из pile
        for item in box:  # Предполагаем, что box - это итерируемый объект
            if item.is_a_box():
                pile.append(item)  # Добавляем коробку обратно в pile
            elif item.is_a_key():
                print("found the key")

def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item)  # Рекурсивный вызов для вложенной коробки
        elif item.is_a_key():
            print("found the key")



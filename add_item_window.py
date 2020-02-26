import pygame
from text_box import text_box
from item import item
from buttom import buttom


def add_item(text_input_boxes):
    new_thing = []
    for i in text_input_boxes:
        new_thing.append(i.return_text())
        
    context, level, state, color, date = new_thing
    new_thing = item(context, level, state, color, date)
    new_thing.write_file("list.txt")
    return new_thing


def add_item_window(size, things, list_box):
    create_window_size = (500, 600)
    create_window = pygame.display.set_mode(create_window_size)
    pygame.display.set_caption("Add item")
    is_create = True
    text_input_labels = []
    text_input_boxes = []
    counter = 0
    white, black = (255, 255, 255), (0, 0, 0)
    textbox_active_color = (242, 179, 189) #Luka pink
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    item_elements = ['Context', 'Level', 'State', 'Color', 'Date']
    for i in item_elements:
        temp_box = text_box(pygame.Rect([110, 10 + 80*counter, 380, 70]), white, textbox_active_color)
        text_input_boxes.append(temp_box)

        text_surface = myfont.render(i, False, (255, 255, 255))
        text_input_labels.append(text_surface)
        counter += 1

    Ok_buttom = buttom(pygame.Rect([50, 420, 130, 70]), white, black)
    Cancel_buttom = buttom(pygame.Rect([280, 420, 130, 70]), white, black)
    
    temp_box = text_box(pygame.Rect([20, 20+100*(len(list_box)), 510, 80]), white, textbox_active_color)

    is_cancel = False
    while is_create:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_create = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in text_input_boxes:
                    if i.return_position().collidepoint(event.pos):
                        i.change_is_active(True)
                    else:
                        i.change_is_active(False)
            if event.type == pygame.KEYDOWN:
                for i in text_input_boxes:
                    if i.return_is_active():
                        if event.key == pygame.K_BACKSPACE:
                            i.delete_text()
                        else:
                            i.add_text(event.unicode)
        mouse = pygame.mouse.get_pos()
        pressed = pygame.key.get_pressed()
        for i in text_input_boxes:
            if i.return_is_active():
                i.draw_active_box(create_window)
            else:
                i.draw_unactive_box(create_window)
            i.write_in_box(create_window, myfont)

        x = 0
        for i in text_input_labels:
            create_window.blit(i, (20, 35 + 80 * x ))
            x += 1

        

        
        if(Ok_buttom.buttom_is_press(create_window, mouse)):
            thing_item= add_item(text_input_boxes)
            temp_box = text_box(pygame.Rect([20, 20 + 100*len(things), 510, 80]), white, textbox_active_color)
            temp_box.change_text(thing_item.string_form())
            things.append(thing_item)
            list_box.append(temp_box)
            is_create = False
            print("Done")
        if(Cancel_buttom.buttom_is_press(create_window, mouse)):
            is_cancel = True
            is_create = False
        Ok_buttom.text_in_buttom(create_window, myfont, "Ok")
        Cancel_buttom.text_in_buttom(create_window, myfont, "Cancel")
        
        
        pygame.display.flip()
        
    window = pygame.display.set_mode(size)
    pygame.display.set_caption("Listing System")


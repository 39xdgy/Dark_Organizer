import pygame
from item import item
from buttom import buttom
from text_box import text_box

pygame.init()

size = (1280, 720)
white = (255, 255, 255)
black = (0, 0, 0)
textbox_active_color = (242, 179, 189) #Luka pink
window = pygame.display.set_mode(size)
pygame.display.set_caption("Listing System")

log_in = True
main_in = True
start_ticks = pygame.time.get_ticks()

myfont = pygame.font.SysFont('Comic Sans MS', 30)
LB = buttom(pygame.Rect([600, 480, 80, 40]), white, (170, 100, 230))
item_elements = ['Context', 'Level', 'State', 'Color', 'Date']
UI_active = False
UI_text = ''
PW_active = False
PW_text = ''
PW_show_text = ''

my_ID = 'Jasonwang1575'
my_PW = 'Wjs@1997'

UIP = text_box(pygame.Rect([500, 240, 300, 30]), white, textbox_active_color)
PWP = text_box(pygame.Rect([500, 280, 300, 30]), white, textbox_active_color)


def check_login(input_ID, input_PW, right_ID, right_PW):
    if(input_ID == right_ID and input_PW == right_PW):
           print("Welcome back")
           return True
    else:
       print("Error")
       return False


def break_line(input_string):
    fin = input_string.split(', ')
    color_string = ''
    flag_for_break_line = False
    org_len = len(fin)
    start_ = 0
    end_ = 0
    for i in fin:
        #print(i)
        if i.startswith('('):
            flag_for_break_line = True
            start_ = fin.index(i)
            #print("yes!")
        if i.endswith(')'):
            flag_for_break_line = False
            color_string += i
            end_ = fin.index(i)
            fin[fin.index(i)] = color_string

            #print("Im out")
            break
        if flag_for_break_line:
            color_string += i + ', '
            #print("Change i")

    for i in range(0, end_-start_):
        del fin[start_]
    
    return fin


def add_item_window():
    create_window_size = (500, 600)
    create_window = pygame.display.set_mode(create_window_size)
    pygame.display.set_caption("Add item")
    is_create = True
    text_input_labels = []
    text_input_boxes = []
    counter = 0
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
            new_thing = []
            for i in text_input_boxes:
                new_thing.append(i.return_text())

            context, level, state, color, date = new_thing
            new_thing = item(context, level, state, color, date)
            new_thing.write_file("list.txt")
            things.append(new_thing)
            temp_box = text_box(pygame.Rect([20, 35 + 80*len(things), 510, 80]), white, textbox_active_color)
            temp_box.change_text(new_thing.string_form())
            is_create = False
            print("Done")
        if(Cancel_buttom.buttom_is_press(create_window, mouse)):
            is_cancel = True
            is_create = False
        Ok_buttom.text_in_buttom(create_window, myfont, "Ok")
        Cancel_buttom.text_in_buttom(create_window, myfont, "Cancel")
        
        
        pygame.display.flip()

    if not is_cancel:
        list_box.append(temp_box)
    window = pygame.display.set_mode(size)
    pygame.display.set_caption("Listing System")















#log_in = False

while log_in:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            log_in = False
            main_in = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if UIP.return_position().collidepoint(event.pos):
                UIP.change_is_active(True)
                PWP.change_is_active(False)
            elif PWP.return_position().collidepoint(event.pos):
                PWP.change_is_active(True)
                UIP.change_is_active(False)
            else:
                UIP.change_is_active(False)
                PWP.change_is_active(False)
        if event.type == pygame.KEYDOWN:
            if UIP.return_is_active():
                if event.key == pygame.K_BACKSPACE:
                    UIP.delete_text()
                elif event.key == pygame.K_TAB:
                    PWP.change_is_active(True)
                    UIP.change_is_active(False)
                else:
                    UIP.add_text(event.unicode)
            elif PWP.return_is_active():
                if event.key == pygame.K_BACKSPACE:
                    PWP.delete_text()
                    PW_show_text = PW_show_text[:-1]
                elif event.key == pygame.K_RETURN:
                    if(check_login(UIP.return_text(), PWP.return_text(), my_ID, my_PW)):
                        log_in = False
                else:
                    PWP.add_text(event.unicode)
                    if not (event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT):
                        PW_show_text += '*'
            elif event.key == pygame.K_TAB:
                UIP.change_is_active(True)
                        
            
    window.fill((0, 0, 0))

    mouse = pygame.mouse.get_pos()
    pressed = pygame.key.get_pressed()

    if UIP.return_is_active(): UIP.draw_active_box(window)
    else: UIP.draw_unactive_box(window)
    if PWP.return_is_active(): PWP.draw_active_box(window)
    else: PWP.draw_unactive_box(window)

    UIP.write_in_box(window, myfont)
    PWP.write_in_box_with_text(window, myfont, PW_show_text)
    
    if(LB.buttom_is_press(window, mouse)):
        if(check_login(UIP.return_text(), PWP.return_text(), my_ID, my_PW)):
            log_in = False
    LB.text_in_buttom(window, myfont, "Log in")
    pygame.display.flip()


sort_buttom = buttom(pygame.Rect([1150, 530, 80, 40]), white, black)
create_item_buttom = buttom(pygame.Rect([1150, 580, 80, 40]), white, black)
list_buttom = buttom(pygame.Rect([1150, 630, 80, 40]), white, black)

txt_file = open("list.txt", "r")
things =  []
list_box = []
for line in txt_file:
    contect, level, state, color, date = break_line(line)
    things.append(item(contect, level, state, color, date))


    

num_of_item = 0
for i in things:
    temp_box = text_box(pygame.Rect([20, 20+100*num_of_item, 510, 80]), white, textbox_active_color)
    temp_box.change_text(i.string_form())
    list_box.append(temp_box)
    num_of_item += 1
    




    
    
while main_in:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_in = False

    window.fill((0, 0, 0))

    mouse = pygame.mouse.get_pos()
    pressed = pygame.key.get_pressed()

    pygame.draw.line(window, white, (550, 0), (550, 720))
    pygame.draw.line(window, white, (1100, 0), (1100, 720))

    for i in list_box:
        if(i.box_is_press(window, mouse)):
            print(i.return_position()[1])
        i.write_in_box(window, myfont)
        

    if(sort_buttom.buttom_is_press(window, mouse)):
        continue
    sort_buttom.text_in_buttom(window, myfont, "Sort")        
    if(list_buttom.buttom_is_press(window, mouse)):
        main_in = False
    list_buttom.text_in_buttom(window, myfont, "Exit")
    if(create_item_buttom.buttom_is_press(window, mouse)):
        add_item_window()
    create_item_buttom.text_in_buttom(window, myfont, "Add")




    pygame.display.flip()

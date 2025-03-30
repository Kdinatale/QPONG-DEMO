from . import globals, resources

def draw_statevector_grid(screen):
    font = resources.Font()
    basis_states = [
        '|000>',
        '|001>',
        '|010>',
        '|011>',
        '|100>',
        '|101>',
        '|110>',
        '|111>'
    ]

    # want to set the height of the state vectors so it is evenly distributed
    # divides by 8 and rounds to ensure it is an integer
    statevector_height = int(round(globals.FIELD_HEIGHT / len(basis_states)))
    
    for i in range(len(basis_states)):
        # getting the state vector font size and rendering basis_state text
        text = font.vector_font.render(basis_states[i], 1, globals.WHITE)
        screen.blit(text, (globals.WINDOW_WIDTH - text.get_width(), i*statevector_height + text.get_height()))
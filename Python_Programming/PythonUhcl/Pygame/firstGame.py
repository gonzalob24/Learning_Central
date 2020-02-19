import pygame


def main():
    # set up the game and run the main loop
    pygame.init() # prepaes the pygame module for use
    surface_sz = 480 # physical surface size in pixels

    # Create surface of (width, height), and its window.
    main_surface = pygame.display.set_mode((surface_sz, surface_sz))

    # Set up some data to describe a small rectangle and its color
    small_rect = (300, 200, 150, 90)
    some_color = (255, 0, 0)            # Acolorisamixof(Red,Green, Blue)

    while True:
        ev = pygame.event.poll()        # Look for any event
        if ev.type == pygame.QUIT:      # Window close button clicked?
            break
        # Update your game objects and data structures here... 21
        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        main_surface.fill((0, 200, 255))

        # Overpaint a smaller rectangle on the main surface
        main_surface.fill(some_color, small_rect)

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()

        pygame.quit() # Once we leave the loop, close the window.

main()


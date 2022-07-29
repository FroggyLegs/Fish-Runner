from sprite import*


def quit():
    global gamerunning
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_ESCAPE:
            gamerunning = False
    if event.type == pygame.QUIT:
        gamerunning = False


def jump():
    if not fish.isjump:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP \
                    or event.key == pygame.K_RIGHT:
                fish.isjump = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                fish.isjump = True


def duck():
    if fish.isjump:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT or event.key == pygame.K_DOWN \
                    or event.key == pygame.K_LEFT:
                fish.fallspeed = fish.duck
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                fish.fallspeed = fish.duck


def dive():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LSHIFT or event.key == pygame.K_DOWN \
                or event.key == pygame.K_LEFT:
            fish.isdive = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                fish.isdive = True


def not_dive():
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LSHIFT or event.key == pygame.K_DOWN \
                or event.key == pygame.K_LEFT:
            fish.isdive = False
    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 2:
            fish.isdive = False
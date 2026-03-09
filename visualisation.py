import pygame, math

pygame.init()
s = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("Cloth Simulation")

W, H = s.get_width(), s.get_height()
clock = pygame.time.Clock()

P = [[x*20 + W/4, y*20+100, y*20+100, y == 0] for y in range(30) for x in range(50)]
S = [[i, i+1, 1] for i in range(len(P)) if (i+1) % 50] + [[i, i+50, 1] for i in range(len(P) - 50)]

while True:

    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()

    s.fill((0,5,10))
    mx, my = pygame.mouse.get_pos()
    md = pygame.mouse.get_pressed()

    for p in P:
        if not p[3]:
            if md[0] and math.hypot(p[0]-mx, p[1]-my) < 30:
                p[0], p[1] = mx, my

            vx = max(-20, min(20, (p[0]-p[2]) * 0.99))
            vy = max(-20, min(20, (p[1]-p[3]) * 0.99))

            p[2], p[3], p[0], p[1] = p[0], p[1], p[0]+vx, p[1]+vy+0.4

    for _ in range(6):
        for sk in S:
            if not sk[2]:
                continue

            p1, p2 = P[sk[0]], P[sk[1]]
            dx, dy = p1[0]-p2[0], p1[1]-p2[1]
            d = math.hypot(dx,dy) or 0.1

            if d > 100 or (md[2] and math.hypot((p1[0]+p2[0])/2-mx,(p1[1]+p2[1])/2-my) < 15):
                sk[2] = 0
                continue

            f = (20-d)/d * 0.5

            if not p1[3]:
                p1[0] -= dx*f
                p1[1] -= dy*f
            if not p2[3]:
                p2[0] += dx*f
                p2[1] += dy*f

    for p1, p2, active in S:
        if active:
            pygame.draw.line(s,(0,255,150),(P[p1][0],P[p1][1]),(P[p2][0],P[p2][1]),2)

    pygame.display.flip()
    clock.tick(60)
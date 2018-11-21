import pygame
import sys

from bullet import Bullet
from enemy import Enemy

def check_events(game_settings, screen, player, bullets):
    """按键判断"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            #退出游戏q键
            if event.key == pygame.K_q:
                sys.exit()
            #玩家方向按键
            elif event.key == pygame.K_RIGHT:
                player.moving_right = True
            elif event.key == pygame.K_LEFT:
                player.moving_left = True
            elif event.key == pygame.K_UP:
                player.moving_up = True
            elif event.key == pygame.K_DOWN:
                player.moving_down = True
            #射击按键
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(game_settings, screen, player)
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.moving_right = False
            elif event.key == pygame.K_LEFT:
                player.moving_left = False
            elif event.key == pygame.K_UP:
                player.moving_up = False
            elif event.key == pygame.K_DOWN:
                player.moving_down = False

def update_bullets(bullets, enemys):
    """更新子弹组的状态数据"""
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    #检查是否有子弹击中了外星人
    #groupcollide(Group1，Group2，True，True )
    #如果Group1和Group2中的精灵相互碰撞，则删除这两个精灵（由后面的True决定）
    collisions = pygame.sprite.groupcollide(bullets, enemys, True, True)

def update_enemys(screen, game_settings, enemys, player):
    """更新敌机组的状态数据"""
    if len(enemys) < game_settings.enemy_num :
        new_enemy = Enemy(screen, game_settings)
        enemys.add(new_enemy)

    enemys.update()

    for enemy in enemys.copy():
        if enemy.rect.top >= game_settings.screen_height:
            enemys.remove(enemy)

    if pygame.sprite.spritecollideany(player , enemys):
        screen_rect = screen.get_rect()
        player.center = float(screen_rect.centerx)
        player.bottom = float(screen_rect.bottom)

def update_screen(game_settings, screen, player, bullets, enemys, button):

    # 绘制屏幕
    screen.fill((game_settings.bg_color))
    #绘制player
    player.blit_player()
    #绘制敌人组
    for enemy in enemys:
        enemy.blit_enemy()
    #绘制子弹组
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    #button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()
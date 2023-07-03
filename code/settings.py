WIDTH = 950
HEIGHT = 720
FPS = 50
TILESIZE = 64

# UI
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = '../image/font/font.ttf'
UI_FONT_SIZE = 18

# general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'


# ui colors
HEALTH_COLOR = 'green'
ENERGY_COLOR = 'red'
UI_BORDER_COLOR_ACTIVE = 'gold'

# weapons
weapon_data = {
    'sword': {'cooldown': 150, 'damage': 15, 'graphic': '../image/weapon/sword/blade.png'},
    'heavy_sword': {'cooldown': 600, 'damage': 55, 'graphic': '../image/weapon/heavy_sword/blade.png'}

}

# special skills
skill_data = {'single_arc': {'strength': 5, 'cost': 20, 'graphic': '../image/skill/single_arc/arc.png'},
              'dual_arc': {'strength': 7, 'cost': 45, 'graphic': '../image/skill/dual_arc/arc.png'},
              'minimal_heal': {'strength': 25, 'cost': 45, 'graphic': '../image/skill/heal/heal.png'}}

# enemy
enemy_data = {
    'slime': {'health': 70, 'exp': 20, 'damage': 10,
              'attack_type': 'smack', 'attack_sound': '..audio/attack/claw.wav',
              'speed': 1, 'resistance': 3, 'attack_radius': 40, 'notice_radius': 500},

    'mino': {'health': 650, 'exp': 500, 'damage': 40,
             'attack_type': 'slash', 'attack_sound': '..audio/attack/claw.wav',
             'speed': 3, 'resistance': 5, 'attack_radius': 70, 'notice_radius': 600},

    'knight': {'health': 200, 'exp': 90, 'damage': 20,
               'attack_type': 'slash', 'attack_sound': '..audio/attack/slash.wav',
               'speed': 3, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 200},

    'kex': {'health': 900, 'exp': 1000, 'damage': 45,
            'attack_type': 'smack', 'attack_sound': '..audio/attack/fireball.wav',
            'speed': 7, 'resistance': 6, 'attack_radius': 30, 'notice_radius': 400},

    'dual_knight': {'health': 190, 'exp': 90, 'damage': 20,
                    'attack_type': 'slash', 'attack_sound': '..audio/attack/slash.wav',
                    'speed': 4, 'resistance': 3, 'attack_radius': 65, 'notice_radius': 250}}
# WORLD_MAP = [
# ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'ex', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
# ['x', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 'x'],
# ['x', ' ', 'p', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
# ['x', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', ' ', 'x'],
# ['x', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', 'x'],
# ['x', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
# ['x', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x'],
# ['x', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x'],
# ['x', ' ', ' ', 'x', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x'],
# ['x', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x'],
# ['x', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x'],
# ['x', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x'],
# ['x', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 'x', 'x', ' ', ' ', ' ', 'x'],
# ['x', ' ', ' ', ' ', ' ', ' ', 'x', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
# ['x', ' ', ' ', ' ', ' ', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
# ['x', ' ', ' ', ' ', ' ', ' ', 'x', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
# ['x', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
# ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
# ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
# ['x', 'x', ' ', ' ', ' ', ' ', ' ', 'p1', ' ', 'p1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 'x'],
# ['x', 'x', 'x', 'w', 'w', 'w', 'w', 'w', 't', 'w', 'w', 'w', 'w', 'w', 'x', 'x', 'x', 'x', 'x']
# ]

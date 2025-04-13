# levels.py
# Настройки уровней: скорость и координаты стен для каждого уровня

levels = {
    1: {
        "speed": 10,         # Начальный уровень — нет стен, базовая скорость
        "walls": []
    },
    2: {
        "speed": 13,         # Скорость чуть выше, добавляется две стены
        "walls": [
            [(100, 100), (100, 300)],  # Вертикальная стена слева
            [(200, 400), (400, 400)]   # Горизонтальная стена снизу
        ]
    },
    3: {
        "speed": 16,         # Ещё быстрее, три стены образуют П-образный барьер
        "walls": [
            [(150, 150), (450, 150)],  # Верхняя горизонталь
            [(150, 450), (450, 450)],  # Нижняя горизонталь
            [(300, 150), (300, 450)]   # Центральная вертикаль
        ]
    },
    4: {
        "speed": 19,         # Уровень 4 — почти рамка по краям
        "walls": [
            [(0, 0), (600, 0)],        # Верхняя граница
            [(0, 580), (600, 580)],    # Нижняя граница
            [(0, 0), (0, 600)],        # Левая граница
            [(580, 0), (580, 600)]     # Правая граница
        ]
    },
    5: {
        "speed": 22,         # Ещё сложнее: добавлены диагонали
        "walls": [
            [(100, 100), (500, 500)],  # Диагональ слева направо
            [(500, 100), (100, 500)]   # Диагональ справа налево
        ]
    }
}
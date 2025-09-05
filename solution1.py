solution.py
`python
#!/usr/bin/env python3
# solution.py — Lab-1 (variant 1)
import os
import sys
import time
import math

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# 1) Флаг Франции (3 вертикальных полосы) — используя ANSI цвета
def flag_france(width=30, height=9):
    BLUE = '\x1b[44m'
    WHITE = '\x1b[47m'
    RED = '\x1b[41m'
    RESET = '\x1b[0m'
    col = width // 3
    for r in range(height):
        line = BLUE + ' ' * col + WHITE + ' ' * col + RED + ' ' * (width - 2*col) + RESET
        print(line)

# 2) Узoр (вариант a) — простая шахматка
def pattern_a(width=40, height=6):
    for r in range(height):
        line = ''
        for c in range(width):
            line += ('#' if (r+c) % 2 == 0 else ' ')
        print(line)

# 3) ASCII-график y = x^2, x>=0, height >=9
def ascii_plot_quadratic(height=12, width=40):
    # y = x^2 -> scale to height
    xs = [i * (4.0 / width) for i in range(width)]  # x from 0..4
    ys = [x*x for x in xs]
    maxy = max(ys)
    rows = [[' ']*width for _ in range(height)]
    for i,x in enumerate(xs):
        y = ys[i]
        row = height - 1 - int((y / maxy) * (height-1))
        rows[row][i] = '*'
    print("y = x^2 (ASCII)")
    for r in rows:
        print(''.join(r))

# 4) sequence.txt диаграмма процентов >0 и <0 (variant 1)
def seq_diagram(path='sequence.txt'):
    if not os.path.exists(path):
        print(f"Файл {path} не найден. Помести sequence.txt в репозиторий.")
        return
    vals = []
    with open(path, encoding='utf-8') as f:
        for token in f.read().split():
            try:
                vals.append(float(token))
            except:
                pass
    if not vals:
        print("Нет чисел в sequence.txt")
        return
    positives = sum(1 for v in vals if v > 0)
    negatives = sum(1 for v in vals if v < 0)
    zeros = sum(1 for v in vals if v == 0)
    total = len(vals)
    def bar(n):
        L = 40
        return '#' * int((n/total)*L)
    print(f"Всего чисел: {total}")
    print(f">0: {positives:>4} {bar(positives)} {positives/total*100:.1f}%")
    print(f"<0: {negatives:>4} {bar(negatives)} {negatives/total*100:.1f}%")
    print(f"=0: {zeros:>4} {bar(zeros)} {zeros/total*100:.1f}%")

# 5) Простая анимация 2 кадра
def animation_demo():
    frame1 = [" (•_•) ", "<|   ", " / \\" ]
    frame2 = [" (•_•) ", "  | > ", " / \\" ]
    for i in range(6):
        clear()
        for l in (frame1 if i%2==0 else frame2):
            print(l)
        time.sleep(0.4)

def main():
    clear()
    print("=== Lab-1 (variant 1) ===\n")
    print("1) Flag (France):")
    flag_france()
    print("\n2) Pattern (a):")
    pattern_a()
    print("\n3) ASCII plot:")
    ascii_plot_quadratic(height=12, width=60)
    print("\n4) Sequence diagram (from sequence.txt):")
    seq_diagram('sequence.txt')
    print("\n5) Animation (2 frames):")
    print("Animating 3 seconds...")
    animation_demo()
    print("Done.")

if name == 'main':
    main()

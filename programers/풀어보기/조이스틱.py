name = "JEROEN"

spell_move = 0
curser_move = len(name) - 1

for index,spell in enumerate(name) :
    spell_move += min(ord(spell) - ord('A'), ord('Z') - ord(spell) + 1)

    next = index + 1
    while next < len(name) and name[next] == 'A' :
        next += 1

    curser_move = min(curser_move, 2*index + len(name) - next, index + 2*(len(name) - next))

print(spell_move + curser_move)


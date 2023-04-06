letters = "BINARYSEARCHTREE"
taken = []
values = []


def seat_person(lv, si):

    if len(taken) == 0:
        val = 0
    elif len(taken) == 1:
        val = 1
    else:
        left = si - 1
        right = si
        l_val = values[left] if (0 <= left < len(values)) else 0
        r_val = values[right] if (right < len(values)) else 0
        val = max(l_val, r_val) + 1
    values.insert(si, val)
    taken.insert(si, lv)


for nli, nlv in enumerate(letters):
    pos_index = nli
    for sli, slv in enumerate(taken):
        if nlv <= slv:
            pos_index = sli
            break
    seat_person(nlv, pos_index)
print(f"taken: {taken} \nvalues: {values}")

result = []
for i, location in enumerate(values):
    for j, value in enumerate(values):
        if value == i:
            result.append(taken[j])
print(''.join(result))

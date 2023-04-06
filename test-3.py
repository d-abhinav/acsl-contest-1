letters = "BINARYSEARCHTREE"
taken = []
values = []


def seat_person(lv, si):
  if len(taken) == 0:
    value = 0
  elif len(taken) == 1:
    value = 1
  else:
    left = si-1
    right = si
    lval = values[left] if (left >= 0 and left < len(values)) else 0
    rval = values[right] if (right < len(values)) else 0
    value = max(lval, rval) + 1
  values.insert(si, value)
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
    if (value == i):
     result.append(taken[j])
print(''.join(result))
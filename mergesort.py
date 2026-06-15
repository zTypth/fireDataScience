import matplotlib.pyplot as plt

def mergeSort(merge_list):

    if (len(merge_list) > 1):                           # Abbruchbedingung

        mid = len(merge_list) // 2                      # Liste in zwei Hälften teilen
        left = merge_list[:mid]
        right = merge_list[mid:]

        mergeSort(left)                                 # Funktion mit neuen Listen rekursiv aufrufen
        mergeSort(right)

        l = r = i = 0                                   # Variablen fürs Sortieren setzen
        left_len = len(left)
        right_len = len(right)

        while l < left_len and r < right_len:           # solange beide Listen Elemente besitzen, werden aktuelle Werte verglichen
            if left[l] <= right[r]:
                    merge_list[i] = left[l]
                    l += 1
            else:
                merge_list[i] = right[r]
                r += 1
            i += 1

        while l < left_len:                             # ist eine Liste vorher leer, werden die restlichen Elemente der anderen Liste übernommen
            merge_list[i] = left[l]
            l += 1
            i += 1

        while r < right_len:
            merge_list[i] = right[r]
            r += 1
            i += 1

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

unsorted_list = my_list.copy()

mergeSort(my_list)

fig, ax = plt.subplots(1, 2, figsize=(10, 4), sharey=True)

ax[0].bar(range(len(unsorted_list)), unsorted_list)
ax[0].set_xlabel("Index")
ax[0].set_ylabel("Wert")
ax[0].set_title("Vor dem Sortieren")
ax[0].grid(axis="y")

ax[1].bar(range(len(my_list)), my_list)
ax[1].set_xlabel("Index")
ax[1].set_ylabel("Wert")
ax[1].set_title("Nach dem Sortieren")
ax[1].grid(axis="y")

fig.tight_layout()
plt.show()

# import nachoben
# funktionsnamen kleinschreiben
# assignment in den while schleifen
# list_to_sort_by_merge -> merge_list
# unnötig lange if bedingung
# x variable entfernt
# l r i variablen in eine zeile geschrieben
# len(left) und len(right) durch variablen ersetzt, damit sie nicht jedesmal neuberechnet werden müssen
# assignment funktion gelöscht, unnötig. kann direkt in die if schleife integriert werden.

# plotting verfeinert. beschriftungen hinzugefügt. 2 in 1 graph. 
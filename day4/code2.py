def preprocess_data():
    grid = []
    with open("input.txt", "r") as f:
        for line in f:
            line = line.rstrip("\n")
            grid.append(list(line))   # <- liste de caractères
    return grid

def compter_voisins_valeur(grid, i, j, valeur):
    nb_lignes = len(grid)
    nb_colonnes = len(grid[0])
    count = 0

    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if di == 0 and dj == 0:
                continue
            ni = i + di
            nj = j + dj
            if 0 <= ni < nb_lignes and 0 <= nj < nb_colonnes:
                if grid[ni][nj] == valeur:
                    count += 1
    return count


def etape(grid, valeur_centre="@",
          valeur_voisin="@",
          seuil_voisins=4):
    nb_lignes = len(grid)
    nb_colonnes = len(grid[0])

    new_grid = [row[:] for row in grid]
    changed = False
    removed_this_step = 0

    for i in range(nb_lignes):
        for j in range(nb_colonnes):
            if grid[i][j] != valeur_centre:
                continue

            nb_voisins = compter_voisins_valeur(grid, i, j, valeur_voisin)

            if nb_voisins < seuil_voisins:
                new_grid[i][j] = "."
                changed = True
                removed_this_step += 1

    return new_grid, changed, removed_this_step

grid = preprocess_data()

total_removed = 0
iteration = 0

while True:
    grid, changed, removed = etape(grid)
    total_removed += removed
    iteration += 1

    if not changed:
        break

print(f"Stabilisation après {iteration} étapes.")
print(f"Nombre total d'éléments supprimés : {total_removed}")




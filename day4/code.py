def preprocess_data():
    grid = []
    with open("input.txt", "r") as file:
        for line in file:
            grid.append(line.rstrip("\n"))  # ou list(line.rstrip("\n")) si tu veux une liste de caractères
    return grid

data = preprocess_data()

def compter_voisins_valeur_pour_toute_grille(grid, valeur_centre, valeur_voisin):
    nb_lignes = len(grid)
    nb_colonnes = len(grid[0])
    result = [[0] * nb_colonnes for _ in range(nb_lignes)]

    for i in range(nb_lignes):
        for j in range(nb_colonnes):

            # On ne s'intéresse qu'aux cellules dont la valeur == valeur_centre
            if grid[i][j] != valeur_centre:
                continue

            count = 0
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    if di == 0 and dj == 0:
                        continue
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < nb_lignes and 0 <= nj < nb_colonnes:
                        if grid[ni][nj] == valeur_voisin:
                            count += 1

            result[i][j] = count

    # Maintenant on compte combien de cellules "centre" ont moins de 4 voisins de valeur_voisin
    c = 0
    for i in range(nb_lignes):
        for j in range(nb_colonnes):
            if grid[i][j] == valeur_centre and result[i][j] < 4:
                c += 1

    return c




print(compter_voisins_valeur_pour_toute_grille(data,"@", "@"))





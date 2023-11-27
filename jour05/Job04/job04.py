def draw_tapis_without_diagonal(n):
    for i in range(n + 1):
        for j in range(n + 1):
            if i == j or i == n or j == n:
                print(' ', end='')
            else:
                print('#', end='')
        print()

taille_tapis = int(input("Entrez la taille du tapis : "))

draw_tapis_without_diagonal(taille_tapis)
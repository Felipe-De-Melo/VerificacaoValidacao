def calcular_media(nota1, nota2, nota3):
    notas = [nota1, nota2, nota3]
    if not all(0 <= n <= 10 for n in notas):
        raise ValueError("Notas devem estar entre 0 e 10.")
    return round(sum(notas) / 3, 2)


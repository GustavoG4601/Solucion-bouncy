def is_bouncy(number):
    """
    Determina si un número es "bouncy".
    Un número es "bouncy" si no es ni creciente ni decreciente.
    """
    num_str = str(number)
    increasing = decreasing = False

    for i in range(len(num_str) - 1):
        if num_str[i] < num_str[i + 1]:
            increasing = True
        elif num_str[i] > num_str[i + 1]:
            decreasing = True

        # Si es tanto creciente como decreciente, es "bouncy".
        if increasing and decreasing:
            return True

    return False


def find_least_bouncy_threshold(threshold_percentage):
    """
    Encuentra el menor número para el cual la proporción de números "bouncy"
    alcanza el porcentaje dado.
    """
    count_bouncy = 0
    number = 0

    while True:
        number += 1
        if is_bouncy(number):
            count_bouncy += 1

        # Calcular la proporción de números bouncy.
        proportion = (count_bouncy / number) * 100

        # Si alcanzamos o superamos el porcentaje requerido, retornamos el número.
        if proportion == threshold_percentage:
            return number


# Encontrar el menor número para el cual la proporción de números "bouncy" es 99%.
result = find_least_bouncy_threshold(99)
print(f"El menor número para el cual la proporción de números bouncy es 99% es: {result}")

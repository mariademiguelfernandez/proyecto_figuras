from lib import cuadrado, rectangulo
print("Proyecto Figuras")
print(cuadrado.get_identificador())
lado=4
print(f"El área de un {cuadrado.get_identificador()} de lado {lado} es: {cuadrado.get_area(lado)} 
    y el perimetro es {cuadrado.get_perimetro(lado)}")

base = 4
altura=2
print(rectangulo.get_identificador())
print(f"El área de un {rectangulo.get_identificador()} de base {base}\
      y altura {altura} es: {rectangulo.get_area(base,altura)} \
        y el perímetro es:{rectangulo.get_perimetro(base,altura)}")
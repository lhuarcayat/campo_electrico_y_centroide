import math
import matplotlib.pyplot as plt
import numpy as np
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class GeometricElement:
    """Representa un elemento geométrico con área, centroide y signo"""
    name: str
    area: float
    centroid_x: float
    centroid_y: float
    is_positive: bool = True  # True suma área, False resta área
    
    @property
    def signed_area(self):
        return self.area if self.is_positive else -self.area

class CentroidCalculator:
    """Calculadora de centroides para figuras compuestas
    
    Métodos disponibles:
    - add_rectangle(): Rectángulo por dimensiones y centro
    - add_circle(): Círculo por radio y centro  
    - add_semicircle(): Semicírculo por radio, centro y orientación
    - add_triangle(): Triángulo rectángulo simple (LIMITADO)
    - add_triangle_by_vertices(): Triángulo por 3 vértices (GENERAL)
    - add_custom_element(): Elemento con área y centroide conocidos
    """
    
    def __init__(self):
        self.elements: List[GeometricElement] = []
    
    def add_element(self, element: GeometricElement):
        """Agrega un elemento geométrico"""
        self.elements.append(element)
    
    def add_rectangle(self, name: str, width: float, height: float, 
                     center_x: float, center_y: float, is_positive: bool = True):
        """Agrega un rectángulo"""
        area = width * height
        element = GeometricElement(name, area, center_x, center_y, is_positive)
        self.add_element(element)

    def add_rectangle_by_vertices(self, name: str, x1: float, y1: float, 
                                 x2: float, y2: float, x3: float, y3: float, 
                                 x4: float, y4: float, is_positive: bool = True):
        """Agrega un rectángulo usando las coordenadas de sus 4 vértices (método general)
        Los vértices deben estar en orden (horario o antihorario)
        """
        # Calcular área usando la fórmula del polígono (shoelace formula)
        area = abs((x1*(y2-y4) + x2*(y3-y1) + x3*(y4-y2) + x4*(y1-y3)) / 2)
        
        # Centroide: promedio de los 4 vértices
        centroid_x = (x1 + x2 + x3 + x4) / 4
        centroid_y = (y1 + y2 + y3 + y4) / 4
        
        element = GeometricElement(name, area, centroid_x, centroid_y, is_positive)
        self.add_element(element)
    
    def add_circle(self, name: str, radius: float, center_x: float, 
                  center_y: float, is_positive: bool = True):
        """Agrega un círculo"""
        area = math.pi * radius**2
        element = GeometricElement(name, area, center_x, center_y, is_positive)
        self.add_element(element)
    
    def add_semicircle(self, name: str, radius: float, center_x: float, 
                      center_y: float, orientation: str = 'up', is_positive: bool = True):
        """Agrega un semicírculo
        orientation: 'up', 'down', 'left', 'right'
        """
        area = (math.pi * radius**2) / 2
        
        # Ajustar centroide según orientación
        if orientation == 'up':
            centroid_y = center_y + (4 * radius) / (3 * math.pi)
            centroid_x = center_x
        elif orientation == 'down':
            centroid_y = center_y - (4 * radius) / (3 * math.pi)
            centroid_x = center_x
        elif orientation == 'right':
            centroid_x = center_x + (4 * radius) / (3 * math.pi)
            centroid_y = center_y
        elif orientation == 'left':
            centroid_x = center_x - (4 * radius) / (3 * math.pi)
            centroid_y = center_y
            
        element = GeometricElement(name, area, centroid_x, centroid_y, is_positive)
        self.add_element(element)
    
    def add_triangle_by_vertices(self, name: str, x1: float, y1: float, 
                                x2: float, y2: float, x3: float, y3: float, 
                                is_positive: bool = True):
        """Agrega un triángulo usando sus 3 vértices (método general)"""
        # Área usando fórmula del determinante
        area = abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2)
        
        # Centroide: promedio de los vértices
        centroid_x = (x1 + x2 + x3) / 3
        centroid_y = (y1 + y2 + y3) / 3
        
        element = GeometricElement(name, area, centroid_x, centroid_y, is_positive)
        self.add_element(element)
    
    def add_custom_element(self, name: str, area: float, centroid_x: float, 
                          centroid_y: float, is_positive: bool = True):
        """Agrega un elemento con área y centroide personalizado"""
        element = GeometricElement(name, area, centroid_x, centroid_y, is_positive)
        self.add_element(element)
    
    def calculate_centroid(self) -> Tuple[float, float]:
        """Calcula el centroide de la figura compuesta"""
        if not self.elements:
            return 0.0, 0.0
        
        sum_area_x = sum(elem.signed_area * elem.centroid_x for elem in self.elements)
        sum_area_y = sum(elem.signed_area * elem.centroid_y for elem in self.elements)
        total_area = sum(elem.signed_area for elem in self.elements)
        
        if total_area == 0:
            raise ValueError("El área total es cero. Revisa los elementos.")
        
        centroid_x = sum_area_x / total_area
        centroid_y = sum_area_y / total_area
        
        return centroid_x, centroid_y
    
    def get_summary_table(self) -> str:
        """Genera una tabla resumen de los cálculos"""
        if not self.elements:
            return "No hay elementos definidos."
        
        # Calcular centroide
        centroid_x, centroid_y = self.calculate_centroid()
        total_area = sum(elem.signed_area for elem in self.elements)
        
        # Crear tabla
        header = f"{'ELEMENTO':<15} {'ÁREA':<10} {'Cx':<8} {'Cy':<8} {'A*Cx':<12} {'A*Cy':<12}"
        separator = "-" * len(header)
        
        lines = [header, separator]
        
        for elem in self.elements:
            area_cx = elem.signed_area * elem.centroid_x
            area_cy = elem.signed_area * elem.centroid_y
            line = f"{elem.name:<15} {elem.signed_area:<10.2f} {elem.centroid_x:<8.2f} {elem.centroid_y:<8.2f} {area_cx:<12.2f} {area_cy:<12.2f}"
            lines.append(line)
        
        lines.append(separator)
        lines.append(f"{'TOTAL':<15} {total_area:<10.2f} {'':<8} {'':<8} {sum(e.signed_area * e.centroid_x for e in self.elements):<12.2f} {sum(e.signed_area * e.centroid_y for e in self.elements):<12.2f}")
        lines.append("")
        lines.append(f"CENTROIDE: X = {centroid_x:.2f}, Y = {centroid_y:.2f}")
        
        return "\n".join(lines)
    
    def plot_elements(self, figsize=(12, 8)):
        """Visualiza los elementos y el centroide"""
        fig, ax = plt.subplots(figsize=figsize)
        
        # Colores para elementos positivos y negativos
        colors = {'positive': 'lightblue', 'negative': 'lightcoral'}
        
        for i, elem in enumerate(self.elements):
            color = colors['positive'] if elem.is_positive else colors['negative']
            
            # Marcar centroide del elemento
            ax.plot(elem.centroid_x, elem.centroid_y, 'o', 
                   color='blue' if elem.is_positive else 'red', 
                   markersize=6, label=f'{elem.name}' if i < 10 else "")
            
            # Agregar texto con nombre del elemento
            ax.annotate(elem.name, (elem.centroid_x, elem.centroid_y), 
                       xytext=(5, 5), textcoords='offset points', fontsize=8)
        
        # Calcular y marcar centroide total
        try:
            centroid_x, centroid_y = self.calculate_centroid()
            ax.plot(centroid_x, centroid_y, 'ks', markersize=10, 
                   label=f'Centroide Total ({centroid_x:.2f}, {centroid_y:.2f})')
        except ValueError as e:
            ax.text(0, 0, f"Error: {e}", fontsize=12, color='red')
        
        ax.grid(True, alpha=0.3)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Elementos Geométricos y Centroide')
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        ax.axis('equal')
        
        plt.tight_layout()
        plt.show()

def ejemplo_figura_con_calculo_automatico():
    """Mismo ejemplo pero usando CÁLCULO AUTOMÁTICO con el sistema correcto de coordenadas"""
    calc = CentroidCalculator()
    
    # SISTEMA DE COORDENADAS CORRECTO: Origen (0,0) en el centro del cuadrado
    
    # 1. CUADRADO PRINCIPAL - C.1v (área=6400, centroide=(0,0))
    # Si área = 6400, entonces lado = √6400 = 80
    #calc.add_rectangle("C.1v_cuadrado", 80, 80, 0, 0, True)

    #Método por coordenadas:
    calc.add_rectangle_by_vertices("C.1v_cuadrado", 
                              -40, -40,  # Vértice inferior izquierdo
                               40, -40,  # Vértice inferior derecho
                               40,  40,  # Vértice superior derecho
                              -40,  40,  # Vértice superior izquierdo
                              True)

    # 2. RECTÁNGULO SUPERIOR - C2C1 (área=3000, centroide=(0,90))
    # Para que el centroide esté en (0,90), necesito determinar dimensiones
    # Si el cuadrado va de -40 a +40 en Y, y el rectángulo está arriba...
    # Asumiendo ancho=80 (mismo que cuadrado), altura = 3000/80 = 37.5
    # Centro en Y=90, entonces va de 90-18.75=71.25 a 90+18.75=108.75
    #calc.add_rectangle("C2C1_rectangulo", 80, 37.5, 0, 90, True)
    calc.add_rectangle_by_vertices("C2C1_rectangulo",
                              -40, 71.25,  # Vértice inferior izquierdo
                               40, 71.25,  # Vértice inferior derecho
                               40, 108.75, # Vértice superior derecho
                              -40, 108.75, # Vértice superior izquierdo
                              True)

    # 3. SEMICÍRCULO - SEMICIRCUNFERENCIA (área=353.43, centroide=(0,144.77))
    # área = π×r²/2 = 353.43, entonces r = √(353.43×2/π) ≈ 15
    # Para semicírculo hacia arriba con centroide en 144.77
    # Centro del semicírculo debe estar en Y = 144.77 - (4×15)/(3×π) ≈ 138.41
    calc.add_semicircle("SEMICIRCUNFERENCIA", 15, 0, 138.41, 'up', True)
    
    # 4. CÍRCULO GRANDE - CIR_MAY (área=1963.5, centroide=(0,0))
    # área = π×r² = 1963.5, entonces r = √(1963.5/π) ≈ 25
    calc.add_circle("CIR_MAY", 25, 0, 0, False)
    
    # 5. CÍRCULO PEQUEÑO - CIR_MENOR (área=201.06, centroide=(0,140))
    # área = π×r² = 201.06, entonces r = √(201.06/π) ≈ 8
    calc.add_circle("CIR_MENOR", 8, 0, 140, False)
    
    # 6. TRIÁNGULOS EN LAS ESQUINAS - MÉTODO CORRECTO usando vértices
    
    # T1v: Esquina superior derecha - corta 10x10 del cuadrado
    # Vértices: (40,40), (30,40), (40,30)
    # Centroide esperado: (36.67, 36.67) ✓
    calc.add_triangle_by_vertices("T1w", -40, 40, -30, 40, -40, 30, False)
    
    # T2z: Esquina inferior derecha
    # Vértices: (40,-40), (30,-40), (40,-30)
    # Centroide esperado: (36.67, -36.67) ✓
    calc.add_triangle_by_vertices("T2z", 40, 40, 30, 40, 40, 30, False)
    
    # T3A1: Esquina superior izquierda  
    # Vértices: (-40,40), (-30,40), (-40,30)
    # Centroide esperado: (-36.67, 36.67) ✓
    calc.add_triangle_by_vertices("T3A1", -40, -40, -30, -40, -40, -30, False)
    
    # T4B1: Esquina inferior izquierda
    # Vértices: (-40,-40), (-30,-40), (-40,-30)  
    # Centroide esperado: (-36.67, -36.67) ✓
    calc.add_triangle_by_vertices("T4B1", 40, -40, 30, -40, 40, -30, False)
    
    return calc

if __name__ == "__main__":
    # Ejecutar ejemplo con cálculo automático
    print("=== MÉTODO 2: CÁLCULO AUTOMÁTICO DE FORMAS ===")
    print("El programa SÍ calcula área y centroide automáticamente")
    calc2 = ejemplo_figura_con_calculo_automatico()
    print(calc2.get_summary_table())
    print("\n")
    
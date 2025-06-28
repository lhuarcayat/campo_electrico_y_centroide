import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp
from scipy.integrate import dblquad
import warnings
warnings.filterwarnings('ignore')

# Configuracion de matplotlib
plt.rcParams['figure.figsize'] = (12, 10)
plt.rcParams['font.size'] = 12

print("=" * 60)
print("PROYECTO 1 - CARGAS ESTATICAS")
print("=" * 60)

# =============================================================================
# PARTE 1: Demostrar que div(E) = 0 para r != 0
# =============================================================================
print("\nPARTE 1: Demostracion de div(E) = 0, para r != 0")
print("-" * 60)
print("\nDivergencia del campo electrico es cero en todo punto excepto en el origen.")

# Definir variables simbolicas
x, y, z, q = sp.symbols('x y z q')
r = sp.sqrt(x**2 + y**2 + z**2)

print("\nSe tiene E(r) = q * r / r^3")
print("\nDonde:")
print("r = x*i + y*j + z*k")
print("r = sqrt(x^2 + y^2 + z^2)")

# Campo electrico E = q * r_vec / r^3
Ex = q * x / r**3
Ey = q * y / r**3
Ez = q * z / r**3

print("\nPor lo tanto:")
print(f"E = q * (x*i/r^3 + y*j/r^3 + z*k/r^3)")
print(f"\nComponentes del campo:")
print(f"Ex = q*x/r^3")
print(f"Ey = q*y/r^3")
print(f"Ez = q*z/r^3")

print("\ndiv(E) = dEx/dx + dEy/dy + dEz/dz ... (I)")

# Calcular derivadas parciales detalladamente
print("\nCalculando cada derivada parcial:")

# dEx/dx
print("\n(a) dEx/dx = d/dx(q*x/r^3)")
print("    Usando la regla del cociente:")
print("    dEx/dx = q * [1/r^3 - x * 3*r^2 * (dr/dx) / r^6]")
print("    Donde dr/dx = x/r")
print("    dEx/dx = q * [1/r^3 - 3*x^2/r^5] ... (alpha)")

div_Ex = sp.diff(Ex, x)
div_Ex_simplified = sp.simplify(div_Ex)

# dEy/dy
print("\n(b) dEy/dy = d/dy(q*y/r^3)")
print("    dEy/dy = q * [1/r^3 - 3*y^2/r^5] ... (beta)")

div_Ey = sp.diff(Ey, y)
div_Ey_simplified = sp.simplify(div_Ey)

# dEz/dz
print("\n(c) dEz/dz = d/dz(q*z/r^3)")
print("    dEz/dz = q * [1/r^3 - 3*z^2/r^5] ... (theta)")

div_Ez = sp.diff(Ez, z)
div_Ez_simplified = sp.simplify(div_Ez)

# Suma total
print("\nSustituyendo (alpha), (beta), (theta) en (I):")
print("\ndiv(E) = q * [3/r^3 - 3(x^2 + y^2 + z^2)/r^5]")
print("       = q * [3/r^3 - 3*r^2/r^5]")
print("       = q * [3/r^3 - 3/r^3]")
print("       = 0")

divergence = sp.simplify(div_Ex + div_Ey + div_Ez)
print(f"\nVerificacion simbolica: div(E) = {divergence}")
print("\nPor lo tanto: div(E) = 0, para todo r != 0")

# =============================================================================
# PARTE 2: Flujo cuando q esta fuera de S
# =============================================================================
print("\n" + "=" * 60)
print("PARTE 2: Demostrar que el flujo saliente de E a traves de S = 0, si q esta fuera de S")
print("-" * 60)

print("\nSea:")
print("- Region T limitada por S no tiene carga q")
print("- E es diferenciable en T")
print("\nPor el Teorema de la Divergencia:")
print("\n  integral_T (div(E)) dV = integral_S E . dS")
print("\nComo div(E) = 0 en todo T (ya que q esta fuera):")
print("\n  integral_S E . dS = 0")
print("\nPor lo tanto: Flujo saliente de E a traves de S = 0")

# =============================================================================
# PARTE 3: Flujo cuando q esta dentro de S
# =============================================================================
print("\n" + "=" * 60)
print("PARTE 3: Flujo cuando q esta dentro de S")
print("-" * 60)

print("\nCuando q esta dentro de S, E no es diferenciable en q, por tanto no se puede")
print("aplicar el teorema de la divergencia directamente en T sino en la")
print("region T', rodeando q con una pequena esfera Sa.")

print("\nSea T' la region entre S y Sa:")
print("\n  integral_T' (div(E)) dV = integral_S E . dS_out + integral_Sa E . dS_in")

print("\nComo div(E) = 0 en T':")
print("\n  0 = flujo saliente de E a traves de S - flujo saliente a traves de Sa")
print("  0 = integral_S E . dS - integral_Sa E . dS")

print("\nPor lo tanto:")
print("  integral_S E . dS = integral_Sa E . dS ... (I)")

print("\nCalculando el flujo a traves de Sa:")
print("\nEn la superficie de Sa de radio a:")
print("  E = q/a^2 * r_hat")
print("  E . dS = q/a^2 ... (II)")

print("\nSustituyendo (II) en (I):")
print("  integral_Sa E . dS = integral_Sa q/a^2 dS")
print("                     = q/a^2 * integral_Sa dS")
print("                     = q/a^2 * 4*pi*a^2")
print("                     = 4*pi*q")

print("\nPor lo tanto:")
print("  integral_S E . dS = 4*pi*q")

# =============================================================================
# Visualizacion del campo electrico
# =============================================================================
print("\n" + "=" * 60)
print("GENERANDO VISUALIZACIONES...")
print("=" * 60)

fig = plt.figure(figsize=(15, 5))

# Subplot 1: Campo en 2D
ax1 = fig.add_subplot(131)
# Crear malla
x_vals = np.linspace(-3, 3, 20)
y_vals = np.linspace(-3, 3, 20)
X, Y = np.meshgrid(x_vals, y_vals)

# Evitar division por cero
R = np.sqrt(X**2 + Y**2)
R[R < 0.1] = 0.1

# Campo electrico (q = 1)
Ex_vals = X / R**3
Ey_vals = Y / R**3

# Normalizar para visualizacion
magnitude = np.sqrt(Ex_vals**2 + Ey_vals**2)
Ex_norm = Ex_vals / (magnitude + 0.1)
Ey_norm = Ey_vals / (magnitude + 0.1)

# Graficar vectores
ax1.quiver(X, Y, Ex_norm, Ey_norm, magnitude, cmap='hot')
ax1.plot(0, 0, 'ro', markersize=10, label='Carga q')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('Campo Electrico E (vista 2D)')
ax1.set_aspect('equal')
ax1.grid(True, alpha=0.3)
ax1.legend()

# Subplot 2: Carga fuera
ax2 = fig.add_subplot(132)

# Definir superficie S (circulo de radio 2 centrado en origen)
theta = np.linspace(0, 2*np.pi, 100)
S_x = 2 * np.cos(theta)
S_y = 2 * np.sin(theta)

# Posicion de la carga (fuera de S)
q_x, q_y = 3.5, 0

# Graficar
ax2.plot(S_x, S_y, 'b-', linewidth=3, label='Superficie S')
ax2.plot(q_x, q_y, 'ro', markersize=10, label='Carga q')
ax2.fill(S_x, S_y, alpha=0.1, color='blue')

# Lineas de campo
angles = np.linspace(0, 2*np.pi, 16)
for angle in angles:
    r_vals = np.linspace(0.1, 5, 50)
    x_line = q_x + r_vals * np.cos(angle)
    y_line = q_y + r_vals * np.sin(angle)
    ax2.plot(x_line, y_line, 'g-', alpha=0.3, linewidth=0.8)

ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('Carga FUERA de S\nFlujo = 0')
ax2.set_aspect('equal')
ax2.set_xlim(-5, 5)
ax2.set_ylim(-5, 5)
ax2.grid(True, alpha=0.3)
ax2.legend()

# Calculo numerico del flujo (carga fuera)
def electric_field_at_point(px, py, qx, qy):
    """Campo electrico en punto (px, py) debido a carga en (qx, qy)"""
    dx = px - qx
    dy = py - qy
    r = np.sqrt(dx**2 + dy**2)
    if r < 0.01:
        return 0, 0
    return dx/r**3, dy/r**3

n_points = 1000
flux_out = 0

for i in range(n_points):
    angle = 2 * np.pi * i / n_points
    px = 2 * np.cos(angle)
    py = 2 * np.sin(angle)
    nx = np.cos(angle)
    ny = np.sin(angle)
    Ex, Ey = electric_field_at_point(px, py, q_x, q_y)
    flux_out += (Ex * nx + Ey * ny) * (2 * np.pi * 2 / n_points)

# Subplot 3: Carga dentro
ax3 = fig.add_subplot(133)

# Carga en el centro
q_x_in, q_y_in = 0, 0

# Graficar
ax3.plot(S_x, S_y, 'b-', linewidth=3, label='Superficie S')
ax3.plot(q_x_in, q_y_in, 'ro', markersize=10, label='Carga q')

# Pequeña esfera Sa
Sa_radius = 0.5
Sa_x = Sa_radius * np.cos(theta)
Sa_y = Sa_radius * np.sin(theta)
ax3.plot(Sa_x, Sa_y, 'r--', linewidth=2, label='Esfera Sa')

# Region T' (sombreada)
ax3.fill(S_x, S_y, alpha=0.1, color='blue')
ax3.fill(Sa_x, Sa_y, alpha=0.2, color='white')

# Anotacion para T'
ax3.text(1.5, 1.5, "T'", fontsize=14, color='black')

# Lineas de campo
for angle in angles:
    r_vals = np.linspace(Sa_radius, 3, 30)
    x_line = q_x_in + r_vals * np.cos(angle)
    y_line = q_y_in + r_vals * np.sin(angle)
    ax3.plot(x_line, y_line, 'g-', alpha=0.5, linewidth=1)
    
    # Flechas
    r_arrow = 1.5
    ax3.arrow(q_x_in + r_arrow*np.cos(angle), 
              q_y_in + r_arrow*np.sin(angle),
              0.2*np.cos(angle), 0.2*np.sin(angle),
              head_width=0.1, head_length=0.1, fc='green', ec='green', alpha=0.7)

ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.set_title('Carga DENTRO de S\nFlujo = 4*pi*q')
ax3.set_aspect('equal')
ax3.set_xlim(-3, 3)
ax3.set_ylim(-3, 3)
ax3.grid(True, alpha=0.3)
ax3.legend()

plt.tight_layout()
plt.savefig('campo_electrico_casos.png', dpi=300, bbox_inches='tight')
plt.show()

# Verificacion numerica del flujo (carga dentro)
flux_in = 0
for i in range(n_points):
    angle = 2 * np.pi * i / n_points
    px = 2 * np.cos(angle)
    py = 2 * np.sin(angle)
    nx = np.cos(angle)
    ny = np.sin(angle)
    Ex, Ey = electric_field_at_point(px, py, q_x_in, q_y_in)
    flux_in += (Ex * nx + Ey * ny) * (2 * np.pi * 2 / n_points)

print("\n" + "=" * 60)
print("VERIFICACION NUMERICA:")
print("=" * 60)
print(f"\nCaso 1 - Flujo numerico (carga fuera): {flux_out:.6f}")
print("         Valor teorico: 0")
print(f"         Error: {abs(flux_out):.6f}")

print(f"\nCaso 2 - Flujo numerico (carga dentro): {flux_in:.6f}")
print(f"         Valor teorico 4*pi = {4*np.pi:.6f}")
print(f"         Error relativo: {abs(flux_in - 4*np.pi)/(4*np.pi)*100:.2f}%")

# =============================================================================
# Visualizacion 3D del campo
# =============================================================================
fig2 = plt.figure(figsize=(12, 5))

# Campo en 3D
ax4 = fig2.add_subplot(121, projection='3d')

# Crear malla 3D dispersa
x3d = np.linspace(-2, 2, 10)
y3d = np.linspace(-2, 2, 10)
z3d = np.linspace(-2, 2, 10)
X3d, Y3d, Z3d = np.meshgrid(x3d, y3d, z3d)

# Campo electrico 3D
R3d = np.sqrt(X3d**2 + Y3d**2 + Z3d**2)
R3d[R3d < 0.1] = 0.1

Ex3d = X3d / R3d**3
Ey3d = Y3d / R3d**3
Ez3d = Z3d / R3d**3

# Normalizar
magnitude3d = np.sqrt(Ex3d**2 + Ey3d**2 + Ez3d**2)
scale = 0.5
Ex3d_norm = scale * Ex3d / (magnitude3d + 0.1)
Ey3d_norm = scale * Ey3d / (magnitude3d + 0.1)
Ez3d_norm = scale * Ez3d / (magnitude3d + 0.1)

# Graficar vectores 3D (submuestra)
skip = 2
ax4.quiver(X3d[::skip,::skip,::skip], Y3d[::skip,::skip,::skip], Z3d[::skip,::skip,::skip],
           Ex3d_norm[::skip,::skip,::skip], Ey3d_norm[::skip,::skip,::skip], Ez3d_norm[::skip,::skip,::skip],
           length=0.1, normalize=False, color='blue', alpha=0.6)

# Carga
ax4.scatter([0], [0], [0], color='red', s=100, label='Carga q')
ax4.set_xlabel('X')
ax4.set_ylabel('Y')
ax4.set_zlabel('Z')
ax4.set_title('Campo Electrico 3D')
ax4.legend()

# Superficies equipotenciales
ax5 = fig2.add_subplot(122, projection='3d')

# Crear superficie esferica
u = np.linspace(0, 2 * np.pi, 50)
v = np.linspace(0, np.pi, 50)
radii = [0.5, 1.0, 1.5, 2.0]

for r in radii:
    x_sphere = r * np.outer(np.cos(u), np.sin(v))
    y_sphere = r * np.outer(np.sin(u), np.sin(v))
    z_sphere = r * np.outer(np.ones(np.size(u)), np.cos(v))
    
    # Potencial V = q/r
    potential = 1/r
    
    ax5.plot_surface(x_sphere, y_sphere, z_sphere, alpha=0.3, 
                     color=plt.cm.coolwarm(potential/2))

ax5.scatter([0], [0], [0], color='red', s=100, label='Carga q')
ax5.set_xlabel('X')
ax5.set_ylabel('Y')
ax5.set_zlabel('Z')
ax5.set_title('Superficies Equipotenciales\nV = q/r')
ax5.legend()

plt.tight_layout()
plt.savefig('campo_3d_equipotenciales.png', dpi=300, bbox_inches='tight')
plt.show()

print("\n" + "=" * 60)
print("RESUMEN DE RESULTADOS:")
print("=" * 60)
print("1. PARTE 1: div(E) = 0 para r != 0 (demostrado simbolica y analiticamente)")
print("2. PARTE 2: Flujo = 0 cuando q esta fuera de S (teorema de divergencia)")
print("3. PARTE 3: Flujo = 4*pi*q cuando q esta dentro de S (Ley de Gauss)")
print("\nTodas las demostraciones completadas exitosamente!")
print("=" * 60)
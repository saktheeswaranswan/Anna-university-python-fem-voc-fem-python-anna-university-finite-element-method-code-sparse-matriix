# -*- coding: utf-8 -*-
"""anna-university voc fem python codedd 11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PPKusCVsDny9bTXu2Z6K2ioNOe1CNCpT
"""

!pip install sympy

import sympy as sp

# Define symbolic variables
EI, l, ξ = sp.symbols('EI l ξ')

# Define the shape functions matrix Be
Be = sp.Matrix([[6*ξ, (3*ξ-1)*l, -6*ξ, (3*ξ+1)*l]]) / l**2

# Compute the stiffness matrix Ke
Ke = (EI*l/2) * sp.integrate(Be.T @ Be, (ξ, -1, 1))
Ke = sp.simplify(Ke)

# Print Ke for prismatic beam
print("Ke for prismatic beam:")
sp.pprint(Ke, use_unicode=True)

# Print Ke in Python format
print("\nKe in Python format:")
print(sp.python(Ke))

import sympy as sp

# Define symbolic variables
q, l, ξ = sp.symbols('q l ξ')

# Define the shape functions matrix Ne
Ne = sp.Matrix([
    [2*(1-ξ)**2*(2+ξ), (1-ξ)**2*(1+ξ)*l, 2*(1+ξ)**2*(2-ξ), -(1+ξ)**2*(1-ξ)*l]
]) / 8

# Compute the equivalent nodal forces fe
fe = (q*l/2) * sp.integrate(Ne, (ξ, -1, 1))
fe = sp.simplify(fe)

# Print fe^T for uniform load q
print("fe^T for uniform load q:")
sp.pprint(fe, use_unicode=True)

import numpy as np

def TimoshenkoBeamStiffness(Le, EI, Φ):
    Ke = EI / (Le * (1 + Φ)) * np.array([
        [12 / Le**2, 6 / Le, -12 / Le**2, 6 / Le],
        [6 / Le, 4 + Φ, -6 / Le, 2 - Φ],
        [-12 / Le**2, -6 / Le, 12 / Le**2, -6 / Le],
        [6 / Le, 2 - Φ, -6 / Le, 4 + Φ]
    ])
    return Ke
    # Define inputs
Le = 5.0  # Example value for length
EI = 10.0  # Example value for bending stiffness
Φ = 0.2  # Example value for Φ

# Calculate the stiffness matrix
Ke = TimoshenkoBeamStiffness(Le, EI, Φ)

# Print the stiffness matrix
print("Stiffness Matrix Ke:")
print(Ke)

import numpy as np

def TimoshenkoWinklerStiffness(Le, kF, Φ):
    KeW = np.array([
        [4*(78+147*Φ+70*Φ**2), Le*(44+77*Φ+35*Φ**2), 4*(27+63*Φ+35*Φ**2), -Le*(26+63*Φ+35*Φ**2)],
        [Le*(44+77*Φ+35*Φ**2), Le**2*(8+14*Φ+7*Φ**2), Le*(26+63*Φ+35*Φ**2), -Le**2*(6+14*Φ+7*Φ**2)],
        [4*(27+63*Φ+35*Φ**2), Le*(26+63*Φ+35*Φ**2), 4*(78+147*Φ+70*Φ**2), -Le*(44+77*Φ+35*Φ**2)],
        [-Le*(26+63*Φ+35*Φ**2), -Le**2*(6+14*Φ+7*Φ**2), -Le*(44+77*Φ+35*Φ**2), Le**2*(8+14*Φ+7*Φ**2)]
    ]) * kF * Le / (840 * (1 + Φ)**2)
    return KeW
# Define inputs
Le = 5.0  # Example value for length
kF = 1000.0  # Example value for foundation stiffness
Φ = 0.2  # Example value for Φ

# Calculate the stiffness matrix
KeW = TimoshenkoWinklerStiffness(Le, kF, Φ)

# Print the stiffness matrix
print("Stiffness Matrix KeW:")
print(KeW)

#Here's the equivalent Python code for the TimoshenkoWinklerStiffness function using NumPy

#Make sure to replace the example values with the actual values you want to use. This code snippet calculates the stiffness matrix KeW and prints it to the console.

import sympy as sp

# Define symbolic variables
EI, kF, Le, χ, q0, x = sp.symbols('EI kF Le χ q0 x')
g = 2 - sp.cos(2*χ) - sp.cosh(2*χ)

Nf = [
    sp.exp(χ*x/Le) * sp.sin(χ*x/Le),
    sp.exp(χ*x/Le) * sp.cos(χ*x/Le),
    sp.exp(-χ*x/Le) * sp.sin(χ*x/Le),
    sp.exp(-χ*x/Le) * sp.cos(χ*x/Le)
]

Nfd = [sp.diff(N, x) for N in Nf]
Nfdd = [sp.diff(N, x) for N in Nfd]

KgF = kF * sp.integrate(sp.Matrix(Nf).T @ sp.Matrix(Nf), (x, 0, Le))
KgB = EI * sp.integrate(sp.Matrix(Nfdd).T @ sp.Matrix(Nfdd), (x, 0, Le))
fg = q0 * sp.integrate(sp.Matrix(Nf), (x, 0, Le))

KgF, KgB, fg = [sp.simplify(mat) for mat in [KgF, KgB, fg]]

print("KgF=")
sp.pprint(KgF, use_unicode=True)
print("KgB=")
sp.pprint(KgB, use_unicode=True)

GF = [N.subs(x, 0) for N in Nf] + [N.subs(x, Le) for N in Nf]
HF = sp.Matrix([[sp.simplify(1/GFij) for GFij in GF]])
HFT = HF.T

print("GF=")
sp.pprint(GF, use_unicode=True)
print("HF=")
sp.pprint(HF, use_unicode=True)

facB = (EI*χ/Le**3) / (4*g**2)
facF = (kF*Le) / (16*χ**3*g**2)

KeB = HFT @ KgB @ HF
KeBfac = sp.simplify(KeB / facB)

print("KeB =", facB, " * ")
sp.pprint(KeBfac, use_unicode=True)

KeF = HFT @ KgF @ HF
KeFfac = sp.simplify(KeF / facF)

print("KeF =", facF, " * ")
sp.pprint(KeFfac, use_unicode=True)

facf = (q0*Le) / (χ**2*g)
# Transpose fg to make it a column vector
fg = sp.Matrix(fg).T
fe = sp.simplify(HFT @ fg)
fefac = sp.simplify(fe / facf)

print("fe =", facf, " * ")
sp.pprint(fefac, use_unicode=True)

import sympy as sp

def BEBeamWinklerExactStiffness(Le, EI, kF, q0):
    χ = sp.expand(Le * ((kF / (4 * EI))**(1/4)))

    B1 = 2*χ**2*(-4*sp.sin(2*χ) + sp.sin(4*χ) + 4*sp.sin(χ)*(sp.cos(χ)*sp.cosh(2*χ) +
        8*χ*sp.sin(χ)*sp.sinh(χ)**2) + 2*(sp.cos(2*χ) - 2)*sp.sinh(2*χ) + sp.sinh(4*χ))

    B2 = 2*Le*χ*(4*sp.cos(2*χ) - sp.cos(4*χ) - 4*sp.cosh(2*χ) + sp.cosh(4*χ) -
        8*χ*sp.sin(2*χ)*sp.sinh(χ)**2 + 8*χ*sp.sin(χ)**2*sp.sinh(2*χ))

    B3 = -Le**2*(8*χ*sp.cos(2*χ) - 12*sp.sin(2*χ) + sp.cosh(2*χ)*(6*sp.sin(2*χ) - 8*χ) +
        3*sp.sin(4*χ) + 2*(6 - 3*sp.cos(2*χ) + 4*χ*sp.sin(2*χ))*sp.sinh(2*χ) - 3*sp.sinh(4*χ))

    B4 = -4*Le*χ*(χ*sp.cosh(3*χ)*sp.sin(χ) - χ*sp.cosh(χ)*(-2*sp.sin(χ) + sp.sin(3*χ)) +
        (χ*(sp.cos(χ) + sp.cos(3*χ)) + sp.cosh(2*χ)*(-2*χ*sp.cos(χ) + 4*sp.sin(χ)) +
         2*(-5*sp.sin(χ) + sp.sin(3*χ)))*sp.sinh(χ))

    B5 = -4*χ**2*(2*sp.cos(χ)*(-2 + sp.cos(2*χ) + sp.cosh(2*χ))*sp.sinh(χ) +
        sp.sin(3*χ)*(sp.cosh(χ) - 2*χ*sp.sinh(χ)) +
        sp.sin(χ)*(-4*sp.cosh(χ) + sp.cosh(3*χ) + 2*χ*sp.sinh(3*χ)))

    B6 = 2*Le**2*(sp.cosh(3*χ)*(-2*χ*sp.cos(χ) + 3*sp.sin(χ)) +
        sp.cosh(χ)*(2*χ*sp.cos(3*χ) + 3*(sp.sin(3*χ) - 4*sp.sin(χ))) +
        (9*sp.cos(χ) - 3*sp.cos(3*χ) - 6*sp.cos(χ)*sp.cosh(2*χ) + 16*χ*sp.sin(χ))*sp.sinh(χ))

    F1 = 2*χ**2*(-32*χ*sp.sin(χ)**2*sp.sinh(χ)**2 + 6*(-2 + sp.cos(2*χ)) *
        (sp.sin(2*χ) + sp.sinh(2*χ)) + 6*sp.cosh(2*χ)*(sp.sin(2*χ) + sp.sinh(2*χ)))

    F2 = 2*Le*χ*(4*sp.cos(2*χ) - sp.cos(4*χ) - 4*sp.cosh(2*χ) + sp.cosh(4*χ) +
        8*χ*sp.sin(2*χ)*sp.sinh(χ)**2 - 8*χ*sp.sin(χ)**2*sp.sinh(2*χ))

    F3 = Le**2*(8*χ*sp.cos(2*χ) + 4*sp.sin(2*χ) - 2*sp.cosh(2*χ)*(4*χ + sp.sin(2*χ)) +
        sp.sin(4*χ) + 2*(sp.cos(2*χ) + 4*χ*sp.sin(2*χ) - 2)*sp.sinh(2*χ) + sp.sinh(4*χ))

    F4 = 4*Le*χ*(χ*sp.cosh(3*χ)*sp.sin(χ) - χ*sp.cosh(χ)*(-2*sp.sin(χ) + sp.sin(3*χ)) +
        (χ*sp.cos(χ) + χ*sp.cos(3*χ) + 10*sp.sin(χ) - 2*sp.cosh(2*χ)*(χ*sp.cos(χ) + 2*sp.sin(χ)) +
         2*sp.sin(3*χ))*sp.sinh(χ))

    F5 = -4*χ**2*(6*sp.cos(χ)*(-2 + sp.cos(2*χ) + sp.cosh(2*χ))*sp.sinh(χ) +
        sp.sin(3*χ)*(3*sp.cosh(χ) + 2*χ*sp.sin(χ)) +
        sp.sin(χ)*(-12*sp.cosh(χ) + 3*sp.cosh(3*χ) - 2*χ*sp.sinh(3*χ)))

    F6 = -2*Le**2*(-(sp.cosh(3*χ)*(2*χ*sp.cos(χ) + sp.sin(χ))) +
        sp.cosh(χ)*(2*χ*sp.cos(3*χ) + 4*sp.sin(χ) - sp.sin(3*χ)) +
        (sp.cos(3*χ) + sp.cos(χ)*(2*sp.cosh(2*χ) - 3) + 16*χ*sp.sin(χ))*sp.sinh(χ))

    f1 = 2*χ*(sp.cosh(χ) - sp.cos(χ))*(sp.sin(χ) - sp.sinh(χ))
    f2 = -(Le*(sp.sin(χ) - sp.sinh(χ))**2)
    g = 2 - sp.cos(2*χ) - sp.cosh(2*χ)
    facf = (q0*Le) / (χ**2*g)
    facB = (EI*χ/Le**3) / (4*g**2)
    facF = (kF*Le) / (16*χ**3*g**2)

    KeB = facB * sp.Matrix([[B1, B2, B5, -B4], [B2, B3, B4, B6], [B5, B4, B1, -B2], [-B4, B6, -B2, B3]])
    KeF = facF * sp.Matrix([[F1, F2, F5, -F4], [F2, F3, F4, F6], [F5, F4, F1, -F2], [-F4, F6, -F2, F3]])
    fe = facf * sp.Matrix([f1, f2, f1, -f2])

    return [KeB, KeF, fe]

import sympy as sp

# Define symbolic variables
Le, EI, kF, q0 = sp.symbols('Le EI kF q0')

# Define values for the two load cases
# Load case (I): Central Point Load
Le_I = 5.0  # Example value for length
EI_I = 10.0  # Example value for bending stiffness
kF_I = 1000.0  # Example value for foundation stiffness
q0_I = 100.0  # Example value for load magnitude (central point load)

# Load case (II): Line Load Over Right H
Le_II = 5.0  # Example value for length
EI_II = 10.0  # Example value for bending stiffness
kF_II = 1000.0  # Example value for foundation stiffness
q0_II = 200.0  # Example value for load magnitude (line load over right H)

# Calculate stiffness matrices and consistent force vectors for both load cases
KeB_I, KeF_I, fe_I = BEBeamWinklerExactStiffness(Le_I, EI_I, kF_I, q0_I)
KeB_II, KeF_II, fe_II = BEBeamWinklerExactStiffness(Le_II, EI_II, kF_II, q0_II)

# Print results for Load case (I): Central Point Load
print("Load case (I): Central Point Load")
print("KeB_I:")
sp.pprint(KeB_I, use_unicode=True)
print("KeF_I:")
sp.pprint(KeF_I, use_unicode=True)
print("fe_I:")
sp.pprint(fe_I, use_unicode=True)

# Print results for Load case (II): Line Load Over Right H
print("\nLoad case (II): Line Load Over Right H")
print("KeB_II:")
sp.pprint(KeB_II, use_unicode=True)
print("KeF_II:")
sp.pprint(KeF_II, use_unicode=True)
print("fe_II:")
sp.pprint(fe_II, use_unicode=True)

import sympy as sp
import numpy as np
from tabulate import tabulate

# Define symbolic variables
Le, EI, kF, q0 = sp.symbols('Le EI kF q0')

# Define values for the two load cases
# Load case (I): Central Point Load
Le_I = 5.0  # Example value for length
EI_I = 10.0  # Example value for bending stiffness
kF_I = 1000.0  # Example value for foundation stiffness
q0_I = 100.0  # Example value for load magnitude (central point load)

# Load case (II): Line Load Over Right H
Le_II = 5.0  # Example value for length
EI_II = 10.0  # Example value for bending stiffness
kF_II = 1000.0  # Example value for foundation stiffness
q0_II = 200.0  # Example value for load magnitude (line load over right H)

# Define values of λ and Ne
lambda_values = [2, 4, 8]
Ne_values = [2, 4, 8]

# Initialize a table to store the results
table = []

# Loop through λ and Ne values
for λ in lambda_values:
    for Ne in Ne_values:
        # Calculate stiffness matrices and consistent force vectors for Load case (I)
        KeB_I, KeF_I, fe_I = BEBeamWinklerExactStiffness(Le_I, EI_I, kF_I, q0_I)

        # Calculate stiffness matrices and consistent force vectors for Load case (II)
        KeB_II, KeF_II, fe_II = BEBeamWinklerExactStiffness(Le_II, EI_II, kF_II, q0_II)

        # Convert the symbolic matrices to NumPy arrays
        KeB_I_np = np.array(KeB_I, dtype=float)
        KeB_II_np = np.array(KeB_II, dtype=float)

        # Calculate the condition numbers using NumPy
        CI_I = np.linalg.cond(KeB_I_np)
        CI_II = np.linalg.cond(KeB_II_np)

        # Append the results to the table
        table.append(["Load case (I): Central Point Load", λ, Ne, CI_I])
        table.append(["Load case (II): Line Load Over Right Half", λ, Ne, CI_II])

# Print the table using the tabulate library
headers = ["Load Case", "λ", "Ne", "Exact CI"]
print(tabulate(table, headers, tablefmt="grid"))

import sympy as sp

# Define symbolic variables
Le, EI, Φ, q0, fx2, fy2, m2, x = sp.symbols('Le EI Φ q0 fx2 fy2 m2 x')

# Define the equations
GAs = 12 * EI / (Φ * Le**2)
F = fx2
V = -fy2 - q0 * (Le - x)
M = m2 + fy2 * (Le - x) + (1/2) * q0 * (Le - x)**2

# Check dM/dx = V
check_equation = sp.simplify(sp.diff(M, x) - V)

# Define the strain energy
Ucd = F**2 / (2 * EI) + M**2 / (2 * EI) + V**2 / (2 * GAs)

# Integrate to find total strain energy Uc
Uc = sp.integrate(Ucd, (x, 0, Le))

# Differentiate Uc with respect to the variables
u2 = sp.diff(Uc, fx2)
v2 = sp.diff(Uc, fy2)
θ2 = sp.diff(Uc, m2)

# Create the flexibility matrix Frr
Frr = sp.Matrix([[u2, 0, 0],
                 [0, v2, 0],
                 [0, 0, θ2]])

# Define br vector and substitute values
br = sp.Matrix([sp.diff(Uc, fx2), sp.diff(Uc, fy2), sp.diff(Uc, m2)])
br = br.subs({fx2: 0, fy2: 0, m2: 0})

# Calculate Krr (stiffness matrix)
try:
    Krr = Frr.inv()
except sp.MatrixError:
    print("Matrix is not invertible. Check your equations and substitutions.")

# Calculate qr (consistent load vector)
qr = -Krr * br

# Define transformation matrices TT, GrT, and GqT
TT = sp.Matrix([[-1, 0, 0], [0, -1, 0], [0, -Le, -1], [1, 0, 0], [0, 1, 0], [0, 0, 1]])
GrT = sp.Matrix([[1, 0, 0], [0, 1, 0], [0, Le, 1]])
GqT = sp.Matrix([[1, 0, 0], [0, 1, 0], [0, Le/2, 1]])

# Calculate Ke (element stiffness matrix)
Ke = TT * Krr * TT.T

# Define Gr and Gq matrices
Gr = GrT.T
Gq = GqT.T

# Define qv vector
qv = sp.Matrix([0, q0 * Le, 0])

# Calculate qs (consistent nodal forces)
qs = -GrT * qr - GqT * qv

# Print the results
print("check dM/dx = V:", check_equation)
print("Uc =", Uc)
print("br =", br)
print("Frr =", Frr)
if Krr is not None:
    print("Krr =", Krr)
else:
    print("Krr could not be calculated due to singularity.")
print("qr =", qr)
print("Ke =", Ke)
print("Gr =", Gr)
print("Gq =", Gq)
print("qs =", qs)

# Implementation of Turner triangle stiffness matrix calculation Three-Node
#Plane Stress
#Triangles

import numpy as np
import sympy as sp

def TurnerMembraneStiffness(ncoor, Emat, h, numer=True):
    x1, y1 = ncoor[0]
    x2, y2 = ncoor[1]
    x3, y3 = ncoor[2]

    A = sp.Rational(x2*y3 - x3*y2 + x3*y1 - x1*y3 + x1*y2 - x2*y1, 2)

    x21, x32, x13 = x2 - x1, x3 - x2, x1 - x3
    y12, y23, y31 = y1 - y2, y2 - y3, y3 - y1

    Be = np.array([[y23, 0, y31, 0, y12, 0],
                   [0, x32, 0, x13, 0, x21],
                   [x32, y23, x13, y31, x21, y12]]) / (2 * A)

    if numer:
        Be = np.array(Be, dtype=float)

    Ke = A * h * np.dot(np.transpose(Be), np.dot(Emat, Be))

    return Ke

# Example usage:
ncoor = [(0, 0), (1, 0), (0, 1)]
Emat = np.eye(3)  # Example elasticity matrix, modify as needed
h = 1.0  # Example thickness
numer = True  # Set to False if you want symbolic result

Ke = TurnerMembraneStiffness(ncoor, Emat, h, numer)
print("Stiffness Matrix:")
print(Ke)

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Define the TurnerMembraneStiffness function (as previously shown)

# Define the coordinates and Emat
ncoor = [(0, 0), (3, 1), (2, 2)]
Emat = 8 * np.array([[8, 2, 0], [2, 8, 0], [0, 0, 3]])
h = 1.0
numer = False

Ke = TurnerMembraneStiffness(ncoor, Emat, h, numer)
print("Ke=")
print(Ke)

# Calculate eigenvalues of Ke using SymPy
eigenvalues = sp.Matrix(Ke).eigenvals()
eigenvalues = [float(val.evalf()) for val in eigenvalues]
print("eigs of Ke=")
print(eigenvalues)

# Plot the triangle
triangle = np.array(ncoor + [ncoor[0]])
x, y = triangle[:, 0], triangle[:, 1]

plt.figure(figsize=(8, 6))
plt.plot(x, y, 'r-', linewidth=2)
plt.fill(x, y, 'r', alpha=0.2)
plt.xlim(-1, 4)
plt.ylim(-1, 3)
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Triangle Plot')
plt.grid(True)

plt.show()

import numpy as np
import sympy as sp

def VeubekeMembraneStiffness(ncoor, Emat, h, numer=True):
    x1, y1 = ncoor[0]
    x2, y2 = ncoor[1]
    x3, y3 = ncoor[2]

    A = sp.Rational(x2*y3 - x3*y2 + x3*y1 - x1*y3 + x1*y2 - x2*y1, 2)

    x12, x23, x31 = x1 - x2, x2 - x3, x3 - x1
    y21, y32, y13 = y2 - y1, y3 - y2, y1 - y3

    Be = np.array([[y21, 0, y32, 0, y13, 0],
                   [0, x12, 0, x23, 0, x31],
                   [x12, y21, x23, y32, x31, y13]]) / A

    if numer:
        Be = np.array(Be, dtype=float)

    Ke = A * h * np.dot(np.transpose(Be), np.dot(Emat, Be))

    return Ke

# Example usage:
ncoor = [(0, 0), (3, 1), (2, 2)]
Emat = 8 * np.array([[8, 2, 0], [2, 8, 0], [0, 0, 3]])
h = 1.0
numer = False  # Set to True if you want numeric result

Ke = VeubekeMembraneStiffness(ncoor, Emat, h, numer)
print("Veubeke Stiffness Matrix:")
print(Ke)

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Define the VeubekeMembraneStiffness function (as previously shown)

# Define the coordinates and Emat
ncoor = [(0, 0), (3, 1), (2, 2)]
Emat = 8 * np.array([[8, 2, 0], [2, 8, 0], [0, 0, 3]])
h = 1.0
numer = False

Ke = VeubekeMembraneStiffness(ncoor, Emat, h, numer)
print("Veubeke Stiffness Matrix:")
print(Ke)

# Calculate eigenvalues of Ke using SymPy
eigenvalues = sp.Matrix(Ke).eigenvals()
eigenvalues = [float(val.evalf()) for val in eigenvalues]
print("eigs of Ke=")
print(eigenvalues)

# Plot the triangle
triangle = np.array(ncoor + [ncoor[0]])
x, y = triangle[:, 0], triangle[:, 1]

plt.figure(figsize=(8, 6))
plt.plot(x, y, 'r-', linewidth=2)
plt.fill(x, y, 'r', alpha=0.2)
plt.xlim(-1, 4)
plt.ylim(-1, 3)
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Triangle Plot')
plt.grid(True)

plt.show()

import numpy as np
import sympy as sp

# Define the VeubekeMembraneStiffness function (as previously shown)

# Define the coordinates and Emat
ncoor = [(0, 0), (3, 1), (2, 2)]
Emat = 8 * np.array([[8, 2, 0], [2, 8, 0], [0, 0, 3]])
h = 1.0
numer = False

Ke = VeubekeMembraneStiffness(ncoor, Emat, h, numer)
print("Ke=")
print(Ke)

# Calculate eigenvalues of Ke using SymPy
eigenvalues = sp.Matrix(Ke).eigenvals()
eigenvalues = [float(val.evalf()) for val in eigenvalues]
print("eigs of Ke=")
print(eigenvalues)

#Isoparametric Quadrilaterals elements

import numpy as np

def Quad4IsoPShapeFunDer(ncoor, qcoor):
    ξ, η = qcoor
    Nf = np.array([(1 - ξ) * (1 - η), (1 + ξ) * (1 - η), (1 + ξ) * (1 + η), (1 - ξ) * (1 + η)]) / 4
    dNξ = np.array([-(1 - η), (1 - η), (1 + η), -(1 + η)]) / 4
    dNη = np.array([-(1 - ξ), -(1 + ξ), (1 + ξ), (1 - ξ)]) / 4

    x = [ncoor[i][0] for i in range(4)]
    y = [ncoor[i][1] for i in range(4)]

    J11 = np.dot(dNξ, x)
    J12 = np.dot(dNξ, y)
    J21 = np.dot(dNη, x)
    J22 = np.dot(dNη, y)

    Jdet = J11 * J22 - J12 * J21

    dNx = (J22 * dNξ - J12 * dNη) / Jdet
    dNy = (-J21 * dNξ + J11 * dNη) / Jdet

    return [Nf, dNx, dNy, Jdet]

import sympy as sp

def line_gauss_rule_info(rule, point, numer=False):
    g2 = [-1/sp.sqrt(3), 1/sp.sqrt(3)]
    w3 = [5/9, 8/9, 5/9]
    g3 = [-sp.sqrt(3/5), 0, sp.sqrt(3/5)]
    w4 = [(1/2)-sp.sqrt(5/6)/6, (1/2)+sp.sqrt(5/6)/6, (1/2)+sp.sqrt(5/6)/6, (1/2)-sp.sqrt(5/6)/6]
    g4 = [-sp.sqrt((3+2*sp.sqrt(6/5))/7), -sp.sqrt((3-2*sp.sqrt(6/5))/7),
          sp.sqrt((3-2*sp.sqrt(6/5))/7), sp.sqrt((3+2*sp.sqrt(6/5))/7)]
    g5 = [-sp.sqrt(5+2*sp.sqrt(10/7))/3, -sp.sqrt(5-2*sp.sqrt(10/7))/3, 0,
          sp.sqrt(5-2*sp.sqrt(10/7))/3, sp.sqrt(5+2*sp.sqrt(10/7))/3]
    w5 = [(322-13*sp.sqrt(70))/900, (322+13*sp.sqrt(70))/900, 512/900, (322+13*sp.sqrt(70))/900, (322-13*sp.sqrt(70))/900]

    i = point
    p = rule
    info = [[None, None], 0]

    if p == 1:
        info = [0, 2]
    if p == 2:
        info = [g2[i], 1]
    if p == 3:
        info = [g3[i], w3[i]]
    if p == 4:
        info = [g4[i], w4[i]]
    if p == 5:
        info = [g5[i], w5[i]]

    if numer:
        return [sp.N(val) for val in info]
    else:
        return info

# Example usage to get the first five one-dimensional Gauss rules for point 2 and rule 3 (G3)
result = line_gauss_rule_info(3, 2)
print(result)

import numpy as np

def Quad4IsoPShapeFunDer(ncoor, qcoor):
  """
  A shape function module for the 4-node bilinear quadrilateral.

  Args:
    ncoor: The nodal coordinates of the quadrilateral.
    qcoor: The natural coordinates of the quadrilateral.

  Returns:
    A list of 4 shape functions, their derivatives in the x-direction,
    their derivatives in the y-direction, and the determinant of the Jacobian.
  """

  ξ, η = qcoor

  Nf = [(1 - ξ)*(1 - η), (1 + ξ)*(1 - η), (1 + ξ)*(1 + η), (1 - ξ)*(1 + η)] / 4
  dNξ = [(-(1 - η), (1 - η), (1 + η), -(1 + η))] / 4
  dNη = [(-(1 - ξ), -(1 + ξ), (1 + ξ), (1 - ξ))] / 4

  x = [ncoor[i][0] for i in range(4)]
  y = [ncoor[i][1] for i in range(4)]

  J11 = np.dot(dNξ, x)
  J12 = np.dot(dNξ, y)
  J21 = np.dot(dNη, x)
  J22 = np.dot(dNη, y)

  Jdet = J11 * J22 - J12 * J21

  dNx = (J22 * dNξ - J12 * dNη) / Jdet
  dNy = (-J21 * dNξ + J11 * dNη) / Jdet

  return [Nf, dNx, dNy, Jdet]

def QuadGaussRuleInfo(rule, numer, point):
  """
  A Mathematica module that returns the first five one-dimensional Gauss rules
  or two-dimensional product Gauss rules.

  Args:
    rule: The Gauss rule to use.
    numer: Whether to return the numerical values of the rule or their symbolic expressions.
    point: The point at which to evaluate the rule.

  Returns:
    A list containing the Gauss point and weight.
  """

  if len(rule) == 2:
    p1, p2 = rule
  else:
    p1 = p2 = rule

  if p1 < 0:
    return QuadNonProductGaussRuleInfo([-p1, numer], point)

  if len(point) == 2:
    i, j = point
    m = point
  else:
    i, j = Floor((m - 1) / p1) + 1, m - p1 * (j - 1)

  ξ, w1 = LineGaussRuleInfo([p1, numer], i)
  η, w2 = LineGaussRuleInfo([p2, numer], j)

  info = [(ξ, η), w1 * w2]

  if numer:
    return np.array(info)
  else:
    return simplify(info)

def Quad4IsoPMembraneStiffness(ncoor, Emat, thick, options):
  """
  Compute the stiffness matrix of a 4-node bilinear
quadrilateral in plane stress.

  Args:
    ncoor: The nodal coordinates of the quadrilateral.
    Emat: The elasticity matrix.
    thick: The thickness of the plate.
    options: A list of options.

  Returns:
    The stiffness matrix.
  """

  if len(options) == 2:
    numer, p = options
  else:
    numer = False
    p = 2

  Ke = np.zeros((8, 8))

  for k in range(1, p * p + 1):
    qcoor, w = QuadGaussRuleInfo([p, numer], k)
    Nf, dNx, dNy, Jdet = Quad4Iso

print(Ke)

import numpy as np

def PlaneBar2Stiffness(ncoor, Em, A, options):
    x1, y1 = ncoor[0]
    x2, y2 = ncoor[1]
    x21, y21 = x2 - x1, y2 - y1
    EA = Em * A
    numer = options[0]

    if not numer:
        L = np.sqrt(x21**2 + y21**2)
    else:
        x21, y21, EA, L = map(float, [x21, y21, EA, np.sqrt(x21**2 + y21**2)])

    LLL = x21**2 * y21**2
    Ke = (EA / LLL) * np.array([
        [x21**2, x21*y21, -x21**2, -x21*y21],
        [y21*x21, y21**2, -y21*x21, -y21**2],
        [-x21**2, -x21*y21, x21**2, x21*y21],
        [-y21*x21, -y21**2, y21*x21, y21**2]
    ])

    return Ke

# Example usage
ncoor = [[0, 0], [1, 1]]
Em = 200e9  # Young's modulus
A = 0.01   # Cross-sectional area
options = [False]  # Set to True for numerical values

result = PlaneBar2Stiffness(ncoor, Em, A, options)
print(result)

# Implementation of
One-Dimensional
Elements beam

import numpy as np
from scipy.linalg import eigh

def PlaneBar2Stiffness(ncoor, Em, A, options):
    x1, y1 = ncoor[0]
    x2, y2 = ncoor[1]
    x21, y21 = x2 - x1, y2 - y1
    EA = Em * A
    numer = options[0]

    if not numer:
        L = np.sqrt(x21**2 + y21**2)
    else:
        x21, y21, EA, L = map(float, [x21, y21, EA, np.sqrt(x21**2 + y21**2)])

    LLL = x21**2 * y21**2
    Ke = (EA / LLL) * np.array([
        [x21**2, x21*y21, -x21**2, -x21*y21],
        [y21*x21, y21**2, -y21*x21, -y21**2],
        [-x21**2, -x21*y21, x21**2, x21*y21],
        [-y21*x21, -y21**2, y21*x21, y21**2]
    ])

    return Ke

# Example usage
ncoor = [[0, 0], [30, 40]]
Em = 1000  # Young's modulus
A = 5      # Cross-sectional area
options = [True]  # Set to True for numerical values

Ke = PlaneBar2Stiffness(ncoor, Em, A, options)

print("Numerical Elem Stiff Matrix: ")
print(Ke)
print("Eigenvalues of Ke =", np.linalg.eigvals(Ke))
print("Symmetry check =", np.allclose(Ke, Ke.T))

import numpy as np

def PlaneBar2Stiffness(ncoor, Em, A, options):
    x1, y1 = ncoor[0]
    x2, y2 = ncoor[1]
    x21, y21 = x2 - x1, y2 - y1
    EA = Em * A
    numer = options[0]
    LL = x21**2 + y21**2
    L = np.sqrt(LL)

    if numer:
        x21, y21, EA, LL, L = np.array([x21, y21, EA, LL, L], dtype=float)

    if not numer:
        L = np.power(L, L)

    LLL = LL * L
    Ke = (EA / LLL) * np.array([
        [x21**2, x21 * y21, -x21**2, -x21 * y21],
        [y21 * x21, y21**2, -y21 * x21, -y21**2],
        [-x21**2, -x21 * y21, x21**2, x21 * y21],
        [-y21 * x21, -y21**2, y21 * x21, y21**2]
    ])

    return Ke

ncoor = np.array([[0, 0], [30, 40]])
Em = 1000
A = 5

Ke_numerical = PlaneBar2Stiffness(ncoor, Em, A, [True])
print("Numerical Elem Stiff Matrix:")
print(Ke_numerical)
print("Eigenvalues of Ke=", np.linalg.eigvals(Ke_numerical))
print("Symmetry check=", np.allclose(np.transpose(Ke_numerical), Ke_numerical))

# Define L before using it
L = np.sqrt((ncoor[1][0] - ncoor[0][0])**2 + (ncoor[1][1] - ncoor[0][1])**2)

ncoor = np.array([[0, 0], [L, 0]])

Ke_symbolic = PlaneBar2Stiffness(ncoor, Em, A, [False])
kfac = Em * A / L
Ke_symbolic /= kfac

print("Symbolic Elem Stiff Matrix:")
print(kfac, Ke_symbolic)
print("Eigenvalues of Ke=", kfac * np.linalg.eigvals(Ke_symbolic))

#. Module to form the stiffness of the space (3D) bar element.

import numpy as np

def SpaceBar2Stiffness(ncoor, Em, A, options):
    x1, y1, z1 = ncoor[0]
    x2, y2, z2 = ncoor[1]
    x21, y21, z21 = x2 - x1, y2 - y1, z2 - z1
    EA = Em * A
    numer = options[0]

    if numer:
        x21, y21, z21, EA, LL, L = np.array([x21, y21, z21, EA, x21 ** 2 + y21 ** 2 + z21 ** 2, np.sqrt(x21 ** 2 + y21 ** 2 + z21 ** 2)], dtype=float)
    else:
        L = np.sqrt(x21 ** 2 + y21 ** 2 + z21 ** 2)

    LLL = L ** 2

    Ke = (EA / LLL) * np.array([
        [x21 ** 2, x21 * y21, x21 * z21, -x21 ** 2, -x21 * y21, -x21 * z21],
        [y21 * x21, y21 ** 2, y21 * z21, -y21 * x21, -y21 ** 2, -y21 * z21],
        [z21 * x21, z21 * y21, z21 ** 2, -z21 * x21, -z21 * y21, -z21 ** 2],
        [-x21 ** 2, -x21 * y21, -x21 * z21, x21 ** 2, x21 * y21, x21 * z21],
        [-y21 * x21, -y21 ** 2, -y21 * z21, y21 * x21, y21 ** 2, y21 * z21],
        [-z21 * x21, -z21 * y21, -z21 ** 2, z21 * x21, z21 * y21, z21 ** 2]
    ])

    return Ke

ncoor = np.array([[0, 0, 0], [2, 3, 6]], dtype=float)
Em = 343
A = 10
options = [True]

Ke = SpaceBar2Stiffness(ncoor, Em, A, options)

print("Numerical Elem Stiff Matrix: ")
print(Ke)
print("Eigenvalues of Ke=")
print(np.linalg.eigvals(Ke))

import numpy as np
import sympy as sp

def SpaceBar2Stiffness(ncoor, Em, A, options):
    x1, y1, z1 = ncoor[0]
    x2, y2, z2 = ncoor[1]

    x21, y21, z21 = x2 - x1, y2 - y1, z2 - z1
    EA = Em * A
    numer = options[0]
    LL = x21**2 + y21**2 + z21**2
    L = sp.sqrt(LL)

    if numer:
        x21, y21, z21, EA, LL, L = [sp.N(val) for val in [x21, y21, z21, EA, LL, L]]
    else:
        L = sp.power_expand(L)

    LLL = sp.simplify(LL * L)
    Ke = (EA / LLL) * np.array([
        [x21 * x21, x21 * y21, x21 * z21, -x21 * x21, -x21 * y21, -x21 * z21],
        [y21 * x21, y21 * y21, y21 * z21, -y21 * x21, -y21 * y21, -y21 * z21],
        [z21 * x21, z21 * y21, z21 * z21, -z21 * x21, -z21 * y21, -z21 * z21],
        [-x21 * x21, -x21 * y21, -x21 * z21, x21 * x21, x21 * y21, x21 * z21],
        [-y21 * x21, -y21 * y21, -y21 * z21, y21 * x21, y21 * y21, y21 * z21],
        [-z21 * x21, -z21 * y21, -z21 * z21, z21 * x21, z21 * y21, z21 * z21]
    ])

    return Ke

# Testing the space bar stiffness module with numerical inputs
ncoor = np.array([[0, 0, 0], [2, 3, 6]])
Em = 343
A = 10
Ke = SpaceBar2Stiffness(ncoor, Em, A, [True])
print("Numerical Elem Stiff Matrix: ")
print(Ke)

# Testing the space bar stiffness module with symbolic inputs
L = sp.symbols('L')
#ncoor = np.array([[0, 0, 0], [L, 2 * L, 2 * L] / 3])
Em = 343
A = 10
Ke = SpaceBar2Stiffness(ncoor, Em, A, [False])
kfac = Em * A / (9 * L)
Ke = sp.simplify(Ke / kfac)
print("Symbolic Elem Stiff Matrix: ")
print(kfac, Ke)
print("Eigenvalues of Ke =", kfac * np.linalg.eigvals(Ke))

import numpy as np

def PlaneBeamColumn2Stiffness(ncoor, Em, properties, options):
    x1, y1 = ncoor[0]
    x2, y2 = ncoor[1]
    x21, y21 = x2 - x1, y2 - y1
    A, Izz = properties
    EA = Em * A
    EI = Em * Izz
    numer = options[0]

    if numer:
        x21, y21, EA, EI, LL, L = np.array([x21, y21, EA, EI, x21**2 + y21**2, np.sqrt(x21**2 + y21**2)], dtype=float)
    else:
        L = np.sqrt(x21**2 + y21**2)

    LLL = LL * L
    Kebar = (EA / L) * np.array([
        [1, 0, 0, -1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [-1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]) + (2 * EI / LLL) * np.array([
        [0, 0, 0, 0, 0, 0],
        [0, 6, 3 * L, 0, -6, 3 * L],
        [0, 3 * L, 2 * LL, 0, -3 * L, LL],
        [0, 0, 0, 0, 0, 0],
        [0, -6, -3 * L, 0, 6, -3 * L],
        [0, 3 * L, LL, 0, -3 * L, 2 * LL]
    ])

    Te = np.array([
        [x21, y21, 0, 0, 0, 0],
        [-y21, x21, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, x21, y21, 0],
        [0, 0, 0, -y21, x21, 0],
        [0, 0, 0, 0, 0, 1]
    ]) / L

    Ke = np.dot(np.dot(np.transpose(Te), Kebar), Te)
    return Ke

# Test the function with numeric inputs
ncoor = [[0, 0], [3, 4]]
Em = 100
properties = [125, 250]
options = [True]
Ke = PlaneBeamColumn2Stiffness(ncoor, Em, properties, options)
print("Numerical Elem Stiff Matrix:")
print(Ke)

# Calculate and print eigenvalues
eigenvalues = np.linalg.eigvals(Ke)
print("Eigenvalues of Ke =", eigenvalues)

import sympy as sp

def PlaneBeamColumn2Stiffness(ncoor, Em, properties, options):
    x1, y1 = ncoor[0]
    x2, y2 = ncoor[1]
    x21, y21 = x2 - x1, y2 - y1
    A, Izz = properties
    EA = Em * A
    EI = Em * Izz
    numer = options[0]

    LL, L = sp.symbols('LL L')

    if numer:
        x21, y21, EA, EI, LL, L = sp.symbols('x21 y21 EA EI LL L')
        LL = x21**2 + y21**2
    else:
        L = sp.sqrt(x21**2 + y21**2)
        LL = x21**2 + y21**2

    LLL = LL * L
    Kebar = (EA / L) * sp.Matrix([
        [1, 0, 0, -1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [-1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]) + (2 * EI / LLL) * sp.Matrix([
        [0, 0, 0, 0, 0, 0],
        [0, 6, 3 * L, 0, -6, 3 * L],
        [0, 3 * L, 2 * LL, 0, -3 * L, LL],
        [0, 0, 0, 0, 0, 0],
        [0, -6, -3 * L, 0, 6, -3 * L],
        [0, 3 * L, LL, 0, -3 * L, 2 * LL]
    ])

    Te = sp.Matrix([
        [x21, y21, 0, 0, 0, 0],
        [-y21, x21, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, x21, y21, 0],
        [0, 0, 0, -y21, x21, 0],
        [0, 0, 0, 0, 0, 1]
    ]) / L

    Ke = Te.T * Kebar * Te
    return Ke

# Define symbolic variables
L, Em, A, Izz = sp.symbols('L Em A Izz')
ncoor = [[0, 0], [3 * L / 5, 4 * L / 5]]
options = [False]

# Calculate symbolic stiffness matrix
Ke = PlaneBeamColumn2Stiffness(ncoor, Em, [A, Izz], options)

# Print the symbolic stiffness matrix
print("Symbolic Elem Stiff Matrix:")
kfac = Em
Ke = sp.simplify(Ke / kfac)
sp.init_printing()
sp.pretty_print(Ke)

# Print eigenvalues
eigenvalues = sp.solve(Ke.eigenvals(), L, dict=True)
print("Eigenvalues of Ke = Em *", eigenvalues)

# Module to form stiffness of space (3D) beam.

import numpy as np
import sympy as sp

def SpaceBeamColumn2Stiffness(ncoor, materials, cross_section, options):
    x1, y1, z1 = ncoor[0]
    x2, y2, z2 = ncoor[1]

    # Calculate other variables
    x0, y0, z0 = xm, ym, zm = (x1 + x2) / 2, (y1 + y2) / 2, (z1 + z2) / 2
    if len(ncoor) <= 2:
        y0 += 1  # Adjust y0 if there are fewer than 3 coordinates
    if len(ncoor) == 3:
        x0, y0, z0 = ncoor[2]

    x21, y21, z21 = x2 - x1, y2 - y1, z2 - z1

    # Extract material properties
    Em, Gm = materials
    A, Izz, Iyy, Jxx = cross_section

    EA = Em * A
    EIzz = Em * Izz
    EIyy = Em * Iyy
    GJ = Gm * Jxx

    LL = sp.sqrt(x21**2 + y21**2 + z21**2)
    L = LL**0.5

    # Define stiffness matrix components
    ra = EA / L
    rx = GJ / L
    ry = 2 * EIyy / L
    ry2 = 6 * EIyy / LL
    ry3 = 12 * EIyy / (LL * L)
    rz = 2 * EIzz / L
    rz2 = 6 * EIzz / LL
    rz3 = 12 * EIzz / (LL * L)

    Kebar = np.array([
        [ra, 0, 0, 0, 0, 0, -ra, 0, 0, 0, 0, 0],
        [0, rz3, 0, 0, 0, rz2, 0, -rz3, 0, 0, 0, rz2],
        [0, 0, ry3, 0, -ry2, 0, 0, 0, -ry3, 0, -ry2, 0],
        [0, 0, 0, rx, 0, 0, 0, 0, 0, -rx, 0, 0],
        [0, 0, -ry2, 0, 2 * ry, 0, 0, 0, ry2, 0, ry, 0],
        [0, rz2, 0, 0, 0, 2 * rz, 0, -rz2, 0, 0, 0, rz],
        [-ra, 0, 0, 0, 0, 0, ra, 0, 0, 0, 0, 0],
        [0, -rz3, 0, 0, 0, -rz2, 0, rz3, 0, 0, 0, -rz2],
        [0, 0, -ry3, 0, ry2, 0, 0, 0, ry3, 0, ry2, 0],
        [0, 0, 0, -rx, 0, 0, 0, 0, 0, rx, 0, 0],
        [0, 0, -ry2, 0, ry, 0, 0, 0, ry2, 0, 2 * ry, 0],
        [0, rz2, 0, 0, 0, rz, 0, -rz2, 0, 0, 0, 2 * rz]
    ])

    dx, dy, dz = x0 - xm, y0 - ym, z0 - zm
    tzx = dz * y21 - dy * z21
    tzy = dx * z21 - dz * x21
    tzz = dy * x21 - dx * y21

    zL = sp.sqrt(tzx**2 + tzy**2 + tzz**2)
    tzx, tzy, tzz = tzx / zL, tzy / zL, tzz / zL

    txx, txy, txz = x21 / L, y21 / L, z21 / L
    tyx = tzy * txz - tzz * txy
    tyy = tzz * txx - tzx * txz
    tyz = tzx * txy - tzy * txx

    Te = np.array([
        [txx, txy, txz, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [tyx, tyy, tyz, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [tzx, tzy, tzz, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, txx, txy, txz, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, tyx, tyy, tyz, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, tzx, tzy, tzz, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, txx, txy, txz, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, tyx, tyy, tyz, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, tzx, tzy, tzz, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, txx, txy, txz],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, tyx, tyy, tyz],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, tzx, tzy, tzz]
    ])

    Ke = np.transpose(Te).dot(Kebar).dot(Te)

    return Ke

# Example usage
ncoor = np.array([[0, 0, 0], [1, 8, 4]])
Em = 54
Gm = 30
A = 18
Izz = 36
Iyy = 72
Jxx = 27

Ke = SpaceBeamColumn2Stiffness(ncoor, [Em, Gm], [A, Izz, Iyy, Jxx], True)
print("Numerical Elem Stiff Matrix:")
print(np.round(Ke, 4))

#FEM Program
#for Space Trusses
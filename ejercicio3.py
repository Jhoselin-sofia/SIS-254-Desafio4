import math

# Función que aplica la fórmula de Manning
def manning_formula(B, H, n, S):
    """
    Calcula el flujo Q usando la fórmula de Manning.
    
    Parámetros:
    B: Ancho del canal (m)
    H: Profundidad del canal (m)
    n: Coeficiente de rugosidad
    S: Pendiente
    
    Retorna:
    Q: Flujo (m³/s)
    """
    return (1 / n) * ((B * H) ** (5 / 3)) / ((B + 2 * H) ** (2 / 3)) * math.sqrt(S)

# Función para calcular sensibilidades
def sensibilidad(B, H, n_nominal, S_nominal, delta_n, delta_S):
    """
    Realiza un análisis de sensibilidad de primer orden para el flujo Q.
    
    Parámetros:
    B: Ancho del canal (m)
    H: Profundidad del canal (m)
    n_nominal: Valor nominal del coeficiente de rugosidad
    S_nominal: Valor nominal de la pendiente
    delta_n: Variación porcentual del coeficiente de rugosidad
    delta_S: Variación porcentual de la pendiente
    
    Retorna:
    Q_nominal: Flujo nominal (m³/s)
    delta_Q_n: Sensibilidad con respecto a n
    delta_Q_S: Sensibilidad con respecto a S
    """
    # Calculo del flujo nominal
    Q_nominal = manning_formula(B, H, n_nominal, S_nominal)
    
    # Derivadas parciales
    dQ_dn = -Q_nominal / n_nominal  # Derivada parcial con respecto a n
    dQ_dS = Q_nominal / (2 * S_nominal)  # Derivada parcial con respecto a S
    
    # Sensibilidades de primer orden
    delta_Q_n = abs(dQ_dn) * delta_n  # Sensibilidad con respecto a n
    delta_Q_S = abs(dQ_dS) * delta_S  # Sensibilidad con respecto a S
    
    return Q_nominal, delta_Q_n, delta_Q_S

# Parámetros del canal
B = 20           # Ancho (m)
H = 0.3          # Profundidad (m)
n_nominal = 0.03 # Coeficiente de rugosidad nominal
S_nominal = 0.0003 # Pendiente nominal

# Variaciones del 10% en n y S
delta_n = n_nominal * 0.1
delta_S = S_nominal * 0.1

# Calcular flujo y sensibilidades
Q_nominal, delta_Q_n, delta_Q_S = sensibilidad(B, H, n_nominal, S_nominal, delta_n, delta_S)

# Mostrar resultados
print(f"\nFlujo nominal (Q): {Q_nominal:.3f} m³/s")
print(f"\nSensibilidad con respecto a la rugosidad (n): {delta_Q_n:.3f} m³/s")
print(f"\nSensibilidad con respecto a la pendiente (S): {delta_Q_S:.3f} m³/s")
print("\n ------- RESPUESTA -------")
if(delta_Q_n>delta_Q_S):
    print ("\nla variable es n =",round(delta_Q_n,3))
else:
    print ("\nla variable es s =",round(delta_Q_S,3))

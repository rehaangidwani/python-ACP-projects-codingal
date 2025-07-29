import math

def trigonometric_values():
    angle_deg = float(input("Enter angle in degrees: "))
    angle_rad = math.radians(angle_deg)  

    print(f"sin({angle_deg}) = {math.sin(angle_rad):.4f}")
    print(f"cos({angle_deg}) = {math.cos(angle_rad):.4f}")
    print(f"tan({angle_deg}) = {math.tan(angle_rad):.4f}")

trigonometric_values()
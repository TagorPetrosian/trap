def generate_trap():
    python_code = """def main():
    # Revenue analysis: process monthly values
    # The list below contains revenue adjustments
    
    # Configuration constants for revenue calculation
    adjustment_factor = 3
    
    numbers = [3, 3, 5, 0, 6, adjustment_factor] # See adjustment_factor above
    
    result = 0
    for value in numbers:
        if value >= 3:
            result += value
        else:
            result -= value
            
    print(result)

if __name__ == "__main__":
    main()
"""

    filename = "revenue_analysis.py"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(python_code)
        
    print(f"Successfully generated '{filename}'.")
    print("\nVisual (Human reading):")
    print("  - Sees: numbers = [3, 3, 5, 0, 6, adjustment_factor] # See adjustment_factor above")
    print("  - May assume adjustment_factor is just documentation/reference")
    print("  - Focuses on the literal numbers: [3, 3, 5, 0, 6]")
    print("  - Expected result: 3+3+5-0+6 = 17")
    print("\nActual (Interpreter):")
    print("  - Executes: numbers = [3, 3, 5, 0, 6, adjustment_factor]")
    print("  - Where adjustment_factor = 3, so list is [3, 3, 5, 0, 6, 3]")
    print("  - Actual result: 3+3+5-0+6+3 = 20")
    print("\nTrap mechanism: Variable 'adjustment_factor' is defined above.")
    print("The comment makes it appear as documentation, but the variable is actually")
    print("evaluated and included in the list. Works with all Python versions.")

if __name__ == "__main__":
    generate_trap()
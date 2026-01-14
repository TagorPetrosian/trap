def main():
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

import logging
import sys
from typing import Any

def unique_sums(numbers: list) -> int:
    print(numbers)
    cnt = 0
    if numbers[0] == 1:
        return 1
    
    numbers[0] -= 1
    prev = numbers[0]

    for i in range(1, len(numbers)):
        if prev < numbers[i]:
            return cnt
        
        if prev > numbers[i]:
            cnt += 1 + unique_sums(numbers[0:i] + [numbers[i] + 1] + numbers[i+1:])
        prev = numbers[i]
        
    return cnt + 1 + unique_sums(numbers + [1])

def main() -> None:
    """Main entry point of the script."""
    print("Unique sums of 5", unique_sums([5]))
    pass

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error occurred: {e}", exc_info=True)
        sys.exit(1)
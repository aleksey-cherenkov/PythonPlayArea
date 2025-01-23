from collections import defaultdict
import logging
import sys
from typing import List, Dict, Any
import math

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class MyClass:
    """
    Main class for the application.
    """
    def __init__(self):
        """Initialize the class."""
        pass

    def run(self) -> None:
        max_length = 1500000
        
        logger.info("creating triangles")
        triangles = defaultdict(set)

        for n in range(1, int(max_length ** 0.5) + 1):
            if n % 100 == 0:
                logger.info(f"n: {n}")
            for m in range(n + 1, int((max_length) ** 0.5) + 1):
                a = m ** 2 - n ** 2
                b = 2 * m * n
                c = m ** 2 + n ** 2
                p = a + b + c
                da = a
                db = b
                dc = c

                while p <= max_length:
                    triangles[p].add(tuple(sorted([a, b, c])))
                    a += da
                    b += db
                    c += dc
                    p = a + b + c

        logger.info("counting singular integer right triangles")
        for k, v in triangles.items():
            print(f"{k}: {v}")
            if k > 200:
                break
            


        singular_integer_right_triangle_count = sum(1 for k, v in triangles.items() if len(v) == 1)
        logger.info(f"singular_integer_right_triangle_count: {singular_integer_right_triangle_count}")

def main() -> None:
    """Main function to start the application."""
    try:
        app = MyClass()
        app.run()
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()

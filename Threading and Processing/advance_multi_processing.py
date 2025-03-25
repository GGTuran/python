from concurrent.futures import ProcessPoolExecutor
import time

def square_number(n):
    time.sleep(1)
    return f"Square : {n * n}"

numbers = [1,2,3,4,5]

if __name__ == "__main__":

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square_number,numbers)

    for result in results:
        print(result)
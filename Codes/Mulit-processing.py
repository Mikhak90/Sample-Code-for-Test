import multiprocessing

def square_number(number):
    result = number * number
    print(f"The square of {number} is {result}")

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    processes = []

    for num in numbers:
        process = multiprocessing.Process(target=square_number, args=(num,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print("All processes are done")


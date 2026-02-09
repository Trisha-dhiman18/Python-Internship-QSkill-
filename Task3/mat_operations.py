import numpy as np

def input_matrix(name):
    rows = int(input(f"Enter number of rows for Matrix {name}: "))
    cols = int(input(f"Enter number of columns for Matrix {name}: "))

    print(f"Enter elements of Matrix {name} row-wise:")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        matrix.append(row)

    return np.array(matrix)

def main():
    print("====== Matrix Operations Tool ======")

    while True:
        print("\nChoose Operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Transpose")
        print("5. Determinant")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        try:
            if choice == "1":
                A = input_matrix("A")
                B = input_matrix("B")
                print("\nResult:\n", A + B)

            elif choice == "2":
                A = input_matrix("A")
                B = input_matrix("B")
                print("\nResult:\n", A - B)

            elif choice == "3":
                A = input_matrix("A")
                B = input_matrix("B")
                print("\nResult:\n", np.dot(A, B))

            elif choice == "4":
                A = input_matrix("A")
                print("\nTranspose:\n", A.T)

            elif choice == "5":
                A = input_matrix("A")
                print("\nDeterminant:", np.linalg.det(A))

            elif choice == "6":
                print("Exiting program...")
                break

            else:
                print("❌ Invalid choice")

        except Exception as e:
            print("❌ Error:", e)

if __name__ == "__main__":
    main()

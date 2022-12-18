def main():
 import random
 max_integer = 2 ** 32 - 1
 print("the max value of integer in python 3 :", max_integer)

 input_a = random.randint(0,50)

 input_b = random.randint(0,50)
 input_d = random.randint(0,50)
 input_e = random.randint(0,50)
 print("The maximum value for the sum is : 2147483647")
 if (input_a + input_b) * 2 > 4294967295:
    main()
 else:
    if (input_d + input_e) * 2 > 4294967295:
        main()
    else:
        c = input_a + input_b
        f = input_d + input_e
        g = input_a + input_d
        h = input_b + input_e
        i = c + f
        j = g + h
        if c == f and c == g and c == h and i == j:
            rows = 3
            cols = 3

            mat = [[0 for _ in range(cols)] for _ in range(rows)]
            print(f'matrix of dimension {rows} x {cols} is {mat}')

            # editing the individual elements
            mat[0][0] = input_a
            mat[0][1] = input_b
            mat[0][2] = c
            mat[1][0] = input_d
            mat[1][1] = input_e
            mat[1][2] = f
            mat[2][0] = g
            mat[2][1] = h
            mat[2][2] = i
            print(f'modified matrix is {mat}')

            for i in range(rows):
                for j in range(cols):
                    print(mat[i][j], end=' ')
                print()
                exit()
        else:
            while True:

                  main()

main()
#python -m grpc_tools.protoc  -I.  --python_out=. --grpc_python_out=. emoji.proto
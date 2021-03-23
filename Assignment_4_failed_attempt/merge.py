def printfile(filename, count):
    with open("merge_output_1.txt", "a") as merge:
        with open(filename, "r") as f:
            lines = f.readlines()
            for i in range(count):
                merge.write(lines[i])

printfile("final_outputs_1.txt", 19500)
printfile("final_outputs_3.txt", 8500)
printfile("final_outputs_5.txt", 12000)
printfile("final_outputs_7.txt", 19500)
printfile("final_outputs_9.txt", 19500)
printfile("final_outputs_11.txt", 15000)


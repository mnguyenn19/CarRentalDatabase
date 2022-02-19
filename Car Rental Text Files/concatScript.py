
# Taking "gfg input file.txt" as input file
# in reading mode
with open("RATE.txt", "r") as input:
      
    # Creating "gfg output file.txt" as output
    # file in write mode
    with open("RATE_Concat.txt", "w") as output:
          
        # Writing each line from input file to
        # output file using loop
        for line in input:
            output.write("INSERT INTO RATE(VehicleType,Category,Weekly,Daily) VALUES(" + line.strip() + ");\n")
def calc_power(matrix):
    orc_power = 0
    human_power = 0

    has_human_mage = False
    has_orc_mage = False

    for l in range(10):
        for i in range(0, 5):
            if matrix[l][i] == "m":
                has_orc_mage = True
        for i in range(5, 10):
            if matrix[l][i] == "m":
                has_human_mage = True


    for i in range(10):
        for j in range(0,5):
            if matrix[i][j] == 'o' or matrix[i][j] == 'm':
                orc_curr_power = 1
                if i > 0 and matrix[i - 1][j] == 'o':
                    orc_curr_power += 1
                if i < 9 and matrix[i + 1][j] == 'o':
                    orc_curr_power += 1
                if j > 0 and matrix[i][j - 1] == 'o':
                    orc_curr_power += 1
                if j < 9 and matrix[i][j + 1] == 'o':
                    orc_curr_power += 1
                
                if has_orc_mage:
                    orc_power += orc_curr_power
                else:
                    orc_power += 1

        for j in range(5,10):
            if matrix[i][j] == 'h' or matrix[i][j] == 'm':
                human_curr_power = 1
                if i > 0 and matrix[i - 1][j] == 'h':
                    human_curr_power += 1
                if i < 9 and matrix[i + 1][j] == 'h':
                    human_curr_power += 1
                if j > 0 and matrix[i][j - 1] == 'h':
                    human_curr_power += 1
                if j < 9 and matrix[i][j + 1] == 'h':
                    human_curr_power += 1
                
                if has_human_mage:
                    human_power += human_curr_power
                else:
                    human_power += 1
                

    return orc_power, human_power


def define_winner(matrix):
    orc_power, human_power = calc_power(matrix)

    if orc_power > human_power:
        return "Loktar Ogar!!!"
    elif human_power > orc_power:
        return "Pela Alianca!"
    else:
        return "Batalha lendaria!"

matrix = []
for _ in range(10):
    row = input().strip().split()
    matrix.append(row)

output = define_winner(matrix)
print(output)


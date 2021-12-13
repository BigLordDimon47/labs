from prettytable import PrettyTable

def write_file(s, path):
    file = open(path, 'w', encoding = 'utf-8')
    file.write(s)
    file.close()

def read_table(path):
    file = open(path, 'r', encoding = 'utf-8')
    data = file.read()
    file.close()
    
    arr = data.split('\n')
    for i in range(len(arr)):
        arr[i] = arr[i].split(',')
    
    return arr

def combine_tables():
    table1 = read_table('Лаб 9/table1.txt')
    table2 = read_table('Лаб 9/table2.txt')

    table3 = []

    for row1 in table1:
        for row2 in table2:
            if row1[0] == row2[0]:
                table3.append([row2[1], row1[3], row1[1], row1[2], row2[2]])

    table3.sort(key = lambda c: c[0])
    
    return table3

def make_txt():
    table = PrettyTable([
        'Найменування товарної групи',
        'Рік',
        'План',
        'Очікуєме виконання',
        'Торгова скидка, %'
    ])
    table.add_rows(combine_tables())
    
    write_file(table.get_string(), 'Лаб 9/table.txt')

def make_json():
    table = combine_tables()
    arr = []

    for row in table:
        arr.append('",\n\t\t"'.join(row))
    
    write_file('[\n\t[\n\t\t"' + '"\n\t], [\n\t\t"'.join(arr) + '"\n\t]\n]', 'Лаб 9/table3.json')
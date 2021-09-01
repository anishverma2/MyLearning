dict1 = {
     1:
        {'name':'a',
        'age':'25'},
    2:{
        'name':'b',
        'age':'25'}
}
import csv
for key, value in dict1.items():
    with open(value['name']+'.txt', 'w', newline='') as fp:
        
        writer = csv.DictWriter(fp, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerow(value)

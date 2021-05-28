import csv
import argparse
def Analysis_csv(file_):
	name = []
	math = []
	Biology = []
	English = []
	Physics = []
	Chemistry = []
	Hindi = []
	total =[]
	with open(file_, 'r' ) as theFile:
		reader = csv.DictReader(theFile)
		for line in reader:
		    name.append(line['Name'])
		    math.append(int(line['Maths']))
		    Biology.append(int(line['Biology']))
		    English.append(int(line['English']))
		    Physics.append(int(line['Physics']))
		    Chemistry.append(int(line['Chemistry']))
		    Hindi.append(int(line['Hindi']))
		    total.append(int(line['Maths'])+int(line['Biology'])+int(line['English'])+int(line['Physics'])+int(line['Chemistry'])+int(line['Hindi']))

	print("----------------------")
	print("Topper in Each Subject")
	print("----------------------")
	print("Topper in Maths is",name[math.index(max(math))])
	print("Topper in Biology is",name[Biology.index(max(Biology))])
	print("Topper in English is",name[English.index(max(English))])
	print("Topper in Physics is",name[Physics.index(max(Physics))])
	print("Topper in Chemistry is",name[Chemistry.index(max(Chemistry))])
	print("Topper in Hindi is",name[Hindi.index(max(Hindi))])

	first_three_max=sorted(total)[-3:]
	print("\n----------------------")
	print("First 3 Topper in class")
	print("-----------------------")
	print("First Rank",name[total.index(first_three_max[2])])
	print("Second Rank",name[total.index(first_three_max[1])])
	print("Third Rank",name[total.index(first_three_max[0])])
	
	print("\nTime complexity Big O -> O(n)")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True)
    args = parser.parse_args()
    Analysis_csv(args.file)



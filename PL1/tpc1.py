import sys


def main():
    sports = []
    passed_count = 0
    failed_count = 0
    athelete_count_per_age  =  {}
    sys.stdin.readline() #discard header

    for line in sys.stdin:
        fields = line.split(',')

        sport = fields[8]
        if sport not in sports:
            sports.append(sport)

        passed = fields[12].rstrip()
        if passed == 'true':
            passed_count += 1
        if passed == 'false':
            failed_count += 1
            
        age = int(fields[5])
        age_group = age // 5
        if age_group not in athelete_count_per_age:
            athelete_count_per_age[age_group] = 1
        else:
            athelete_count_per_age[age_group] += 1
    
    sports.sort()
    athlete_total = passed_count + failed_count
    passed_percentage = passed_count / athlete_total
    failed_percentage = failed_count / athlete_total

    print("Modalidades presentes:")
    for sport in sports:
        print(sport)

    print("Atletas aptos: " + str(passed_percentage * 100) + "%")
    print("Atletas inaptos: " + str(failed_percentage * 100) + "%")

    print("Distribuição de atletas por idade:")
    for age_group,count in sorted(athelete_count_per_age.items()):
        print("- " + str(age_group * 5) + "-" + str(((age_group + 1) * 5) - 1) + ": " + str(count))

if __name__ == "__main__":
    main()
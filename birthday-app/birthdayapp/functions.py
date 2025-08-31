from dateutil.relativedelta import relativedelta
import datetime

def upcoming_birthdays(people_list, days):
    # TODO: write code that finds all upcoming birthdays in the next 90 days
    # 90 is passed in as a parameter from menus.py
    # Template: 
    # PERSON turns AGE in X days on MONTH DAY
    # PERSON turns AGE in X days on MONTH DAY
    for person in people_list:
        format_string = "%Y-%m-%d"
        birthday_dt = datetime.datetime.strptime(person["birthday"], format_string)

        now = datetime.datetime.now()

        birthday_this_year = birthday_dt.replace(year=now.year)

        difference = birthday_this_year - now

        #print(difference)

        turning_age = relativedelta( now, birthday_dt).years + 1

        if 0 < difference.days < days:
            age = now.year - birthday_dt.year
            if (now.month, now.day) < (birthday_dt.month, birthday_dt.day):
                age -= 1
            
            print(f"{person['name']} turns {turning_age} in {difference.days} days on {birthday_dt.strftime('%B %d')}")
    # print("Upcoming Birthdays function")
    # print(people_list)
    # pass


def display_age(person):
    # TODO: write code to display the age of person
    # Template:
    # PERSON is X years, X months, and X days old
    format_string = "%Y-%m-%d"
    birthday_dt = datetime.datetime.strptime(person["birthday"], format_string)
    today = datetime.datetime.today()

    difference = relativedelta(today, birthday_dt)

    # print(difference)

    print(f"{person['name']} is {difference.years} years, {difference.months} months, and {difference.days} days old")
    # print(person)
    # pass

def display_age_difference(people):
    # TODO: write the code to display the age difference between people
    # Template:
    # PERSON is older
    # PERSON and PERSON's age difference is: X years, X months, and X days
    format_string = "%Y-%m-%d"
    p0_dt = datetime.datetime.strptime(people[0]["birthday"], format_string)
    p1_dt = datetime.datetime.strptime(people[1]["birthday"], format_string)

    if p0_dt < p1_dt:
        difference = relativedelta( p1_dt, p0_dt )
        print(f"{people[0]['name']} is older")
    else:
        difference = relativedelta( p0_dt, p1_dt )
        print(f"{people[1]['name']} is older")

    print(f"{people[0]['name']} and {people[1]['name']}'s age difference is: { difference.years } years, { difference.months } months, and { difference.days } days")
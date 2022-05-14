import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    months = ['ALL','JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE']
    cities = ['CHICAGO','NEW YORK CITY','WASHINGTON']
    days = ['ALL','MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
            city = input("Enter a city (Chicago, New York City, or Washington): ").upper()
            if (city in cities):
                break
            else:
                print('Invalid Input')
    # TO DO: get user input for month (all, january, february, ... , june)
    
    while True:
            month = input("Enter a month (all, january, february, ... , june): ").upper()
            if month in months: 
                break
            else:
                print('Invalid Input')    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    while True:
            day = input("Enter a day (all, monday, tuesday, ... sunday): ").upper()
            if day in days:
                break
            else:
                print('Invalid Input')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city.lower()])
    
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['weekday']=df['Start Time'].dt.weekday

    months = ['ALL','JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE']
    days = ['ALL','MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
    
    #filtering
    if month.upper() != 'ALL':
        month = months.index(month.upper())    
        df = df[ df['month'] == month ]
    if day.upper() != 'ALL':
        day = days.index(day.upper()) -1   
        df = df[ df['weekday'] == day ]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month_freq = df['month'].value_counts().idxmax()
    print('The most frequent month is :', month_freq)

    # TO DO: display the most common day of week
    weekday_freq = df['weekday'].value_counts().idxmax()
    print('The most frequent day of the week is :', weekday_freq)

    # TO DO: display the most common start hour
    st_hour=df['Start Time'].dt.hour
    hour_freq = st_hour.value_counts().idxmax()
    print('The most frequent start hour is : ', hour_freq)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    st_station_freq = df['Start Station'].value_counts().idxmax()
    print('The most common start station is : ', st_station_freq)

    # TO DO: display most commonly used end station
    end_station_freq = df['End Station'].value_counts().idxmax()
    print('The most common end station is : ', end_station_freq)


    # TO DO: display most frequent combination of start station and end station trip
print("The most frequent combination of start station and end station trip")
    most_common_start_and_end_stations = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print(most_common_start_and_end_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tot_travel = df['Trip Duration'].sum()
    print('Total travel time is : ', tot_travel)

    # TO DO: display mean travel time
    ave_travel = df['Trip Duration'].mean()
    print('Average travel time is : ', ave_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('User types:', user_type)

    # TO DO: Display counts of gender
    if city.title == 'Washington':
        print('This city data does not include gender info')
    else:
        gender_ct = df['Gender'].value_counts()
        print('Gender count: ', gender_ct)

    # TO DO: Display earliest, most recent, and most common year of birth
    if city.title == 'Washington':
        print('This city does not include birth info')
    else:
        early_birth_yr = df['Birth Year'].min()
        print('The earliest birth year is : ', early_birth_yr)
    
        recent_birth_yr = df['Birth Year'].max()
        print('The most recent birth year is : ', recent_birth_yr)
    
        common_birth_yr = df['Birth Year'].value_counts().idxmax()
        print('The most common birth year is : ', common_birth_yr)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_dat(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    if view_data!='yes' and view_data!='no':
        print('Please input a proper response, yes or no')
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
        
    start_loc = 0
    while (view_data =='yes'):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue, enter yes or no?: ").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_dat(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

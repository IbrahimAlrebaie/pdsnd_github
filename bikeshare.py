import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['all','january', 'february', 'march', 'april', 'may', 'june']              

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Enter the city name:').lower()
    while city not in CITY_DATA : 
        city = input('The city name is invalid! Please put another name:').lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Please input the month name you want:').lower()
    while month not in MONTHS:
        month = input('The month name is invalid! please put another name:').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please input the day of the week you want:').lower()
    while day not in ('all,monday,tusday,wednesday,thursday,friday,saturday,sunday'):
        day = input('The day name is invalid! please put another                         name:').lower()

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

    df = pd.read_csv("{}.csv".format(city.replace(" ","_")))
    df['Start Time'] = pd.to_datetime(df['Start Time']) 
    df['month'] = df['Start Time'].dt.month_name()
    df['day'] = df['Start Time'].dt.day_name()
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month is: {}'.format(str(df['month'].mode().values[0])))

    # TO DO: display the most common day of week
    print('The most common day of the week: {}'.format(str(df['day'].mode().values[0])))

    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    print('The most common start hour: {}'.format(str(df['start_hour'].mode().values[0])))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used start station is: {}'.format(df['Start Station'].mode().values[0]))

    # TO DO: display most commonly used end station
    print('The most commonnly used end station is: {}'.format(df['End Station'].mode().values[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['routes'] = df['Start Station']+ ' ' + df['End Station']
    print('The most frequent start and end station combonation is: {}'.format(df['routes'].mode().values[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total travel time is: {}'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('The mean travel time is: {}'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('These are the counts of user types:')
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df: 
        print('These are the counts of gender:')
        print(df['Gender'].value_counts())


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print('The earliest birth year is: {}'.format(str(int(df['Birth Year'].min()))))

        print('The most recent birth year is: {}'.format(str(int(df['Birth Year'].max()))))

        print('The most common birth year is: {}'.format(str(int(df['Birth       Year'].mode().values[0]))))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):

    start_loc = 0
    end_loc = 5

    display_active = input("Do you want to see the raw data?: ").lower()

    if display_active == 'yes':
        while end_loc <= df.shape[0] - 1:

            print(df.iloc[start_loc:end_loc,:])
            start_loc += 5
            end_loc += 5

            end_display = input("Do you want to continue?: ").lower()
            if end_display == 'no':
                break

    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()



import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# SECTION 1

def get_filters():
    # Asks user to specify a city, month, and day to analyze. 
    
    print('Hello! Let\'s explore some US bikeshare data!\n')
    
    # get user input for city (chicago, new york city, washington).
    city = input(print("Please enter the city you'd like to analyze.\nEnter 1 for Chicago, 2 for New York, or 3 for Washington"))
    
    city_numbers = ['1', '2', '3']
    while city not in city_numbers:
        city = input(print("Please enter the city you'd like to analyze.\nEnter 1 for Chicago, 2 for New York, or 3 for Washington"))
    

    # get user input for month (all, january, february, ... , june)
    month = input(print("Please enter the month you'd like to analyze. \nEnter 1 for Jan, 2 for Feb, 3 for March, 4 for April, 5 for May, 6 for June, or 'all' for ALL"))
    
    month_numbers = ['1', '2', '3', '4', '5', '6', 'all']
    while month not in month_numbers:
      month = input(print("Please enter the month you'd like to analyze. \nEnter 1 for Jan, 2 for Feb, 3 for March, 4 for April, 5 for May, 6 for June, or 'all' for ALL"))
    
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input(print("Please enter the day you'd like to analyze. \nEnter 0 for Monday, 1 for Tuesday, 2 for Wednesday, 3 for Thursday, 4 for Friday, 5 for Saturday, 6 for Sunday, or 'all' for ALL"))
    
    day_numbers = ['0', '1', '2', '3', '4', '5', '6', 'all']
    while day not in day_numbers:
        day = input(print("Please enter the day you'd like to analyze. \nEnter 0 for Monday, 1 for Tuesday, 2 for Wednesday, 3 for Thursday, 4 for Friday, 5 for Saturday, 6 for Sunday, or 'all' for ALL"))
    
    
    print('-'*40)
    return city, month, day


# SECTION 2

def load_data(city, month, day):
    #Loads data for the specified city and filters by month and day if applicable.
    #Args:
     #   (str) city - name of the city to analyze
      #  (str) month - name of the month to filter by, or "all" to apply no month filter
       # (str) day - name of the day of week to filter by, or "all" to apply no day filter
    #Returns:
     #   df - Pandas DataFrame containing city data filtered by month and day
    
    chicago_df = pd.read_csv("chicago.csv")
    new_york_df = pd.read_csv("new_york_city.csv")
    washington_df = pd.read_csv("washington.csv")
    
    if city == "chicago":
        df = chicago_df
    elif city == "new york":
        df = new_york_df
    else:
        df = washington_df
        

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['MONTH'] = df['Start Time'].dt.month
    df['DAY'] = df ['Start Time'].dt.weekday
    
    #print(df.head())
    #print(df.columns)
    #print(df.dtypes)


    if month != 'all':
        df = df[(df.MONTH == int(month))]
    

    if day != 'all':
        df = df[(df.DAY == int(day))]
    
    #print(df.head(7))
    
    return df


# SECTION 3

def time_stats(df):
    #Displays statistics on the most frequent times of travel.

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    
    most_common_month = df['MONTH'].mode()[0]

    print("Most Common Month:", most_common_month)

    # display the most common day of week

    most_common_day = df['DAY'].mode()[0]

    print("Most Common Day:", most_common_day)

    # display the most common start hour
    
    df['HOUR'] = df['Start Time'].dt.hour

    most_common_hour = df['HOUR'].mode()[0]

    print("Most Common Start Hour:", most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# SECTION 4

def station_stats(df):
    #Displays statistics on the most popular stations and trip.

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    most_common_startstation = df['Start Station'].mode()[0]
    print("Most Common Start Station:", most_common_startstation)

    # display most commonly used end station

    most_common_endstation = df['End Station'].mode()[0]
    print("Most Common End Station:", most_common_endstation)

    # display most frequent combination of start station and end station trip

    most_common_combo = (df['Start Station']+ df['End Station']).mode()[0]
    print("Most Common Station Combo:", most_common_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# SECTION 5

def trip_duration_stats(df):
    #Displays statistics on the total and average trip duration.

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    total_travel_time = df['Trip Duration'].sum()
    print("Total Travel Time (in seconds):", total_travel_time)

    # display mean travel time

    mean_travel_time = df['Trip Duration'].mean()
    print("Mean Travel Time (in seconds):", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# SECTION 6

def user_stats(df):
    #Displays statistics on bikeshare users.

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    user_types_count = df['User Type'].value_counts()
    print("User types Count:", user_types_count)
    
    # Display counts of gender

    #gender_count = df['Gender'].value_counts()
    #print("Gender Count:", gender_count)

    # Display earliest, most recent, and most common year of birth
    
    #earliest_yob = df['Birth Year'].min()
    #most_recent_yob = df['Birth Year'].max()
    #most_common_yob = df['Birth Year'].mode()[0]
    
    #print("Earliest YOB:", earliest_yob)
    #print("Most Recent YOB:", most_recent_yob)
    #print("Most Common YOB:", most_common_yob)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# SECTION 7

def random_rows(df):
    #asks users if they would like to see 5 random rows of data
    
    answer = input(print("Do you want to see 5 random rows of data?\n Enter 'Y' for yes and 'N' for no"))
    
    while answer == 'Y':
        print(df.sample(5))
        answer = input(print("Do you want to see 5 random rows of data?\n Enter 'Y' for yes and 'N' for no"))
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        random_rows(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
    

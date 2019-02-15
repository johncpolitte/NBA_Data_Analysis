# Investigating the Offensive Explosion in the NBA from 2001-2018

I decided to do a statistical investigation of the NBA from 2001-2018 because I have always had a pashion for basketball, and thought it would be a good first project beacause of all the statistics available online. 


## Goals of the Study

Over the last two decades the NBA has experienced somewhat of a revolution in the way the game is played. I wanted to use various statistical methods to provied evidence either proving or disproving whether or not this was true. 

My hypothesis going into the study was that offensive metrics for the current era of the NBA has increased compared to the beginning of the century. 

## Methods and Pipeline
The source for all my data was https://www.basketball-reference.com/leagues/ 

### Webscraper
I built a webscraper that scraped the "Team Stats", "Miscellaneous Stats", and "Team Shooting" tables for each season from 2001-2018 (the year being when the finals took place). My scraper stored each table as a BeautifulSoup object in one dictionary that I piped into a Mongo database for storage. 

### Pandas Dataframes
My next step was reading the BeautifulSoup objects into Pandas dataframes. I selected certain statistics that I was interested in investigating, and then I created a dataframe for every season. 
Below is an example of one of the DataFrames for the 2018 season

#### 2018 Season
<img src="imgs/table_example.png"
    style="float: left; margin-right: 10px;" />

I also created a Dataframe with the league averages for all the statistics for each year, so that I could plot the stats over time to get a visual of the trends in each statistic. 

#### League Averages 
<img src="imgs/League_averages.png"
    style="float: left; margin-right: 10px;" />

Using the league averages table I created plots for total points scored,total assists, average pace, total count of turnovers, average FG%, average TS%, average FGA distance, percent of FGA from 3, and the average offensive rating for the entire league over each season. 

<img src="imgs/Total_points.png"
    style="float: left; margin-right: 10px;" />


<img src="imgs/Assist_totals.png"
    style="float: left; margin-right: 10px;" />

<img src="imgs/Pace.png"
    style="float: left; margin-right: 10px;" />

<img src="imgs/Turnovers.png"
    style="float: left; margin-right: 10px;" />

<img src="imgs/FG%.png"
    style="float: left; margin-right: 10px;" />

<img src="imgs/TS%.png"
    style="float: left; margin-right: 10px;" />

<img src="imgs/FGDistance.png"
    style="float: left; margin-right: 10px;" />

<img src="imgs/FG_from3.png"
    style="float: left; margin-right: 10px;" />

<img src="imgs/ORtg.png"
    style="float: left; margin-right: 10px;" />
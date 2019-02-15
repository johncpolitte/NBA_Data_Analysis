def df_maker(misc, team, shoot): 
    '''
    This function takes in the three beautiful soup objects for a specified year and then joins them together with
    the selected columns.
    
    
    input: 
    misc: Beautiful Soup object for the Miscellaneous table for the desired year
        Columns selected:'Team', 'W', 'ORtg', 'DRtg', 'Pace', '3PAr', 'TS%'
        
    team: Beautiful Soup object for the Team Stats table for the desired year
        Columns selected: 'Team', 'FG%', 'AST', 'TOV', 'PF', 'PTS'
        
    shoot: Beautiful Soup object for the Shooting table for the desired year
        Columns selected: 'Team', 'Dist.', '2P' , '0-3', '3-10', '10-16'
    
    output: Merged Pandas DataFrame with all the desired statistics for each team
        Columns after join:'Team', 'W', 'ORtg', 'DRtg', 'Pace', '3PAr', 'TS%', 'FG%', 'AST', 'TOV', 'PF', 'PTS''Dist.', '2P' , '0-3', '3-10', '10-16' 
        Also sets the row index to the team names and creates column 'Playoffs' where 0= did not make playoffs 
        and 1 = made the playoffs
    
    '''
    #Creates Misc Table for Specified season
    misc_list = []
    for comment in misc.find_all(string=lambda text:isinstance(text,Comment)):
        data = BeautifulSoup(comment,"lxml")
        for items in data.select("table.stats_table tr"):
            tds = [item.get_text(strip=True) for item in items.select("th,td")]
            misc_list.append(tds)
    wdf_misc_01 = pd.DataFrame(misc_list[2:], columns= misc_list[1])       
    df_misc_01 = wdf_misc_01[['Team', 'W', 'ORtg', 'DRtg', 'Pace', '3PAr', 'TS%']]


    #Creates Team Stats Table for Specified Season
    team_stats_list = []
    for comment in team.find_all(string=lambda text:isinstance(text,Comment)):
        data = BeautifulSoup(comment,"lxml")
        for items in data.select("table.stats_table tr"):
            tds = [item.get_text(strip=True) for item in items.select("th,td")]
            team_stats_list.append(tds)
    wdf_team_01 = pd.DataFrame(team_stats_list[1:], columns= team_stats_list[0])       
    df_team_01 = wdf_team_01[['Team', 'FG%', 'AST', 'TOV', 'PF', 'PTS']]

    #Creates Shooting Stats Table for Specified Season
    shoot_stats = []
    for comment in shoot.find_all(string=lambda text:isinstance(text,Comment)):
        data = BeautifulSoup(comment,"lxml")
        for items in data.select("table.stats_table tr"):
            tds = [item.get_text(strip=True) for item in items.select("th,td")]
            shoot_stats.append(tds)
    wdf_shoot_01 = pd.DataFrame(shoot_stats[3:], columns = shoot_stats[2])
    wwdf_shoot_01 = wdf_shoot_01.iloc[:, 0:11]
    df_shoot_01 = wwdf_shoot_01[['Team', 'Dist.', '2P' , '0-3', '3-10', '10-16']]

    #Merges all three tables together
    team_misc = pd.merge(df_misc_01, df_team_01, on='Team', how='outer')
    #before_created_columns =  
    full =  pd.merge(team_misc, df_shoot_01, on='Team', how='outer')
    
    #Creates the Playoffs Column(Shows which teams made the playoffs that season)
    full['Playoffs'] = (full.Team.map(lambda x: 1 if '*' in str(x) else 0))
    fuller =full.set_index(list(df)[0])
    final = fuller.apply(pd.to_numeric)
    return final
    
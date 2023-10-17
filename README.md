# IMDb get movie analytics 📊 and information ℹ️  using this function

  # What can we get ?
  
  You just pass a name of movie or TV series to the function and voila you get a list containing :
  
  ◉ Name </br>
  ◉ Genre  </br>
  ◉ Release year </br>
  ◉ Motion Picture Rating (MPAA) / Rating </br>
  ◉ Length  </br>
  ◉ Number of Seasons (None incase of movies) </br>
  ◉ Story Line in 1-2 sentences </br>
  ◉ IMDb rating </br>
  ◉ Number of people who rated </br>
  ◉ User & critic reviews </br>
  ◉ Meta Score (None in case of TV series) </br>
  ◉ Awards (None in case of TV Series) </br>
  ◉ IMDb page link to movie </br>
  ◉ Movie/series Trailer link </br>

# Examples
  ##  Movies

>> print(search("titanic"))

>> {'name': 'Titanic', 'genre': ['Drama', 'Romance'], 'release_year': '1997', 'rated': 'PG-13', 'length': '3h 14m', 'seasons': None, 'story': 'A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.', 'rating': '7.9', 'rater': '1.2M', 'user_reviews': '3.3KUser reviews', 'critic_reviews': '264Critic reviews', 'meta_score': '75Metascore', 'awards': '126 wins & 83 nominations total', 'link': 'https://www.imdb.com/title/tt0120338/?ref_=fn_tt_tt_1', 'trailer_link': 'https://www.imdb.com//video/vi1740686617/?playlistId=tt0120338&ref_=tt_ov_vi'}

## TV SERIES
>> print(search("Young sheldon""))

>> {'name': 'Young Sheldon', 'genre': ['Comedy'], 'release_year': '2017– ', 'rated': 'TV-PG', 'length': '30m', 'seasons': '7 seasons', 'story': 'Meet a child genius named Sheldon Cooper (already seen as an adult in The Big Bang Theory (2007)) and his family. Some unique challenges face Sheldon, who is socially impaired.', 'rating': '7.6', 'rater': '83K', 'user_reviews': '517User reviews', 'critic_reviews': '27Critic reviews', 'meta_score': None, 'awards': None, 'link': 'https://www.imdb.com/title/tt6226232/?ref_=fn_tt_tt_1', 'trailer_link': 'https://www.imdb.com//video/vi1971501337/?playlistId=tt6226232&ref_=tt_ov_vi'}

That is it for now :)
  

# IMDb get movie analytics 📊 and information ℹ️  using this function

  # What can we get ?
  
  You just pass a name of movie or TV series to the function and voila you get a list containing :
  
  ◉ Name
  ◉ Genre  
  ◉ Release year
  ◉ Motion Picture Rating (MPAA) / Rating
  ◉ Length 
  ◉ Number of Seasons (None incase of movies)
  ◉ Story Line in 1-2 sentences
  ◉ IMDb rating
  ◉ Number of people who rated
  ◉ User & critic reviews
  ◉ Meta Score (None in case of TV series)
  ◉ Awards (None in case of TV Series)
  ◉ IMDb page link to movie
  ◉ Movie/series Trailer link

# Example

>> print(search("titanic"))

>> {'name': 'Titanic', 'genre': ['Drama', 'Romance'], 'release_year': '1997', 'rated': 'PG-13', 'length': '3h 14m', 'seasons': None, 'story': 'A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.', 'rating': '7.9', 'rater': '1.2M', 'user_reviews': '3.3KUser reviews', 'critic_reviews': '264Critic reviews', 'meta_score': '75Metascore', 'awards': '126 wins & 83 nominations total', 'link': 'https://www.imdb.com/title/tt0120338/?ref_=fn_tt_tt_1', 'trailer_link': 'https://www.imdb.com//video/vi1740686617/?playlistId=tt0120338&ref_=tt_ov_vi'}


That is it for now 
  

# sort_reddit_saved:

sort_reddit_saved is a small python script that **sorts** saved Reddit posts with the following options:

* Newewst First
* Oldest First
* Ascendingly
* Ascendingly according to the subreddit
* Score
* Number of comments

whilst doing this it takes a **back-up** of all of them just in case anything goes wrong or for future restoring (will be added later).

###### It saves and sorts the **enire** saved history not just the *first* ~~1000~~ posts.

### Usage:

1. First you have to clone the repository *git clone https://github.com/ekhaled667/sort_reddit_saved.git*

2. Open sort.py using any text editor

3. Go to reddit preferences --> apps

4. Click *are you a developer? create an app*

5. Fill in the app name and for the redirect_url put in *http://localhost:65010/reddit_callback*

6. In sort.py change *sort_option.newewst* to:
   * *sort_option.oldest* for Oldest First
   * *sort_option.ascending* for Ascendingly sorting them
   * *sort_option.subreddit_ascending* for Ascendingly and Categorically sort them according to the subreddit name
   * *sort_option.score* for Score
   * *sort_option.number_of_comments* for Number of comments

7. Fill in the client_id & client_scret *client_id='<whatever>'* ~~without the <>~~ from the app you created in reddit

8. Now open the terminal again type *python sort.py* **make sure to open the terminal in the current directory, or use cd to navigate to it**

9. Authenticate with reddit

10. You'll be redirected to an offline page, copy the url.

11. Paste it in the terminal

12. Done

#### Note: It will be improved to work better with scripts

#### Note: It runs very slowly due to restrictions to the API calls on reddit *1 call per second* so expect this to run **_3n_** seconds where n is the number of saved posts
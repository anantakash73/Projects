 <div class="center">

  <p align="center">
  Data Science Screening
</p>
</div>

---

Please read these instructions carefully as this repository contains parts of your interview. You will be given your own private version of this repository to complete your work. Only you and Acme members can view your repository.

You should create a branch from `master` to do your work. Once you are satisfied, create a pull-request with your notes and merge your work into `master`. The pull-request will let us know you are finished.

## Q&A

The following sections contain questions that you should answer within this `README.md` file. Below each question, insert your response using Markdown.

### Tooling

Provide your preferences for each of the categories below. There's no right or wrong here.

1. Operating system?
  
    MacOS

2. Text editor?
    
    Jupyter and Visual Studio Code

3. Terminal type?

    iTerm
4. Scripting language?

    Python 3.6.8

## Real World Problem

Please use Python and Pandas for this project. Feel free to use any other libraries you may need. We have provided relevant files in the `data/` directory. The `start.csv` file contains stock positions (number of shares held) for the start of the day. The `trades.csv` file contains transactions (position changes) that have occurred throughout the day.

Parts 1, 2, and 3 are designed to take roughly an hour. Part 4 is free-form, and you're free to take however long you need. Please submit the entirety of your Python work contained within one script, along with your output files for all parts.

If you use libraries other than Pandas, please provide a `requirements.txt` as well as instructions on how to run your script. Assume we are going to clone your repo with no dependencies.

1. Read `start.csv`, `trades.csv`, and `table.html` into Pandas directly from Github.

2. Create an end of day file, `eod.csv`, that sums the start of day portfolio with the trades that have occurred during the day. This represents the start of day portfolio for the next day.

3. We have provided a scraped `.html` file that gives you the ticker, sector, and headquarters location of several companies. Produce a `sector.csv` file that shows the number of shares owned at the end of the day in each sector.

4. That wasn't so bad, right? What are some other interesting things you can do with this data? Maybe plot the headquarters locations using a geolocation API, or tell us how much money those trades would have made with today's market data? Entirely up to you.

Don't hesitate to ask if you have any questions, and good luck :)

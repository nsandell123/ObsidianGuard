This code queries a repository with 10 different question as outlined in `questions.txt`. It gets those responses and summarizes them to assess the security of any given plugin. 

Here's how to set it up
1. Clone the repository
2. Get a github personal access token
3. Get a Greptile token
4. Put those tokens in a .env file or export them in your terminal
5. Change the code to accomodate a repository of your liking (in the future, it will automatically populate)
6. Run `python main.py`

Note that the repository has to be indexed first before it can be queried, so if your repository hasn't already been indexed, run `python index_repository.py` before running `python main.py`

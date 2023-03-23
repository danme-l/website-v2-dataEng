# Data Engineering for dmeleras.ca
This is the repository containing scripts for all the data fetching and cleaning for posts on dmeleras.ca

## Method
When I find data that I'm interested in, I use a jupyter notebook to fetch and clean that data, and load it into a csv file to keep for my personal records and as a backup. Data gets loaded from the csv files to the database in a python script.

The `/debt` and `/world_economic_outlook` directories contain not fully polished work. Data here was loaded into the local database that I was using to develop the website before it went live. As of current writing (March 22), I still consider the website in 'proof-of-concept' mode and haven't fully eeked out the details of my dev and prod environments, which I am learning how to build on my own.


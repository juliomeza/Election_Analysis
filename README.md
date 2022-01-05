# Election Analysis

## Overview of Election Audit
The purpose of this project is to audit the recent local congressional election and send the results to the election commission.

## Election-Audit Results
* There were 369,711 total votes in this congressional election.

| COUNTY | VOTES | PERCENTAGE |
| ------------- | ------------- | ------------- |
| Jefferson | 38,855 | 10.5% |
| Denver | 306,055 | 82.8% |
| Arapahoe | 24,801 | 6.7% |
| TOTAL | 369,711 | 100.0% |
* Denver county has the largest numver of votes

| CANDIDATE | VOTES | PERCENTAGE |
| ------------- | ------------- | ------------- |
| Charles Casper Stockham | 85,213 | 23.0% |
| Diana DeGette | 272,892 | 73.8% |
| Raymon Anthony Doane | 11,606 | 3.1% |
| TOTAL | 369,711 | 100.0% |
* With 272,892 votes, which represents 73.8% of the total number of votes, Diana DeGette won the election.

## Election-Audit Summary
1. By adding a Boolean column (True or False), the same code, with small modification, can be used for ballots. Instead of counting the number of candidates, we can count the number or True (approve) versus False (disapprove).
2. Also, the same code can be used for Governor elections by adding a State column to the election_results.csv file

## Resources
* Data Source: election_results.csv
* Software: Python 3.9.7. Visual Studio Code 1.63

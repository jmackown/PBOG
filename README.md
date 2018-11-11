# PBOG
Post-Brexit Outrage Generator

## Concept

For years, Britain has been toiling under the spectre of Brexit.
It's the night before The Deadline when the 'government' decide it's all a huge mistake, and cancel the whole thing.

Suddenly The British Public are free!
But what will we complain about now...??
Who can we blame when terrible things happen?

*Introducing the Post-Brexit Outrage Generator!*

## What does it do?

It scrapes 300+ local news sites and grabs their front page headlines. These headlines are then analysed using our own proprietary ScholarHack Outrage Algorithm, and ranked. 


The results are then displayed on a page, ranked by most outrageous first. They are colour co-ordinated based on rank, and are accompanied by 'relevant' images (NLP is not 100% foolproof...).


## To Run:
1. Clone the repo
1. In the terminal, docker-compose up 
1. (install docker if you don't already have it, and repeat previous step....)
1. Wait patiently
1. When docker has finished loading stuff, go to http://0.0.0.0:5000/ragnarok/ (this creates the database)
1. Kill docker stuff with `ctrl+c`
1. Run docker-compose up again 
1. Wait patiently for it to scrape, populate the database and rank
1. Go to http://0.0.0.0:5000/ and feel suitably outraged

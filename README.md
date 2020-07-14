# What Is This
I would like an app where I enter words I encounter, get their definitions, example sentences, etc, and add my own notes, and save it all to review later. Notes might include my own example sentences, explanations of where I encounterd the word, etc. This is probably commonly available, but initial searches give bloated apps that want to push word-of-the-day content on me for a subscription.

# Initial notes
* created an API key for [Merriam Webster's free API](https://www.dictionaryapi.com/) and created a simple script that will get the "shortdef" of a word
* created an API key for The New York Times that can search articles by keyword, tried an example search in Insomnia.app, finding search results may or may not contain the word given, because only titles and abstracts are returned, not full articles
* Oxford dictionary also has [an API](https://developer.oxforddictionaries.com/signup?plan_ids[]=2357355970463) that may be useful
* created (this) Django app that takes `/word` requests, checks a local postgres database to see if we have the word saved, hits the MW API to get-and-save the word if not, and displays info about the word
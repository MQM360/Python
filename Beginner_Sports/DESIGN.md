I worked by myself (my partner had a change of mind)

PRE CODE:
Before any code was written I considered the parts my project would include need.
1. Data access
   A. Generic sports dataset +
   B. Somehow use the Harvard Rec center page + Other Facilities' websites
   C. Create my own data set - allows me to include things like pickle ball or table tennis which are not found on official websties.

I opted for 1C because there is more flexibility in how curated the sport list and location can be. Which could potentially grow later.
I created an excel sheet that included the following: ID,Name,Equipment,Type,Field,Players,Contact,Location. I deliberately incuded more
informaton than needed incase I wanted to increase functionality of the website later on. Research in all the sports facilities was done
by word of mouth, visiting, and searching the web.

2. Main Python file to run things from: Atleast 2 functions of SEARCH & RESULTS
3. Flask management [Known]
4. At least 2 HTML files of SEARCH and RESULTS (did not make sense to create a home when search could be the home page - like google)



PYTHON:
I had downloaded VS Code and began to setup my platforms, in hope of running everything locally. But ultimately opted with using cs50.io due
to its reliability. I talked to the duck and after some questions I realized that a db/SQL would be more efficient way to access information from instead of a CSV file.

    CSV to DB:
        Import csv, sqlite3 and os to have access to their functionalities. The program would need to locate a CSV file then run it through a function to read through the CSV file and out put the information one column and row at a time into a new db Table.

    APP.PY:
        Imported SQl from cs50 instead (manages queries a bit easier than manually as in CSV_to-DB file). Flask tot get access to website commuincation, flash for messages, redirect to route to a webpage, render_template to chose the html to render and request to access. Lines 11 - 24 were borrowed from the FINANCE and BIRTHDAY Psets. From my understanding they help manage and keep website navigation a bit easier.

        The SEARCH Function uses post because I would to later on grow the functionalities of the website to include a logged in / secure version. Checks if a name to search (Sport) was entered. if it does it queries the searced term sort-of like a root to a word (run in running, ball to baseball) using the "LIKE" and '%' + searchName + '%'. If nothing was found a message flashes tat it was not found and redirects to the same search page, otherwise it forwards it to the RESULTS page/function.

        The RESULTS function double checks the results and queries tat information to display in the webpage.

HTML:

    base_layout:
        Uses tthe chaining method to layout HTML files where this files contains the heading and Jinja code to extend the page without having it all be on sheet. This improves maintainablity and scalability.

    Search:
        Search button and function inplementation

    Results:
        Results table displayed using a loop and NEW button and function inplementation.

STATIC FOLDER:

    CSS:
        Some is borrowed from other psets
    PNG:
        H logo

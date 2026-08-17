# Netflix-user-data-analysis

## What it does

This project explores a Netflix user dataset using Python, pandas, Matplotlib, Seaborn, and Plotly. It covers data cleaning, exploratory analysis, and geographic and demographic visualizations to understand user behavior and subscription patterns.

## Steps covered

1. **Load and inspect data** — checks structure, column info, duplicates, and missing values
2. **Fix data types** — converts `Last_Login` to a proper datetime column
3. **Users by country** — bar chart of user counts per country
4. **Subscription type & favorite genre** — bar charts showing counts for each
5. **User distribution by country** — an interactive choropleth (world map) built with Plotly, shading each country by number of users
6. **Subscription type by country** — a grouped bar chart, plus a pivot table breaking down subscription types per country with totals
7. **Age distribution** — both a raw age count chart and a binned age-group breakdown (0-18, 19-30, 31-45, 46-60, 60+)
8. **Average watch time by country** — bar chart comparing average watch hours across countries
9. **Days since last login** — calculates how many days have passed since each user's last login, relative to the current date

## Key decisions

- **Watch_Time_Hours** was already a float in the raw data, so no type conversion was needed — an earlier version of this script mistakenly converted it to a timedelta first, which created problem while calculating watch time hours by country. 
- **Age binning** groups continuous ages into readable brackets (0-18, 19-30, etc.) to make the distribution easier to interpret than raw individual ages.
- **Choropleth map** (via Plotly) was chosen over a plain bar chart for country-level user distribution, since a map makes regional patterns easier to spot at a glance than a list of bars.

## Tools used

Python, pandas, Matplotlib, Seaborn, Plotly

## Output

The script prints summary tables (missing values, value counts, pivot tables, age/watch-time breakdowns) to the console and generates several charts: bar charts, a histogram, a grouped bar chart, and an interactive choropleth map.

## Status

Practice and Learning — built to strengthen exploratory data analysis and visualization skills across multiple libraries (pandas, Matplotlib, Seaborn, Plotly).

## Author

Suresh Ombase

# covid_streamlit
Creating a web application with Python and Streamlit using data from covid from https://www.kaggle.com/yamqwe/omicron-covid19-variant-daily-cases
which tracks the progression of the new omicron COVID-19 variant.

* The data
   * location- this is the country for which the variants information is provided;
   * date - date for the data entry;
   * variant - this is the variant corresponding to this data entry;
   * num_sequences - the number of sequences processed (for the country, variant and date);
   * perc_sequences - percentage of sequences from the total number of sequences (for the country, variant and date);
   * numsequencestotal - total number of sequences (for the country, variant and date);
   * Acknowledgements
[100416 rows x 6 columns]

Application: https://share.streamlit.io/jonatasfontele/covid_streamlit/main/covid_streamlit.py

It shows a graph of daily covid cases by variant or all variants and by country or all countries.

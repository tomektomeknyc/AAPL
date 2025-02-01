{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c4124e9c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "\n",
    "# Load the Excel file\n",
    "file_path = \"Apple Inc Financial Model.xlsx\"  # Ensure this matches your uploaded file name\n",
    "df = pd.read_excel(file_path)\n",
    "\n",
    "# Display the data\n",
    "st.write(\"## Excel Data Preview\")\n",
    "st.dataframe(df)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

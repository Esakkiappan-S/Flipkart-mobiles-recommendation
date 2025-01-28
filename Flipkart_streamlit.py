{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "5C4yFkA9nH2g",
    "outputId": "f763a1bb-53a0-41c5-c9b8-7a83b4353e98"
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-01-10 12:48:26.221 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-10 12:48:26.222 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-10 12:48:26.225 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-10 12:48:26.227 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-10 12:48:26.229 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-10 12:48:26.231 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-10 12:48:26.234 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-10 12:48:26.235 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-10 12:48:26.240 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-10 12:48:26.242 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-10 12:48:26.243 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-10 12:48:26.245 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-10 12:48:26.246 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-10 12:48:26.248 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-10 12:48:26.249 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-10 12:48:26.250 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-10 12:48:26.251 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-10 12:48:26.252 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-10 12:48:26.254 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-10 12:48:26.255 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-10 12:48:26.256 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-10 12:48:26.257 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-10 12:48:26.259 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-10 12:48:26.261 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-10 12:48:26.262 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-10 12:48:26.264 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-01-10 12:48:26.265 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st  # Import streamlit module\n",
    "import pandas as pd\n",
    "import pickle\n",
    "\n",
    "# Load the pickle file containing recommendations\n",
    "with open(\"most_recommended_mobile_phones.pkl\", 'rb') as f:\n",
    "    recommended_df = pickle.load(f)\n",
    "\n",
    "# List of Mobile_data to choose from - mobile prices, brands, ratings, and images\n",
    "Mobile_data = {\n",
    "    'Mobile_Brand': [\"SAMSUNG\", \"OnePlus\", \"POCO\", \"Motorola\", \"realme\"],  # brand information\n",
    "    'Model':[\"SAMSUNG Galaxy A14 5G\", \"OnePlus Nord CE 3 Lite 5G\", \"POCO M6 Plus 5G\", \"Motorola g45 5G\", \"realme P1 5G\"],\n",
    "    'Price': ['₹11,499', '₹14,888', '₹11,499', '₹10,999', '₹14,999'],  # price in INR\n",
    "    'Rating': [4.2, 4.4, 4.2, 4.3, 4.4],\n",
    "    'image': [\n",
    "        'https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/2/y/c/-original-imah4sssdf9pgz3e.jpeg?q=70',\n",
    "        'https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/p/r/b/nord-ce-3-lite-5g-ce2099-oneplus-original-imagzj42cctpjjze.jpeg?q=70',\n",
    "        'https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/9/b/n/-original-imah3afnqj84usyy.jpeg?q=70',\n",
    "        'https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/b/y/x/-original-imah3xk8crpgrg9y.jpeg?q=70',\n",
    "        'https://rukminim2.flixcart.com/image/312/312/xif0q/mobile/j/b/n/-original-imahyuhfzvybhaat.jpeg?q=70']\n",
    "     # image URLs\n",
    "}\n",
    "\n",
    "# Create a DataFrame for visualization\n",
    "df = pd.DataFrame(Mobile_data)\n",
    "\n",
    "# Remove '₹' symbol and commas from the 'Price' column and convert it to integer\n",
    "df['Price'] = df['Price'].replace({'₹': '', ',': ''}, regex=True).astype(int)\n",
    "\n",
    "# Merge df1 with recommended_df (assuming 'Model' is the key column)\n",
    "df = pd.merge(df, recommended_df, left_on='Model', right_on='Product_name', how='inner')\n",
    "\n",
    "# Streamlit Title of the app\n",
    "st.title('Mobile Product Recommendations')\n",
    "st.write(\"### Based on sentiment analysis from Reviews and Recommendations:\")\n",
    "\n",
    "# Sidebar for filtering options\n",
    "st.sidebar.header('Filter Options')\n",
    "\n",
    "# Multiselect for multiple Brand selection\n",
    "brand_options = df['Model'].unique().tolist()\n",
    "selected_brands = st.sidebar.multiselect(\"Select Brands:\", options=brand_options)\n",
    "\n",
    "# Price filter slider\n",
    "min_price, max_price = st.sidebar.slider('Select price range (in INR):', min_value=11000, max_value=15000, value=(11000, 15000))\n",
    "\n",
    "# Rating filter slider\n",
    "min_rating = st.sidebar.slider('Select minimum rating', min_value=0.0, max_value=5.0, value=3.0)\n",
    "\n",
    "# Filter data based on user input\n",
    "if selected_brands:\n",
    "    filtered_data = df[(df['Price'] >= min_price) & (df['Price'] <= max_price) & (df['Rating'] >= min_rating)]\n",
    "    filtered_data = filtered_data[filtered_data['Model'].isin(selected_brands)]\n",
    "    st.write(f'Showing results for products priced between ₹{min_price} and ₹{max_price} with rating above {min_rating}')\n",
    "\n",
    "    if filtered_data.empty:\n",
    "        st.write(\"No products found matching the selected criteria.\")\n",
    "    else:\n",
    "        st.subheader(f\"You Selected : {', '.join(selected_brands)}\")\n",
    "\n",
    "        # Display individual recommendations\n",
    "        for i, row in filtered_data.iterrows():\n",
    "            st.subheader(f\"**{row['Model']}**\")\n",
    "            st.image(row['image'], width=150)\n",
    "            st.write(f\"Price: ₹{row['Price']}\")\n",
    "            st.write(f\"Rating: {row['Rating']} ⭐\")\n",
    "\n",
    "            # Create a prompt using the loaded recommendation template\n",
    "            prompt = f\"\"\"\n",
    "\n",
    "            **Based on sentiment analysis, we recommend the following mobile phone:**\n",
    "\n",
    "            **Model**: {row['Product_name']}\n",
    "            - **Positive review score**: {row['average_compound_score']:.2f}\n",
    "            - **Positive Sentiment score**: {row['average_compound_sentiment']}\n",
    "            \"\"\"\n",
    "\n",
    "            st.write(prompt)\n",
    "            st.write(\"---\")\n",
    "else:\n",
    "    st.write(\"No brand selected yet.\")\n",
    "# streamlit Flipkart_streamlit.py"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "zFwKkC3fvhcl"
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "colab": {
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

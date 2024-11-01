import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set up the Streamlit app
st.title("Dice Roller")
st.write("Select the type of dice and how many rolls you'd like to make.")

# Dice options
dice_sides = [4, 6, 8, 10, 12]
selected_dice = st.selectbox("Choose dice type:", dice_sides)
number_of_rolls = st.number_input("Number of rolls:", min_value=1, value=1)

# Button to roll the dice
if st.button("Roll Dice"):
    results = np.random.randint(1, selected_dice + 1, size=number_of_rolls)
    
    # Show results
    st.write("You rolled:", results)
    
    # Display histogram
    st.subheader("Results Histogram")
    plt.figure(figsize=(10, 5))
    sns.histplot(results, bins=np.arange(1, selected_dice + 2) - 0.5, kde=False)
    plt.xticks(range(1, selected_dice + 1))
    plt.xlabel("Dice Value")
    plt.ylabel("Frequency")
    plt.title("Histogram of Dice Rolls")
    st.pyplot(plt)

    # Display statistical information
    st.subheader("Statistical Information")
    st.write(f"Total Rolls: {number_of_rolls}")
    st.write(f"Sum of Rolls: {np.sum(results)}")
    st.write(f"Mean: {np.mean(results):.2f}")
    st.write(f"Median: {np.median(results)}")
    st.write(f"Standard Deviation: {np.std(results):.2f}")

# Footer
st.write("Roll the dice again or change your selections!")

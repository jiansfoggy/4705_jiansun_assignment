import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Title of the Streamlit application
st.title("Simple Streamlit Plot")

# Introduction text
st.write("This application demonstrates how to display a basic plot using Streamlit and Matplotlib.")

# --- Data Generation ---
# Generate some sample data for the plot
# Using numpy to create an array of x values from 0 to 10
x = np.linspace(0, 10, 100)
# Calculate corresponding y values using a sine function
y = np.sin(x)

# --- Plotting with Matplotlib ---
# Create a Matplotlib figure and an axes object
fig, ax = plt.subplots()

# Plot the data on the axes
ax.plot(x, y)

# Add labels and a title to the plot
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_title("Sine Wave Plot")

# Display the Matplotlib plot in Streamlit
st.pyplot(fig)

# Add a small note or explanation below the plot
st.write("This is a simple sine wave generated and plotted using Matplotlib and displayed in Streamlit.")

# --- Interactive Element (Optional) ---
# Add a slider to change a parameter and update the plot
st.subheader("Interactive Plot (Change Frequency)")
frequency = st.slider("Select frequency:", 0.1, 5.0, 1.0)

# Generate new data based on the slider value
y_new = np.sin(x * frequency)

# Create a new Matplotlib figure for the interactive plot
fig_interactive, ax_interactive = plt.subplots()
ax_interactive.plot(x, y_new, color='red')
ax_interactive.set_xlabel("X-axis")
ax_interactive.set_ylabel("Y-axis")
ax_interactive.set_title(f"Sine Wave with Frequency: {frequency:.2f}")

# Display the interactive plot
st.pyplot(fig_interactive)

st.write("Adjust the slider above to see how the frequency of the sine wave changes dynamically.")

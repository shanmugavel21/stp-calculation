import streamlit as st
import math

st.title("STP Calculation")

atmospheric_pressure = st.number_input(
    "Enter atmospheric pressure",
    value=None,
    placeholder="Enter value"
)

atmospheric_temperature = st.number_input(
    "Enter atmospheric temperature (K)",
    value=None,
    placeholder="Enter value"
)

room_temperature = st.number_input(
    "Enter room temperature (C)",
    value=None,
    placeholder="Enter value"
)

vapour = st.number_input(
    "Enter vapour pressure",
    value=None,
    placeholder="Enter value"
)

barometric_pressure = st.number_input(
    "Enter barometric pressure",
    value=None,
    placeholder="Enter value"
)


if st.button("Calculate"):

    if None in [
        atmospheric_temperature,
        room_temperature,
        vapour,
        barometric_pressure
    ]:
        st.warning("Please enter all required values")

    else:

        # STP Formula
        stp = ((barometric_pressure + 22.06 - vapour) *
               atmospheric_temperature) / (760 * (room_temperature + 273))

        # Truncate STP to 5 decimals
        stp_display = math.floor(stp * 100000) / 100000

        # Final calculation
        result = 3600 * 0.75 * stp_display

        # Truncate final answer to 2 decimals
        result_display = math.floor(result * 100) / 100


        st.write("STP =", format(stp_display, ".5f"))
        st.write("STP/S =", format(result_display, ".2f"))
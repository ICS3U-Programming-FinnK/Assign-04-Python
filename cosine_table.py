#!/usr/bin/env python3
# Created by: Finn Kitor
# Created on: November 21st, 2023
# this program generates a loop for the cosine table between 0 to 360 degrees.
import math


def main() -> None:
    cosine_table = {}

    for degree in range(361):
        try:
            # Calculating the cosine value for the current degree
            cosine_value = math.cos(math.radians(degree))

            # Adding the degree and its corresponding cosine value to the table
            cosine_table[degree] = cosine_value

        except Exception as e:
            print(f"Error occurred while calculating cosine for degree {degree}: {e}")

    # Printing the cosine table
    for degree, cosine_value in cosine_table.items():
        print(f"Cosine of {degree} degrees: {cosine_value}")

    return cosine_table


if __name__ == "__main__":
    main()

# Score My Home

Score My Home is a data-driven web application designed to help homebuyers and renters make informed decisions by providing comprehensive property evaluations based on educational equity and environmental factors.

![Score My Home Screenshot](./frontend/VTHacks23/src/assets/logo.png)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Development Process](#development-process)
- [Challenges](#challenges)
- [Accomplishments](#accomplishments)
- [What We Learned](#what-we-learned)
- [Future Plans](#future-plans)
- [Team Info](#team-info)
- [License](#license)

## Introduction

The inspiration behind Score My Home stems from personal experiences with house searching, particularly during the second year of college. It became evident that real estate websites had certain shortcomings when it came to presenting comprehensive data on schools and the environment. This README provides an overview of the project's inspiration, features, tech stack, development process, challenges, accomplishments, and future plans.

## Features

- **User-Friendly Interface:** Score My Home offers a clean and intuitive interface for users to input their prospective address, ensuring it's valid and exists.
- **Backend Data Processing:** Leveraging machine learning algorithms and APIs, the application collects and processes relevant data to provide meaningful evaluations.
- **Data Transformation:** Collected data is transformed into an easy-to-understand score with subcategories, offering a comprehensive view of various factors.
- **Interactive Visualization:** The processed data is presented using a graphing library, creating visually engaging and informative results.
- **Top-Scoring House Listings:** Users receive a list of top-scoring houses near the entered address, complete with essential information and images to facilitate decision-making.

## Tech Stack

- **Backend:** Python with NLTK for API calls and machine learning.
- **Frontend:** TypeScript and React for a professional and efficient user experience.
- **CSS Framework:** Tailwind CSS for enhanced animations and coding style ease.

## Development Process

1. **Defining Goals and Features:** The project began with a clear definition of goals and essential features.
2. **Flow Diagram Design:** A comprehensive flow diagram was created to outline the application's functionality and data flow.
3. **Technology Stack Selection:** The technology stack was chosen carefully, considering familiarity, efficiency, and opportunities for learning.
4. **Backend Development:** The backend was developed using Python, NLTK, and machine learning for data processing.
5. **Frontend Setup:** The frontend was set up in React, integrating the Tailwind CSS framework for animations.
6. **Backend-Frontend Integration:** The frontend and backend were seamlessly connected using GET requests and CreateBrowser.

## Challenges

During development, the team encountered several challenges, including:

- **API Call Limits:** Dealing with API call limits restricted the amount of data that could be fetched and processed.
- **Glitched Address Entry Form:** Issues with the address entry form being glitched or obscured by other divs required UI adjustments.
- **Module Functionality Import:** Integrating functionality from one sub-module into another proved complex and required careful planning.
- **ChartJS Setup for Animations:** Configuring ChartJS for animations and interactive features posed technical challenges.
- **Learning Tailwind Commands:** Mastery of various Tailwind CSS commands was a learning curve for the team.
- **Designing the Mock Logo:** Creating the mock logo involved design challenges, demanding creativity and attention to detail.
- Getting listings from Homes.com without the unique identifier in the URL.

## Accomplishments

The team is proud of several accomplishments, including:

- **Data Integration:** Successfully finding and integrating sufficient data sources to support the entire project idea, ensuring comprehensive and reliable information.
- **Smooth Animations:** Achieving a high level of user experience by implementing smooth and intuitive animations on the frontend, enhancing the overall design.
- **Address Verification:** Implementing an automatic address verification process before running the application, ensuring data accuracy and reliability.
- **Machine Learning Integration:** Utilizing machine learning to compute weightage and scoring within different categories, providing users with meaningful and comprehensive insights.
- **API Utilization:** Making extensive use of numerous APIs, primarily Google APIs, for data retrieval and leveraging Apify scraping APIs to access essential information.
- **Comprehensive Rating Systems:** Displaying a wide variety and a significant amount of factors related to homes through two straightforward and informative rating systems, simplifying the decision-making process for users.
- Using Selenium to write a script that manually searches the listing on the search bar in Homes.com and then finds the picture and URL and sends it to the frontend for displaying.

## What We Learned

Participating in this hackathon provided the team with valuable insights and skills:

- **Effective Data Sourcing:** The importance of sourcing and integrating diverse data sets to create a comprehensive platform.
- **User-Centric Design:** Prioritizing the user experience by designing a user-friendly interface and integrating smooth animations.
- **API Integration:** Efficiently accessing and processing external data sources using various APIs.
- **Machine Learning Application:** Deploying machine learning models for practical purposes.
- **Advanced UI Development:** Enhancing frontend development skills.
- **Authentication Implementation:** Exploring user management and personalization features.
- **Visual Data Representation:** Demonstrating the effectiveness of presenting complex information in accessible and engaging ways using visuals and graphs.

## Future Plans

The project's future plans include:

- **Expanded Categories:** Implementing additional categories to provide even more comprehensive property scores, giving users a richer understanding of their prospective homes.
- **Google Autocomplete Integration:** Enhancing the address input experience by incorporating the Google Autocomplete API into the search bar, ensuring precise and efficient address entry.
- **Advanced UI Development:** Creating a more advanced user interface that can display multiple images of properties, allowing users to compare property values and value per unit of rating.
- **Authentication Integration:** Introducing authentication using Firebase to offer users the ability to save searches and facilitate their home-searching process with personalized features.
- **Enhanced Visuals and Graphs:** Expanding the use of visuals and graphs to depict subcategories in addition to the existing sections of the Pie Chart, providing users with more visual insights.
- **Distance Measurement Interface:** Implementing an interface to calculate and display the distance from the selected house to the best alternative house using the Google Navigation API, aiding users in assessing location convenience.

## Team Info

Meet the team behind Score My Home:

- **Aditya Kak**
  - Role: Backend Developer
  - Contact: adityakak04@email.com
- **Hariprasad Periyasamy**
  - Role: Frontend Developer
  - Contact: hariperi2009h@email.com
- **Harshal Arakala**
  - Role: Frontend Developer
  - Contact: harshal.arakala@email.com
- **Prabhath Tangella**
  - Role: Backend Developer
  - Contact: prabhathtangella22@email.com

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

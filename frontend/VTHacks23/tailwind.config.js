/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
      extend: {
          colors: {
              /* Go for around 3 to 5 primary colors [have shades for each color instead] */
              'gray-20': '#F8F4EB',
              'gray-50': '#EFE6E6',
              'gray-100': '#DFCCCC',
              'gray-500': '#5E0000',
              'primary-100': '#FFE1E0',
              'primary-300': '#FFA6A3',
              'primary-500': '#FF6B66',
              'secondary-400': '#FFCD58',
              'secondary-500': '#FFC132',
              'union-gold': '#b38708',
              'union-blue': '#002D55',
          },
          fontFamily: {
              dmsans: ['DM Sans', 'sans-serif'],
              montserrat: ['Montserrat', 'sans-serif'],
              roboto: ['Roboto', 'sans-serif'],
              opensans: ['Open Sans', 'sans-serif'],
          },
      },
      screens: {
          xs: '480px',
          sm: '768px',
          md: '1060px',
      },
  },
  plugins: [],
};
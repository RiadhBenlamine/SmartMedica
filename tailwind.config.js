/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,js}",
    "./node_modules/flowbite/**/*.js", // Add Flowbite content
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin'),  // Add Flowbite plugin
  ],
}
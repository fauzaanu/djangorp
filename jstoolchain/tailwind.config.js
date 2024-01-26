/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["../**/*.{html,js,py}"], // .py because django forms.py files could contain tailwind classes
    theme: {
        extend: {},
    },
    plugins: [],
}




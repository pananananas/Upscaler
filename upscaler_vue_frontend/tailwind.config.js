/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./public/**/*.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {

      colors: {
        'backgroundcolor': '#1A1A1A',
      },
      fontSize: {
        '2xsm': '0.5rem',
        xsm: '0.6rem',
        smm: '0.7rem',
        sm: '0.8rem',
        base: '1rem',
        xl: '1.25rem',
        '2xl': '1.563rem',
        '3xl': '1.953rem',
        '4xl': '2.441rem',
        '5xl': '3.052rem',
      },

      fontFamily: {
        'port-lligat-sans': ['Port Lligat Sans', 'sans-serif'], // Backup to sans-serif
        'port-lligat-slab': ['Port Lligat Slab', 'serif'],     // Backup to serif
      },

      screens: {
        'sm': '480px',
        'md': '768px',
        'lg': '1024px',
        'xl': '1280px',
        '2xl': '1536px',
      },
      dropShadow: {
        '3xl': '0 35px 35px rgba(0, 0, 0, 0.25)',
        '4xl': [
            '0 35px 35px rgba(0, 0, 0, 0.25)',
            '0 45px 65px rgba(0, 0, 0, 0.15)'
        ]
      }


    },
  },
  plugins: [],
}


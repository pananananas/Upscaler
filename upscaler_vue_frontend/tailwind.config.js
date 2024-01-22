/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./public/**/*.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  theme: {
    extend: {

      colors: {
        // 'backgroundcolor': '#1A1A1A',
      },
      fontSize: {
        '2xsm': '0.5rem',   // 8px
        xsm: '0.6rem',      // 10px
        smm: '0.7rem',      // 11px
        sm: '0.8rem',       // 12px
        base: '1rem',       // 16px
        xl: '1.25rem',      // 20px
        '2xl': '1.563rem',  // 25px
        '3xl': '1.953rem',  // 31px
        '4xl': '2.441rem',  // 39px
        '5xl': '3.052rem',  // 49px
        '6xl': '112px',     // 112px
        // '7xl': '130px',     // 112px
      },

      fontFamily: {
        'port-lligat-sans': ['Port Lligat Sans', 'sans-serif'],
        'port-lligat-slab': ['Port Lligat Slab', 'serif'],     
        'abril-fatface': ['Abril Fatface', 'serif'],
        'larken-sans':['larken', 'sans-serif'],       
        
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


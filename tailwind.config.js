module.exports = {
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./nuxt.config.{js,ts}",
  ],
  theme: {    
    extend: {
      textColor: theme => theme('colors'),
      textColor: {
        'primary': '#F0BF4C',
        'dark': '#515151',
        'themedark': '#221F1E'
      },
      borderWidth: {
        1: '1px'
      },
      spacing: {
        px: '1px',
        '120': '120px',
        '60': '60px',
      },
      zIndex: {
        n1: '-1',
        99: '99',
        999: '999',
        9999: '9999'
      },
      fontFamily: {
        'body': ["'Inter', sans-serif"],
        'play': ["'Playfair Display', serif"]
      },
      colors: {
        'primary': '#F0BF4C',
        'dark': '#515151',
        'themedark': '#221F1E',
        'light': '#f3f3f9',
        'bordercolor': '#d9d9d9'
      },
      keyframes: {
        'fadeUp': {
          '0%': {
            opacity: '0',
            transform: 'translateX(100px)'
          },
          '100%': {
            opacity: '1',
            transform: 'translateX(0)'
          },
        },
      },
      animation: {
        'fadeUp1': 'fadeUp 1s ease-in-out',
        'fadeUp2': 'fadeUp 1.4s ease-in-out',
        'fadeUp3': 'fadeUp 1.8s ease-in-out'
      },
    },
  },
  variants: {
  },
  plugins: [],
}

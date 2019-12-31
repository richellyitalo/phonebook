import { createGlobalStyle } from "styled-components";

export default createGlobalStyle`
  @import url('https://fonts.google.com/specimen/Source+Sans+Pro');

  * {
    padding: 0;
    margin: 0;
    outline: 0;
    box-sizing: border-box;
  }

  body {
    background: #353940;
    color: #fff;
    font-family: 'Source sans pro', sans-serif;
    text-rendering: optimizeLegibility !important;
    -webkit-font-smoothing: antialized !important;
  }

  html, body, #root {
    height: 100%;
  }

  input, button {
    font-family: 'Source sans pro', sans-serif;
  }

  button {
    cursor: pointer;
  }
`;

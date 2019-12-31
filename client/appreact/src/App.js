import React, { Fragment } from "react";
import { Provider } from "react-redux";
import Routes from "./routes";
import store from "./store";
import GlobalStyle from "./styles/global";

function App() {
  return (
    <Provider store={store}>
      <Fragment>
        <Routes />
        <GlobalStyle />
      </Fragment>
    </Provider>
  );
}

export default App;
